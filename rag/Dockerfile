# MCP server for local vector search over the project's documentation.
# The vector index (rag/db) is built separately on the host with
# scripts/index_docs.py, then mounted read-only into the container.
FROM python:3.12-slim

WORKDIR /app

COPY requirements-server.txt .
RUN pip install --no-cache-dir -r requirements-server.txt

# Bake the embedding model into the image so containers start fast and work
# offline (must match EMBEDDING_MODEL in scripts/index_docs.py).
RUN python -c "from sentence_transformers import SentenceTransformer; SentenceTransformer('BAAI/bge-small-en-v1.5')"

COPY scripts/rag_mcp_server.py .

ENV RAG_DB_PATH=/app/db
# Model is baked in above — never hit the network at runtime, even to
# revalidate cache freshness.
ENV HF_HUB_OFFLINE=1
ENV TRANSFORMERS_OFFLINE=1

# MCP communicates over stdio: the client must run this image with `-i`
# (interactive, stdin kept open) and no allocated tty.
ENTRYPOINT ["python", "rag_mcp_server.py"]
