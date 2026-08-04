PYTHON     := /opt/homebrew/bin/python3.12
VENV       := .venv
PIP        := $(VENV)/bin/pip
MARKER     := $(VENV)/bin/marker_single
OUTPUT_DIR := docs/markdown

RAG_DIR       := rag
RAG_VENV      := $(RAG_DIR)/.venv
RAG_PIP       := $(RAG_VENV)/bin/pip
RAG_PYTHON    := $(RAG_VENV)/bin/python
RAG_DB        := $(RAG_DIR)/db
RAG_DOC       := docs/markdown/ACE - Cars Physics Assets/ACE - Cars Physics Assets.md
RAG_IMAGE     := ace-rag-mcp

.PHONY: all convert setup clean distclean list rag-setup rag-index rag-serve rag-clean rag-distclean rag-docker-build rag-docker-run rag-test rag-docker-test rag-inspector rag-docker-inspector

all: list

## List available file IDs
list:
	@./scripts/convert.sh 2>/dev/null || true

## Install dependencies into the local virtualenv
setup: $(MARKER)

$(VENV)/bin/activate:
	$(PYTHON) -m venv $(VENV)
	$(PIP) install --quiet --upgrade pip

$(MARKER): $(VENV)/bin/activate
	$(PIP) install --quiet marker-pdf

## Convert a PDF by ID: make convert ID=1
convert: $(MARKER)
ifndef ID
	$(error ID is required. Usage: make convert ID=1)
endif
	./scripts/convert.sh $(ID)

## Remove generated output
clean:
	rm -rf "$(OUTPUT_DIR)"

## Remove virtualenv and output
distclean: clean
	rm -rf "$(VENV)"

## --- Local RAG (MCP vector search over the docs) ---
## Self-contained under rag/: its own virtualenv ($(RAG_VENV)), separate from
## $(VENV)/marker-pdf, to avoid dependency conflicts (txtai/markitdown pull
## newer pillow/pypdfium2).

## Install RAG dependencies (markitdown, mcp, txtai, sentence-transformers)
rag-setup: $(RAG_VENV)/bin/activate
	$(RAG_PIP) install --quiet -r $(RAG_DIR)/requirements.txt

$(RAG_VENV)/bin/activate:
	$(PYTHON) -m venv $(RAG_VENV)
	$(RAG_PIP) install --quiet --upgrade pip

## Build/rebuild the vector index: make rag-index [FILE=path/to/file.pdf]
rag-index: rag-setup
	$(RAG_PYTHON) $(RAG_DIR)/scripts/index_docs.py "$(if $(FILE),$(FILE),$(RAG_DOC))" --db "$(RAG_DB)"

## Run the MCP server standalone over stdio (manual testing only —
## MCP clients normally launch it themselves via their own config)
rag-serve: rag-setup
	$(RAG_PYTHON) $(RAG_DIR)/scripts/rag_mcp_server.py

## Remove the vector index
rag-clean:
	rm -rf "$(RAG_DB)"

## Remove the RAG virtualenv and index
rag-distclean: rag-clean
	rm -rf "$(RAG_VENV)"

## Build the Docker image for the MCP server
rag-docker-build:
	docker build -t $(RAG_IMAGE) -f $(RAG_DIR)/Dockerfile $(RAG_DIR)

## Run the dockerized MCP server standalone over stdio (manual testing only)
rag-docker-run: rag-docker-build
	docker run --rm -i -v "$(abspath $(RAG_DB))":/app/db:ro $(RAG_IMAGE)

## Smoke-test the local venv server with a real MCP client: make rag-test Q="..."
rag-test: rag-setup
	$(RAG_PYTHON) $(RAG_DIR)/scripts/test_search.py "$(if $(Q),$(Q),total mass measurement unit)"

## Smoke-test the Docker image with a real MCP client: make rag-docker-test Q="..."
rag-docker-test: rag-docker-build rag-index
	$(RAG_PYTHON) $(RAG_DIR)/scripts/test_search.py --docker "$(if $(Q),$(Q),total mass measurement unit)"

## Launch the interactive MCP Inspector (web UI) against the local venv server.
## Requires Node.js >= 22.19 (https://github.com/modelcontextprotocol/inspector).
rag-inspector: rag-setup
	npx -y @modelcontextprotocol/inspector@latest -- $(RAG_PYTHON) $(RAG_DIR)/scripts/rag_mcp_server.py

## Launch the interactive MCP Inspector (web UI) against the Docker image.
## Requires Node.js >= 22.19.
rag-docker-inspector: rag-docker-build
	npx -y @modelcontextprotocol/inspector@latest -- docker run --rm -i -v "$(abspath $(RAG_DB))":/app/db:ro $(RAG_IMAGE)
