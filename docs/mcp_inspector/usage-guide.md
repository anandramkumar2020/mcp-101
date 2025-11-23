# MCP Inspector Usage Guide

A quick guide to testing MCP servers using MCP Inspector.

---

## What is MCP Inspector?

MCP Inspector is a web-based tool from Anthropic for testing and debugging MCP (Model Context Protocol) servers. It lets you:

- View all available tools in your MCP server
- Test tools by providing inputs and seeing outputs
- Debug issues without needing a full AI client

---

## Starting MCP Inspector

### Command Format

```bash
npx @modelcontextprotocol/inspector <command-to-start-your-server>
```

### Example for mcp-101

```bash
npx @modelcontextprotocol/inspector uv run python -m mcp_101.server
```

### What Happens

1. MCP Inspector starts two components:
   - **Client UI** at `http://localhost:6274` (default)
   - **Proxy Server** at port `6277` (default)
2. A browser window opens automatically
3. Your MCP server starts in the background
4. Inspector connects to your server via stdio

### Custom Ports (Optional)

```bash
CLIENT_PORT=8080 SERVER_PORT=9000 npx @modelcontextprotocol/inspector uv run python -m mcp_101.server
```

---

## Using the Interface

### Step 1: Connect to Server

When the Inspector opens, click the **"Connect"** button to establish connection with your MCP server.

### Step 2: View Available Tools

After connecting, navigate to the **"Tools"** tab. You will see a list of all registered tools with their:

- Name
- Description
- Input schema (parameters)

### Step 3: Test a Tool

1. Click on a tool name (e.g., `x_add`)
2. Fill in the required parameters in the input form
3. Click **"Run"** to execute the tool
4. View the JSON response in the output panel

---

## Quick Test Checklist

| Tool | Test Input | Expected Result |
|------|------------|-----------------|
| `x_add` | a=5, b=3 | result: 8 |
| `x_subtract` | a=10, b=4 | result: 6 |
| `x_multiply` | a=7, b=6 | result: 42 |
| `x_divide` | a=20, b=4 | result: 5.0 |
| `x_divide` | a=10, b=0 | error message |
| `x_api_demo` | text="hello" | simulated API response |

---

## Troubleshooting

| Issue | Solution |
|-------|----------|
| Inspector won't start | Ensure Node.js and npm are installed |
| Server not connecting | Check that `uv sync` was run successfully |
| Tools not showing | Verify server.py has `@server.list_tools()` decorator |
| Port already in use | Close other Inspector instances or use a different port |

---

## Stopping the Inspector

Press `Ctrl+C` in the terminal where you started the Inspector.

---

## Learn More

- [MCP Documentation](https://modelcontextprotocol.io)
- [MCP Inspector GitHub](https://github.com/modelcontextprotocol/inspector)
