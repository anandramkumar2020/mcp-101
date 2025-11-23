"""
interactions.py - MCP Tool Implementations for mcp-101

This module contains the implementation of 5 educational tools that demonstrate
how MCP (Model Context Protocol) tools work. Each tool returns rich metadata
to help understand the flow of data through the MCP system.

Tools:
    - x_add: Addition of two integers
    - x_subtract: Subtraction of two integers
    - x_multiply: Multiplication of two integers
    - x_divide: Division of two integers (with zero handling)
    - x_api_demo: Demonstrates the API bridge pattern
"""

from typing import Any


def x_add(a: int, b: int) -> dict[str, Any]:
    """
    Add two integers together.

    This is a simple MCP tool that demonstrates basic arithmetic operations.
    The tool receives parameters from the AI model and returns a structured response.

    Args:
        a: First integer operand
        b: Second integer operand

    Returns:
        Dictionary containing operation metadata and result
    """
    result = a + b
    return {
        "tool_name": "x_add",
        "mcp_server": "mcp-101",
        "operation": "addition",
        "inputs": {"a": a, "b": b},
        "result": result,
        "message": f"MCP Tool x_add: {a} + {b} = {result}"
    }


def x_subtract(a: int, b: int) -> dict[str, Any]:
    """
    Subtract second integer from first integer.

    Args:
        a: First integer operand (minuend)
        b: Second integer operand (subtrahend)

    Returns:
        Dictionary containing operation metadata and result
    """
    result = a - b
    return {
        "tool_name": "x_subtract",
        "mcp_server": "mcp-101",
        "operation": "subtraction",
        "inputs": {"a": a, "b": b},
        "result": result,
        "message": f"MCP Tool x_subtract: {a} - {b} = {result}"
    }


def x_multiply(a: int, b: int) -> dict[str, Any]:
    """
    Multiply two integers together.

    Args:
        a: First integer operand
        b: Second integer operand

    Returns:
        Dictionary containing operation metadata and result
    """
    result = a * b
    return {
        "tool_name": "x_multiply",
        "mcp_server": "mcp-101",
        "operation": "multiplication",
        "inputs": {"a": a, "b": b},
        "result": result,
        "message": f"MCP Tool x_multiply: {a} * {b} = {result}"
    }


def x_divide(a: int, b: int) -> dict[str, Any]:
    """
    Divide first integer by second integer.

    Handles division by zero gracefully by returning an error message
    instead of raising an exception.

    Args:
        a: First integer operand (dividend)
        b: Second integer operand (divisor)

    Returns:
        Dictionary containing operation metadata and result (or error)
    """
    # Handle division by zero
    if b == 0:
        return {
            "tool_name": "x_divide",
            "mcp_server": "mcp-101",
            "operation": "division",
            "inputs": {"a": a, "b": b},
            "result": None,
            "error": "Division by zero is not allowed",
            "message": f"MCP Tool x_divide: Cannot divide {a} by zero"
        }

    result = a / b
    return {
        "tool_name": "x_divide",
        "mcp_server": "mcp-101",
        "operation": "division",
        "inputs": {"a": a, "b": b},
        "result": result,
        "message": f"MCP Tool x_divide: {a} / {b} = {result}"
    }


def x_api_demo(text: str) -> dict[str, Any]:
    """
    Demonstrate the API bridge pattern used in MCP servers.

    This tool shows how an MCP server can act as a bridge between an AI model
    and external APIs/services. In a real implementation, this would make an
    actual HTTP request to an external service.

    In the automaX project, hmi_touch() actually calls the HMI Driver API
    to interact with physical hardware through a similar pattern.

    Args:
        text: Input text to process (for demonstration)

    Returns:
        Dictionary containing simulated API response and explanation
    """
    # ==========================================================================
    # COMMENTED CODE: How to make an actual API call
    # ==========================================================================
    # In a real implementation, you would make an HTTP request like this:
    #
    # import httpx
    #
    # async def x_api_demo_real(text: str) -> dict:
    #     """Make actual API call to external service."""
    #     api_url = "http://localhost:8093/api/touch"
    #
    #     async with httpx.AsyncClient() as client:
    #         response = await client.post(
    #             api_url,
    #             json={"action": "touch", "data": text}
    #         )
    #         return response.json()
    #
    # ==========================================================================

    # Simulated response for demonstration purposes
    simulated_response = {
        "status": "success",
        "api_endpoint": "http://localhost:8093/api/touch",
        "processed_text": text,
        "simulated": True
    }

    return {
        "tool_name": "x_api_demo",
        "mcp_server": "mcp-101",
        "operation": "api_bridge_demo",
        "inputs": {"text": text},
        "result": simulated_response,
        "message": f"MCP Tool x_api_demo: Demonstrating API bridge pattern with input '{text}'",
        "note": "In automaX, hmi_touch() actually calls the HMI Driver API to interact with hardware"
    }
