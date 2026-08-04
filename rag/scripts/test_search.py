#!/usr/bin/env python3
"""Smoke-test the RAG MCP server with a real MCP client, local or Docker.

Usage:
    rag/.venv/bin/python rag/scripts/test_search.py "your query" [--top-k 5] [--docker]
"""
import argparse
import asyncio
import json
from pathlib import Path

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

REPO_ROOT = Path(__file__).resolve().parent.parent.parent


async def run(command: str, args: list[str], query: str, top_k: int) -> None:
    params = StdioServerParameters(command=command, args=args)
    async with stdio_client(params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            tools = await session.list_tools()
            print(f"Tools available: {[t.name for t in tools.tools]}")
            result = await session.call_tool("search_docs", {"query": query, "top_k": top_k})
            for block in result.content:
                text = getattr(block, "text", block)
                try:
                    print(json.dumps(json.loads(text), indent=2, ensure_ascii=False))
                except (json.JSONDecodeError, TypeError):
                    print(text)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("query", help="Search query to send to search_docs")
    parser.add_argument("--top-k", type=int, default=3)
    parser.add_argument(
        "--docker",
        action="store_true",
        help="Test the Docker image (ace-rag-mcp) instead of the local venv server",
    )
    args = parser.parse_args()

    if args.docker:
        db = str(REPO_ROOT / "rag" / "db")
        command = "docker"
        cli_args = ["run", "--rm", "-i", "-v", f"{db}:/app/db:ro", "ace-rag-mcp"]
    else:
        command = str(REPO_ROOT / "rag" / ".venv" / "bin" / "python")
        cli_args = [str(REPO_ROOT / "rag" / "scripts" / "rag_mcp_server.py")]

    asyncio.run(run(command, cli_args, args.query, args.top_k))


if __name__ == "__main__":
    main()
