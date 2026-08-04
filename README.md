# Assetto Corsa EVO — Vehicle Physics Reference

Community documentation of **Assetto Corsa EVO** car physics assets (target version **0.7.1**): schemas, units, and field descriptions for modders and vehicle-dynamics work.

This is **not** official Kunos Simulazioni documentation. The Markdown source opens with a **Preface** that explains scope, methodology, and how inferred entries should be treated — read it before relying on any field.

## Repository layout


| Path                                         | Contents                                         |
| -------------------------------------------- | ------------------------------------------------ |
| `[docs/pdf/](./docs/pdf/)`                   | Source PDF reference                             |
| `[docs/markdown/](./docs/markdown/)`         | PDF converted to Markdown (via Marker)           |
| `[scripts/convert.sh](./scripts/convert.sh)` | PDF → Markdown conversion helper                 |
| `[rag/](./rag/)`                             | Local RAG / MCP server over the docs (see below) |




## Local RAG — vector search (MCP)

The repository includes a fully local RAG (*Retrieval-Augmented Generation*) system, kept under `[rag/](./rag/)`: the documentation (PDF or Markdown) is indexed into a `rag/db` vector store, queryable by any **MCP**-compatible assistant (Claude Code, Claude Desktop, Cursor, Windsurf, VS Code, …) via the `search_docs(query, top_k)` tool.

No data leaves your machine: indexing and search both run entirely locally (`sentence-transformers` embeddings, `txtai` vector index).

```
rag/
├── requirements.txt          # indexing + server (markitdown, mcp, txtai, sentence-transformers)
├── requirements-server.txt   # server only, no markitdown (lean Docker image)
├── Dockerfile                # Docker build for the MCP server
├── .dockerignore
└── scripts/
    ├── index_docs.py         # PDF/MD → chunks → vector index
    ├── rag_mcp_server.py     # stdio MCP server, search_docs tool
    └── test_search.py        # smoke-test: sends a real MCP query to the server
```



### 1. Install dependencies

```bash
make rag-setup
```

Or manually:

```bash
python3.12 -m venv rag/.venv
rag/.venv/bin/pip install -r rag/requirements.txt
```

> The RAG stack uses its **own** virtualenv (`rag/.venv`), separate from `.venv` (used by `make convert` / `marker-pdf`): `txtai`/`markitdown` pull `pillow`/`pypdfium2` versions incompatible with `marker-pdf`.



### 2. Run indexing

Index the already-generated Markdown (default file):

```bash
make rag-index
```

Index a different file (PDF or Markdown):

```bash
make rag-index FILE="docs/pdf/ACE - Cars Physics Assets.pdf"
```

Or directly in Python:

```bash
rag/.venv/bin/python rag/scripts/index_docs.py "docs/pdf/ACE - Cars Physics Assets.pdf" --db rag/db
```

This converts the PDF to Markdown (via `markitdown`), chunks the text, generates embeddings, and writes the index to `rag/db/`.

### 3. Connect the MCP server to your client

The server (`rag/scripts/rag_mcp_server.py`) runs over **stdio** — it's launched automatically by the MCP client, there's nothing to start manually (the `make rag-serve` target below is for manual testing only).

**Claude Code** — `[.mcp.json](./.mcp.json)` at the project root (already provided, versioned, shared with the team):

```json
{
  "mcpServers": {
    "ace-rag": {
      "command": "rag/.venv/bin/python",
      "args": ["rag/scripts/rag_mcp_server.py"]
    }
  }
}
```

Claude Code automatically detects `.mcp.json` when opening the project (confirmation prompted on first launch). CLI alternative: `claude mcp add ace-rag --scope project -- rag/.venv/bin/python rag/scripts/rag_mcp_server.py`.

**Claude Desktop** — edit `claude_desktop_config.json` (macOS: `~/Library/Application Support/Claude/claude_desktop_config.json`) and add, with the **absolute path** to the repo:

```json
{
  "mcpServers": {
    "ace-rag": {
      "command": "/absolute/path/to/ace-documentation/rag/.venv/bin/python",
      "args": ["/absolute/path/to/ace-documentation/rag/scripts/rag_mcp_server.py"]
    }
  }
}
```

**Cursor** — `.cursor/mcp.json` (at the project root, or `~/.cursor/mcp.json` for a global config), same format as above.

**Windsurf** — `~/.codeium/windsurf/mcp_config.json`, same format (`mcpServers` key).

Restart the client after editing. The `search_docs` tool should then appear in its MCP tool list.

### 4. Docker version of the MCP server

The server can run containerized, without installing Python/dependencies on the host machine. The vector index (`rag/db`, generated in step 2 on the host) is mounted read-only into the container.

Build:

```bash
make rag-docker-build
# equivalent to: docker build -t ace-rag-mcp -f rag/Dockerfile rag/
```

Manual test (stdio):

```bash
make rag-docker-run
# equivalent to: docker run --rm -i -v "$(pwd)/rag/db":/app/db:ro ace-rag-mcp
```

MCP client configuration (Claude Code, Claude Desktop, Cursor, Windsurf — same format everywhere), with the **absolute path** to `rag/db`:

```json
{
  "mcpServers": {
    "ace-rag": {
      "command": "docker",
      "args": [
        "run", "--rm", "-i",
        "-v", "/absolute/path/to/ace-documentation/rag/db:/app/db:ro",
        "ace-rag-mcp"
      ]
    }
  }
}
```

`-i` is required (keeps stdin open for the MCP stdio transport); don't add `-t`.

### 5. Test the server (local or Docker)

Three ways to check that `search_docs` responds correctly, without needing a full MCP client:

**a) Smoke-test script** (fast, no Node dependency) — sends a real MCP query to the server and prints the returned excerpts:

```bash
make rag-test Q="total mass measurement unit"          # local server (venv)
make rag-docker-test Q="total mass measurement unit"    # Docker server
```

Direct equivalent: `rag/.venv/bin/python rag/scripts/test_search.py "your query" [--docker] [--top-k 5]`.

**b) MCP Inspector** (official tool, interactive web UI to browse tools and run queries by hand):

```bash
make rag-inspector          # local server (venv)
make rag-docker-inspector   # Docker server
```

Opens `http://localhost:6274` in the browser (URL with token shown in the terminal). Requires **Node.js ≥ 22.19** (`nvm use` a recent version if needed) — [github.com/modelcontextprotocol/inspector](https://github.com/modelcontextprotocol/inspector).

**c) Manual server start** (just to check it launches without error — it doesn't accept keyboard input, it's a binary JSON-RPC protocol):

```bash
make rag-serve          # local server (venv)
make rag-docker-run      # Docker server
```



### Clean up the index

```bash
make rag-clean
```



## Report a correction

Found a wrong unit, a shaky description, or a missing field?

→ **[Open a documentation correction issue](https://github.com/CorsaClub/ace-documentation/issues/new?template=documentation-correction.yml)**

Include the section, field ID (when relevant), current text, proposed change, and evidence (asset values, in-game behaviour, game version). Maintainers will review and update the reference.

If you already have a concrete edit ready, open a **Pull Request** instead — Issues remain preferred for “something is wrong, please fix it.”

## License

Released under **[CC BY 4.0](./LICENSE)**. You may share and adapt the material with appropriate credit.

Assetto Corsa EVO is a trademark of Kunos Simulazioni. This repository is an independent, non-commercial community project.