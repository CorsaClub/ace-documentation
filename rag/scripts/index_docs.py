#!/usr/bin/env python3
"""Index a PDF or Markdown file into a local txtai vector store.

Usage:
    python rag/scripts/index_docs.py <path/to/file.pdf|.md> [--db rag/db]
"""
import argparse
import re
import sys
from pathlib import Path

EMBEDDING_MODEL = "BAAI/bge-small-en-v1.5"

# --- Generic fallback chunking (used when the document doesn't look like the
# expected "asset" structure, e.g. an arbitrary PDF/MD indexed by a user) ---
CHUNK_SIZE = 800
CHUNK_OVERLAP = 150

# --- Structural chunking tuning ---
TABLE_CHUNK_SIZE = 2000
TABLE_ROW_OVERLAP = 2
CODE_CHUNK_SIZE = 2000
MIN_CHUNK_SIZE = 150

SPAN_RE = re.compile(r"<span[^>]*>\s*</span>")
HEADING_RE = re.compile(r"^(#{1,6})[ \t]+(.*)$", re.MULTILINE)
ASSET_RE = re.compile(r"^\d+\.\s+.+\[\s*\.\S+\s*\]$")
TABLE_ROW_RE = re.compile(r"^\|.*\|[ \t]*$")
SEPARATOR_ROW_RE = re.compile(r"^\|[\s:|-]+\|[ \t]*$")
FENCE_RE = re.compile(r"^```", re.MULTILINE)


