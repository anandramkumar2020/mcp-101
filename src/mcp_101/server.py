"""
server.py - MCP Server for mcp-101

This module sets up and runs an MCP (Model Context Protocol) server that exposes
educational tools for demonstrating MCP concepts. The server registers tools
defined in interactions.py and handles tool call routing.

MCP Server Architecture:
    1. Server Initialization - Create an MCP server instance with a name
    2. Tool Registration - Register functions as callable tools with schemas
    3. Tool Routing - Handle incoming tool calls and route to implementations
    4. Communication - Use stdio transport for communication with AI clients

Usage:
    Run directly: python -m mcp_101.server
    Or via entry point: mcp-101
"""

import json
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp.types import Tool, TextContent

# Import tool implementations from interactions module
from mcp_101.interactions import (
    x_add,
    x_subtract,
    x_multiply,
    x_divide,
    x_api_demo,
)


# =============================================================================
# MCP Server Initialization
# =============================================================================
# Create an MCP server instance. The server name is used to identify this
# server in logs and to clients connecting to it.

server = Server("mcp-101")


# =============================================================================
# Tool Registration
# =============================================================================
# Tools are registered using the @server.list_tools() decorator. This function
# returns a list of Tool objects that describe what tools are available and
# their input schemas (using JSON Schema format).

@server.list_tools()
async def list_tools() -> list[Tool]:
    """
    List all available tools in this MCP server.

    Each tool is defined with:
        - name: Unique identifier for the tool
        - description: Human-readable explanation of what the tool does
        - inputSchema: JSON Schema defining the expected parameters

    Returns:
        List of Tool objects describing available tools
    """
    return [
        Tool(
            name="x_add",
            description="Add two integers together. Returns the sum of a + b.",
            inputSchema={
                "type": "object",
                "properties": {
                    "a": {
                        "type": "integer",
                        "description": "First integer operand"
                    },
                    "b": {
                        "type": "integer",
                        "description": "Second integer operand"
                    }
                },
                "required": ["a", "b"]
            }
        ),
        Tool(
            name="x_subtract",
            description="Subtract second integer from first. Returns a - b.",
            inputSchema={
                "type": "object",
                "properties": {
                    "a": {
                        "type": "integer",
                        "description": "First integer operand (minuend)"
                    },
                    "b": {
                        "type": "integer",
                        "description": "Second integer operand (subtrahend)"
                    }
                },
                "required": ["a", "b"]
            }
        ),
        Tool(
            name="x_multiply",
            description="Multiply two integers together. Returns a * b.",
            inputSchema={
                "type": "object",
                "properties": {
                    "a": {
                        "type": "integer",
                        "description": "First integer operand"
                    },
                    "b": {
                        "type": "integer",
                        "description": "Second integer operand"
                    }
                },
                "required": ["a", "b"]
            }
        ),
        Tool(
            name="x_divide",
            description="Divide first integer by second. Returns a / b. Handles division by zero gracefully.",
            inputSchema={
                "type": "object",
                "properties": {
                    "a": {
                        "type": "integer",
                        "description": "First integer operand (dividend)"
                    },
                    "b": {
                        "type": "integer",
                        "description": "Second integer operand (divisor)"
                    }
                },
                "required": ["a", "b"]
            }
        ),
        Tool(
            name="x_api_demo",
            description="Demonstrate the API bridge pattern. Shows how MCP servers can connect AI models to external APIs. In automaX, this pattern is used by hmi_touch() to call the HMI Driver API.",
            inputSchema={
                "type": "object",
                "properties": {
                    "text": {
                        "type": "string",
                        "description": "Input text for the demo"
                    }
                },
                "required": ["text"]
            }
        ),
    ]


# =============================================================================
# Tool Call Routing
# =============================================================================
# The @server.call_tool() decorator registers a handler for incoming tool calls.
# When a client requests a tool execution, this function routes the call to
# the appropriate implementation in interactions.py.

@server.call_tool()
async def call_tool(name: str, arguments: dict) -> list[TextContent]:
    """
    Handle incoming tool calls and route to appropriate implementations.

    This function acts as a dispatcher, receiving tool call requests from
    AI clients and forwarding them to the correct implementation function.

    Args:
        name: The name of the tool to execute
        arguments: Dictionary of arguments passed to the tool

    Returns:
        List containing a TextContent object with the tool's response as JSON

    Raises:
        ValueError: If an unknown tool name is requested
    """
    # Route to the appropriate tool implementation
    if name == "x_add":
        result = x_add(arguments["a"], arguments["b"])
    elif name == "x_subtract":
        result = x_subtract(arguments["a"], arguments["b"])
    elif name == "x_multiply":
        result = x_multiply(arguments["a"], arguments["b"])
    elif name == "x_divide":
        result = x_divide(arguments["a"], arguments["b"])
    elif name == "x_api_demo":
        result = x_api_demo(arguments["text"])
    else:
        raise ValueError(f"Unknown tool: {name}")

    # Return the result as JSON-formatted text content
    # MCP uses TextContent to wrap tool responses
    return [TextContent(type="text", text=json.dumps(result, indent=2))]


# =============================================================================
# Server Entry Point
# =============================================================================

async def main():
    """
    Main entry point for the MCP server.

    Starts the server using stdio transport, which communicates via
    standard input/output streams. This is the standard way MCP servers
    communicate with AI clients like Claude Desktop.
    """
    async with stdio_server() as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            server.create_initialization_options()
        )


if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
