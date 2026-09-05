# MCP Fundamentals

Learn the basics of Model Context Protocol and how it lets Claude use your tools directly.

---

## What is MCP?

Model Context Protocol (MCP) is a standard that lets AI assistants like Claude call your code directly. Instead of Claude telling you what command to run, Claude can execute it through your MCP server.

### Before MCP

```
You: "Check server status"
Claude: "Please run: brain status"
You: *runs command*
You: *copies output*
You: *pastes to Claude*
Claude: "I see your disk is at 15%..."
```

### With MCP

```
You: "Check server status"
Claude: *calls server_status tool*
Claude: "Your disk is at 15%, 23 containers running, nginx is active."
```

---

## How MCP Works

```
┌─────────────┐     stdio      ┌─────────────┐
│   Claude    │ ←──────────→   │ MCP Server  │
│   (Client)  │                │  (Python)   │
└─────────────┘                └─────────────┘
       │                              │
       │ 1. "What tools exist?"       │
       │ ─────────────────────────→   │
       │                              │
       │ 2. List of tools + schemas   │
       │ ←─────────────────────────   │
       │                              │
       │ 3. "Call tool X with args"   │
       │ ─────────────────────────→   │
       │                              │
       │ 4. Result                    │
       │ ←─────────────────────────   │
```

---

## MCP Server Structure

Every MCP server has two main functions:

### 1. `list_tools()` - Define Available Tools

```python
@server.list_tools()
async def list_tools():
    return [
        Tool(
            name="server_status",
            description="Get current server status",
            inputSchema={
                "type": "object",
                "properties": {},
                "required": []
            }
        )
    ]
```

### 2. `call_tool()` - Handle Tool Calls

```python
@server.call_tool()
async def call_tool(name: str, arguments: dict):
    if name == "server_status":
        result = subprocess.getoutput("brain status")
        return [TextContent(type="text", text=result)]
```

---

## Input Schema

The `inputSchema` tells Claude what parameters a tool accepts. It uses JSON Schema format:

### No Parameters

```python
inputSchema={
    "type": "object",
    "properties": {},
    "required": []
}
```

### String Parameter

```python
inputSchema={
    "type": "object",
    "properties": {
        "email": {
            "type": "string",
            "description": "Email address to send to"
        }
    },
    "required": ["email"]
}
```

### Multiple Parameters

```python
inputSchema={
    "type": "object",
    "properties": {
        "to": {"type": "string", "description": "Recipient"},
        "subject": {"type": "string", "description": "Subject line"},
        "body": {"type": "string", "description": "Message body"}
    },
    "required": ["to", "subject", "body"]
}
```

### Optional with Default

```python
inputSchema={
    "type": "object",
    "properties": {
        "lines": {
            "type": "integer",
            "description": "Lines to read",
            "default": 20
        }
    },
    "required": []  # Not required = optional
}
```

### Enum (Limited Choices)

```python
inputSchema={
    "type": "object",
    "properties": {
        "command": {
            "type": "string",
            "enum": ["status", "apps", "task list"],
            "description": "Command to run"
        }
    },
    "required": ["command"]
}
```

---

## Minimal MCP Server

Here's the smallest working MCP server:

```python
#!/usr/bin/env python3
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp.types import Tool, TextContent

server = Server("my-server")

@server.list_tools()
async def list_tools():
    return [
        Tool(
            name="hello",
            description="Say hello",
            inputSchema={"type": "object", "properties": {}}
        )
    ]

@server.call_tool()
async def call_tool(name: str, arguments: dict):
    if name == "hello":
        return [TextContent(type="text", text="Hello from MCP!")]
    return [TextContent(type="text", text=f"Unknown tool: {name}")]

async def main():
    async with stdio_server() as (read, write):
        await server.run(read, write, server.create_initialization_options())

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
```

---

## Running Your MCP Server

### Test Locally

```bash
# Install the SDK
pip install mcp

# Run the server (will wait for input)
python server.py
```

### Add to Claude Code

Edit `~/.claude.json`:

```json
{
  "mcpServers": {
    "my-server": {
      "command": "python3",
      "args": ["/path/to/server.py"]
    }
  }
}
```

Restart Claude Code. Your tools will be available.

---

## Key Concepts

| Concept | Description |
|---------|-------------|
| **Tool** | A function Claude can call |
| **inputSchema** | JSON Schema defining parameters |
| **TextContent** | The response format |
| **stdio** | Communication channel (stdin/stdout) |

---

## Next Steps

Now that you understand the basics:

1. [Building MCP Tools](mcp-building-tools.md) - Create practical tools
2. [REST API Fundamentals](api-fundamentals.md) - Compare with APIs

---

*Continue to [Building MCP Tools](mcp-building-tools.md) →*