def load_markdown(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def convert_to_markdown(path: Path) -> str:
    from markitdown import MarkItDown

    result = MarkItDown().convert(str(path))
    return result.text_content


def clean_heading_text(raw: str) -> str:
    text = SPAN_RE.sub("", raw).strip()
    text = text.strip("*").strip()
    return text


def split_by_headings(text: str) -> list[dict]:
    """Splits text into (heading, level, body) segments on every heading line,
    regardless of level — this doc's heading levels are inconsistent for the
    same logical role, so heading text/position is the only reliable signal."""
    matches = list(HEADING_RE.finditer(text))
    segments = []
    if not matches or matches[0].start() > 0:
        end = matches[0].start() if matches else len(text)
        segments.append({"heading": None, "level": 0, "body": text[:end]})
    for i, match in enumerate(matches):
        level = len(match.group(1))
        heading = clean_heading_text(match.group(2))
        body_start = match.end()
        body_end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        segments.append({"heading": heading, "level": level, "body": text[body_start:body_end]})
    return segments


def split_asset_sections(text: str) -> list[dict] | None:
    """Splits the doc into top-level asset sections (H1 headings matching the
    "N. Name [ .ext ]" pattern). Returns None if the pattern isn't found at
    all, so callers can fall back to generic chunking for unrelated docs."""
    segments = split_by_headings(text)
    asset_starts = [i for i, seg in enumerate(segments) if seg["level"] == 1 and seg["heading"] and ASSET_RE.match(seg["heading"])]
    if not asset_starts:
        return None

    assets = []
    for i, start in enumerate(asset_starts):
        end = asset_starts[i + 1] if i + 1 < len(asset_starts) else len(segments)
        asset_heading = segments[start]["heading"]
        # Everything between this asset's H1 and the next heading, plus every
        # subsequent segment up to (not including) the next asset, is this
        # asset's content — re-split that combined body by heading again to
        # get its flat list of sub-sections.
        body = segments[start]["body"] + "".join(seg["body"] if seg["heading"] is None else f"\n{'#' * seg['level']} {seg['heading']}\n{seg['body']}" for seg in segments[start + 1 : end])
        assets.append({"name": asset_heading, "sections": split_by_headings(body)})
    return assets


def looks_like_table(body: str) -> bool:
    lines = [l for l in body.splitlines() if l.strip()]
    for i in range(len(lines) - 1):
        if TABLE_ROW_RE.match(lines[i]) and SEPARATOR_ROW_RE.match(lines[i + 1]):
            return True
    return False


def looks_like_code(body: str) -> bool:
    return FENCE_RE.search(body) is not None


def parse_table_blocks(body: str) -> list[dict]:
    """Parses one or more pipe-table blocks out of body text, returning each
    as {"header": [header_line, separator_line], "rows": [row_lines]}."""
    lines = body.splitlines()
    blocks = []
    i = 0
    while i < len(lines):
        if TABLE_ROW_RE.match(lines[i]) and i + 1 < len(lines) and SEPARATOR_ROW_RE.match(lines[i + 1]):
            header = [lines[i], lines[i + 1]]
            rows = []
            j = i + 2
            while j < len(lines) and TABLE_ROW_RE.match(lines[j]):
                rows.append(lines[j])
                j += 1
            blocks.append({"header": header, "rows": rows})
            i = j
        else:
            i += 1
    return blocks


def merge_page_split_tables(blocks: list[dict]) -> list[dict]:
    """Marker re-splits one logical table across a PDF page break, repeating
    the header row on the next fragment. Merge consecutive blocks that share
    the same normalized header line."""

    def normalize(header):
        return re.sub(r"\s+", " ", header[0]).strip()

    merged = []
    for block in blocks:
        if merged and normalize(merged[-1]["header"]) == normalize(block["header"]):
            merged[-1]["rows"].extend(block["rows"])
        else:
            merged.append(dict(block))
    return merged


def chunk_table(body: str, prefix: str) -> list[str]:
    """Chunks a (possibly page-split) table by a char budget, never splitting
    a row, repeating the header in every chunk plus a small row overlap."""
    blocks = merge_page_split_tables(parse_table_blocks(body))
    chunks = []
    for block in blocks:
        header_text = "\n".join(block["header"])
        rows = block["rows"]
        if not rows:
            continue

        current: list[str] = []
        current_len = len(header_text)
        new_since_flush = 0

        def flush():
            nonlocal current, current_len, new_since_flush
            if new_since_flush == 0:
                return
            chunks.append(f"{prefix}\n\n{header_text}\n" + "\n".join(current))
            overlap = current[-TABLE_ROW_OVERLAP:] if TABLE_ROW_OVERLAP else []
            current = list(overlap)
            current_len = len(header_text) + sum(len(r) + 1 for r in overlap)
            new_since_flush = 0

        for row in rows:
            if new_since_flush > 0 and current_len + len(row) + 1 > TABLE_CHUNK_SIZE:
                flush()
            current.append(row)
            current_len += len(row) + 1
            new_since_flush += 1
        flush()
    return chunks


def chunk_code(body: str, prefix: str) -> list[str]:
    # Fence markers are pure formatting noise here (Marker sometimes closes
    # and reopens a fence mid-block around a page break) — drop them and
    # treat the remaining lines as one continuous logical block. Each tree
    # line is a complete field, so it's always safe to cut between lines.
    lines = [l for l in body.splitlines() if not FENCE_RE.match(l) and l.strip()]
    if not lines:
        return []

    chunks = []
    current: list[str] = []
    current_len = 0
    for line in lines:
        if current and current_len + len(line) + 1 > CODE_CHUNK_SIZE:
            chunks.append(f"{prefix}\n\n" + "\n".join(current))
            current, current_len = [], 0
        current.append(line)
        current_len += len(line) + 1
    if current:
        chunks.append(f"{prefix}\n\n" + "\n".join(current))
    return chunks


def chunk_prose(body: str, prefix: str) -> list[str]:
    text = body.strip()
    if not text:
        return []
    chunks = []
    start = 0
    while start < len(text):
        piece = text[start : start + CHUNK_SIZE].strip()
        if piece:
            chunks.append(f"{prefix}\n\n{piece}")
        start += CHUNK_SIZE - CHUNK_OVERLAP
    return chunks


def merge_tiny_tail(pieces: list[str]) -> list[str]:
    """Merges a small leftover final piece into the previous one instead of
    keeping a near-empty fragment as its own chunk."""
    if len(pieces) < 2:
        return pieces
    if len(pieces[-1]) < MIN_CHUNK_SIZE:
        merged = pieces[:-2] + [pieces[-2] + "\n" + pieces[-1].split("\n\n", 1)[-1]]
        return merged
    return pieces


def chunk_structural(text: str, source: str) -> list[dict] | None:
    text = SPAN_RE.sub("", text)
    assets = split_asset_sections(text)
    if not assets:
        return None

    chunks = []
    for asset in assets:
        for section in asset["sections"]:
            heading = section["heading"]
            body = section["body"]
            if not body.strip():
                continue
            prefix = f"{asset['name']} — {heading}" if heading else asset["name"]

            if looks_like_table(body):
                pieces = chunk_table(body, prefix)
            elif looks_like_code(body):
                pieces = chunk_code(body, prefix)
            else:
                pieces = chunk_prose(body, prefix)

            pieces = merge_tiny_tail(pieces)
            for piece in pieces:
                chunks.append({"text": piece, "source": source, "asset": asset["name"], "section": heading or ""})
    return chunks


def chunk_generic(text: str, source: str) -> list[dict]:
    """Fallback for documents that don't match the expected asset structure."""
    sections = re.split(r"\n(?=#{1,6}\s)", text)
    chunks = []
    for section in sections:
        section = section.strip()
        if not section:
            continue
        start = 0
        while start < len(section):
            piece = section[start : start + CHUNK_SIZE].strip()
            if piece:
                chunks.append({"text": piece, "source": source, "asset": "", "section": ""})
            start += CHUNK_SIZE - CHUNK_OVERLAP
    return chunks


def chunk_text(text: str, source: str) -> list[dict]:
    chunks = chunk_structural(text, source)
    if chunks:
        return chunks
    return chunk_generic(text, source)


def build_index(chunks: list[dict], db_path: Path) -> None:
    from txtai.embeddings import Embeddings

    embeddings = Embeddings(
        {
            "path": EMBEDDING_MODEL,
            "content": True,
            "backend": "faiss",
            "hybrid": True,
        }
    )
    data = [
        (i, {"text": c["text"], "source": c["source"], "asset": c["asset"], "section": c["section"]}, None)
        for i, c in enumerate(chunks)
    ]
    embeddings.index(data)
    db_path.mkdir(parents=True, exist_ok=True)
    embeddings.save(str(db_path))


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", help="Path to a .pdf or .md file to index")
    parser.add_argument("--db", default="rag/db", help="Vector DB output directory (default: ./rag/db)")
    args = parser.parse_args()

    src = Path(args.source)
    if not src.exists():
        sys.exit(f"File not found: {src}")

    if src.suffix.lower() == ".pdf":
        print(f"Converting {src.name} to Markdown via markitdown...")
        text = convert_to_markdown(src)
    elif src.suffix.lower() == ".md":
        text = load_markdown(src)
    else:
        sys.exit("Source must be a .pdf or .md file")

    chunks = chunk_text(text, source=src.name)
    if not chunks:
        sys.exit("No text extracted from source — nothing to index")
    print(f"{len(chunks)} chunks produced from {src.name}")

    print("Building vector index (first run downloads the embedding model)...")
    build_index(chunks, Path(args.db))
    print(f"Index written to {args.db}/")


if __name__ == "__main__":
    main()
