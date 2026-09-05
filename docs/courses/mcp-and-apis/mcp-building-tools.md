# Building MCP Tools

Create practical tools that let Claude manage your server, send emails, and more.

---

## Server Status Tool

The most basic useful tool - check server health:

```python
Tool(
    name="server_status",
    description="Get current server status including disk, memory, and services",
    inputSchema={"type": "object", "properties": {}, "required": []}
)
```

Handler:

```python
elif name == "server_status":
    disk = subprocess.getoutput("df -h / | tail -1 | awk '{print $3\"/\"$2\" (\"$5\" used)\"}'")
    memory = subprocess.getoutput("free -h | awk '/Mem:/ {print $3\"/\"$2}'")
    uptime = subprocess.getoutput("uptime -p")
    docker = subprocess.getoutput("docker ps -q | wc -l")
    nginx = subprocess.getoutput("systemctl is-active nginx")

    return [TextContent(type="text", text=f"""Server Status
Disk:     {disk}
Memory:   {memory}
Uptime:   {uptime}
Docker:   {docker} containers
Nginx:    {nginx}""")]
```

---

## Docker Management Tools

### List Containers

```python
Tool(
    name="docker_list",
    description="List Docker containers",
    inputSchema={
        "type": "object",
        "properties": {
            "all": {
                "type": "boolean",
                "description": "Include stopped containers",
                "default": False
            }
        },
        "required": []
    }
)
```

Handler:

```python
elif name == "docker_list":
    flag = "-a" if arguments.get("all", False) else ""
    result = subprocess.getoutput(
        f"docker ps {flag} --format 'table {{{{.Names}}}}\\t{{{{.Status}}}}\\t{{{{.Ports}}}}'"
    )
    return [TextContent(type="text", text=result)]
```

### Restart Container

```python
Tool(
    name="docker_restart",
    description="Restart a Docker container by name",
    inputSchema={
        "type": "object",
        "properties": {
            "name": {
                "type": "string",
                "description": "Container name"
            }
        },
        "required": ["name"]
    }
)
```

Handler:

```python
elif name == "docker_restart":
    container = arguments.get("name", "")

    # Validate container exists
    check = subprocess.getoutput(f"docker ps -a --filter name={container} -q")
    if not check:
        return [TextContent(type="text", text=f"Container not found: {container}")]

    result = subprocess.run(
        ["docker", "restart", container],
        capture_output=True, text=True
    )

    if result.returncode == 0:
        return [TextContent(type="text", text=f"Restarted: {container}")]
    else:
        return [TextContent(type="text", text=f"Failed: {result.stderr}")]
```

---

## Email Tool

Send emails through your configured mail system:

```python
Tool(
    name="send_email",
    description="Send an email from the server",
    inputSchema={
        "type": "object",
        "properties": {
            "to": {"type": "string", "description": "Recipient email"},
            "subject": {"type": "string", "description": "Subject line"},
            "body": {"type": "string", "description": "Message body"}
        },
        "required": ["to", "subject", "body"]
    }
)
```

Handler:

```python
elif name == "send_email":
    to = arguments.get("to", "")
    subject = arguments.get("subject", "")
    body = arguments.get("body", "")

    if not all([to, subject, body]):
        return [TextContent(type="text", text="Missing: to, subject, or body")]

    # Use shadow-mail or msmtp
    result = subprocess.run(
        ["shadow-mail", "send", to, subject, body],
        capture_output=True, text=True
    )

    if result.returncode == 0:
        return [TextContent(type="text", text=f"Email sent to {to}")]
    else:
        return [TextContent(type="text", text=f"Failed: {result.stderr}")]
```

---

## Log Reader Tool

Read recent entries from log files:

```python
Tool(
    name="read_log",
    description="Read recent lines from a log file",
    inputSchema={
        "type": "object",
        "properties": {
            "log_name": {
                "type": "string",
                "enum": ["shadow-mail", "maintenance", "backup", "nginx-error"],
                "description": "Log file to read"
            },
            "lines": {
                "type": "integer",
                "description": "Number of lines",
                "default": 20
            }
        },
        "required": ["log_name"]
    }
)
```

Handler:

```python
elif name == "read_log":
    log_map = {
        "shadow-mail": "/var/log/shadow-mail.log",
        "maintenance": "/var/log/server-maintenance.log",
        "backup": "/var/log/shadow-backup.log",
        "nginx-error": "/var/log/nginx/error.log"
    }

    log_name = arguments.get("log_name", "")
    lines = arguments.get("lines", 20)

    if log_name not in log_map:
        return [TextContent(type="text", text=f"Unknown log: {log_name}")]

    log_path = log_map[log_name]

    if os.path.exists(log_path):
        result = subprocess.getoutput(f"tail -{lines} {log_path}")
        return [TextContent(type="text", text=result or "(empty)")]
    else:
        return [TextContent(type="text", text=f"Log not found: {log_path}")]
```

---

## Brain CLI Wrapper

Wrap your existing CLI tools safely:

```python
Tool(
    name="run_brain",
    description="Run a brain CLI command",
    inputSchema={
        "type": "object",
        "properties": {
            "command": {
                "type": "string",
                "enum": ["status", "apps", "apps health", "task list", "task all"],
                "description": "Brain subcommand"
            }
        },
        "required": ["command"]
    }
)
```

Handler:

```python
elif name == "run_brain":
    command = arguments.get("command", "status")

    # Whitelist for safety
    allowed = ["status", "apps", "apps health", "task list", "task all"]
    if command not in allowed:
        return [TextContent(type="text", text=f"Not allowed. Use: {allowed}")]

    result = subprocess.getoutput(f"brain {command}")
    return [TextContent(type="text", text=result)]
```

---

## Security Best Practices

### 1. Whitelist Commands

Never accept arbitrary shell commands:

```python
# BAD - arbitrary command execution
result = subprocess.getoutput(arguments.get("command"))

# GOOD - whitelist allowed commands
allowed = ["status", "apps", "restart"]
if command not in allowed:
    return error
```

### 2. Validate All Input

```python
# Check required fields exist
if not arguments.get("name"):
    return error

# Sanitize file paths
if ".." in path or path.startswith("/"):
    return error
```

### 3. Use Enums

Limit choices to known-safe values:

```python
"enum": ["option1", "option2", "option3"]
```

### 4. Log Everything

```python
import logging
logging.info(f"Tool called: {name} with {arguments}")
```

### 5. Separate Servers by Access Level

- Read-only tools in one server
- Write/execute tools in another
- Sensitive operations require confirmation

---

## Complete Shadow Server

See the full implementation at:

```
/var/www/zaylegend/mcp-servers/shadow-server/server.py
```

Tools included:

| Tool | Description |
|------|-------------|
| `server_status` | Disk, memory, services |
| `app_health` | Check all portfolio apps |
| `docker_list` | List containers |
| `run_brain` | Brain CLI wrapper |
| `send_email` | Send email |
| `read_log` | Read log files |

---

*Continue to [REST API Fundamentals](api-fundamentals.md) →*
