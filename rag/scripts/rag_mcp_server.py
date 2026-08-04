#!/usr/bin/env python3
"""Generic MCP server exposing local vector search over the rag/db txtai index.

Runs over stdio, so it works with any MCP client (Claude Code, Claude Desktop,
Cursor, Windsurf, VS Code, ...). Build the index first with scripts/index_docs.py.
"""
import os
from pathlib import Path

from mcp.server import MCPServer

DEFAULT_DB_PATH = Path(__file__).resolve().parent.parent / "db"
DB_PATH = Path(os.environ.get("RAG_DB_PATH", DEFAULT_DB_PATH))

# BAAI/bge-* models expect an instruction prefix on the query side only (not
# on indexed passages) for best retrieval — see index_docs.py EMBEDDING_MODEL.
QUERY_INSTRUCTION = "Represent this sentence for searching relevant passages: "

mcp = MCPServer("rag-docs")

_embeddings = None


def get_embeddings():
    global _embeddings
    if _embeddings is None:
        if not DB_PATH.exists():
            raise RuntimeError(
                f"No index found at {DB_PATH}. Run 'python scripts/index_docs.py <file>' first."
            )
        from txtai.embeddings import Embeddings

        _embeddings = Embeddings()
        _embeddings.load(str(DB_PATH))
    return _embeddings


@mcp.tool()
def search_docs(query: str, top_k: int = 5) -> list[dict]:
    """Search the local documentation vector index and return the most relevant excerpts.

    Args:
        query: natural language search query.
        top_k: number of results to return (default 5).
    """
    embeddings = get_embeddings()
    # txtai extracts LIMIT by regex from the SQL text itself (not a bindable
    # parameter), so it must be interpolated directly; top_k is safe here
    # since the MCP tool schema already validates it as an int.
    results = embeddings.search(
        f"select text, source, asset, section, score from txtai where similar(:query) limit {int(top_k)}",
        parameters={"query": QUERY_INSTRUCTION + query},
    )
    return [
        {
            "score": round(r["score"], 4),
            "text": r["text"],
            "source": r.get("source", "unknown"),
            "asset": r.get("asset", ""),
            "section": r.get("section", ""),
        }
        for r in results
    ]


if __name__ == "__main__":
    mcp.run()
