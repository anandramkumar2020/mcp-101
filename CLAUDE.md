# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

mcp-101 is an educational MCP (Model Context Protocol) server designed to demonstrate MCP fundamentals. It provides 5 simple tools (calculator operations + API bridge demo) to help audiences understand how MCP works.

## Commands

```bash
# Install dependencies
uv sync

# Run the MCP server directly
uv run python -m mcp_101.server

# Test with MCP Inspector (opens web UI at http://localhost:6274)
npx @modelcontextprotocol/inspector uv run python -m mcp_101.server
```

## Architecture

The codebase follows a two-file pattern separating concerns:

- **server.py**: MCP protocol layer - server initialization, tool registration with JSON schemas, tool call routing
- **interactions.py**: Business logic layer - tool implementations that return structured metadata dictionaries

### MCP Server Pattern

```
@server.list_tools()     -> Returns Tool objects with name, description, inputSchema
@server.call_tool()      -> Routes tool calls to interaction functions
stdio_server()           -> Handles JSON-RPC communication over stdin/stdout
```

### Tool Response Format

All tools return a consistent metadata structure:
```python
{
    "tool_name": "x_add",
    "mcp_server": "mcp-101",
    "operation": "addition",
    "inputs": {"a": a, "b": b},
    "result": result,
    "message": "MCP Tool x_add: {a} + {b} = {result}"
}
```

## Adding New Tools

1. Add implementation function in `interactions.py` returning the standard metadata dict
2. Add Tool object in `list_tools()` in `server.py` with JSON schema
3. Add routing case in `call_tool()` in `server.py`
