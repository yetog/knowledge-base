# MCP Servers & REST APIs

Build tools that Claude can use directly, and APIs that anyone can call.

---

## Course Overview

This course covers two ways to expose your server's capabilities:

| Approach | Who Calls It | Best For |
|----------|--------------|----------|
| **MCP Servers** | Claude directly | AI assistant tools |
| **REST APIs** | Any HTTP client | External apps, scripts, webhooks |

Both are valuable. MCP lets Claude take action without you copying/pasting commands. APIs let external services integrate with your server.

---

## Modules

### 1. [MCP Fundamentals](mcp-fundamentals.md)
- What is Model Context Protocol?
- Tool definitions and handlers
- Input schemas
- Running an MCP server

### 2. [Building MCP Tools](mcp-building-tools.md)
- Server status tool
- Docker management
- Email sending
- Log reading
- Security best practices

### 3. [REST API Fundamentals](api-fundamentals.md)
- FastAPI basics
- GET, POST, PUT, DELETE
- Request/response models
- Error handling

### 4. [Building REST Endpoints](api-building-endpoints.md)
- Status endpoint
- App management
- Email API
- Brain CLI wrapper

### 5. [Deployment & Security](deployment-security.md)
- Running as a service
- Nginx reverse proxy
- Authentication
- Rate limiting

---

## Prerequisites

- Python 3.10+
- Basic command line skills
- Understanding of JSON

---

## Learning Outcomes

By the end of this course, you will be able to:

1. Build MCP servers that give Claude direct access to your tools
2. Create REST APIs for external integrations
3. Deploy both securely behind nginx
4. Understand when to use MCP vs API

---

## Code Examples

All code from this course is available at:

```
/var/www/zaylegend/mcp-servers/
├── shadow-server/     # MCP server example
└── shadow-api/        # REST API example
```

---

*Start with [MCP Fundamentals](mcp-fundamentals.md) →*
