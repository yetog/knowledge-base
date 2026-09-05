# Deployment & Security

Get your MCP servers and APIs running in production securely.

---

## Running as a Service

### Systemd Service (Recommended)

Create `/etc/systemd/system/shadow-api.service`:

```ini
[Unit]
Description=Shadow API
After=network.target

[Service]
Type=simple
User=www-data
Group=www-data
WorkingDirectory=/var/www/zaylegend/mcp-servers/shadow-api
ExecStart=/usr/bin/python3 -m uvicorn api:app --host 127.0.0.1 --port 8000
Restart=always
RestartSec=5

[Install]
WantedBy=multi-user.target
```

Enable and start:

```bash
sudo systemctl daemon-reload
sudo systemctl enable shadow-api
sudo systemctl start shadow-api
sudo systemctl status shadow-api
```

### Management Commands

```bash
sudo systemctl start shadow-api    # Start
sudo systemctl stop shadow-api     # Stop
sudo systemctl restart shadow-api  # Restart
sudo systemctl status shadow-api   # Check status
journalctl -u shadow-api -f        # View logs
```

---

## Nginx Reverse Proxy

Expose your API at `/api/` on your domain:

```nginx
# In your server block
location /api/ {
    proxy_pass http://127.0.0.1:8000/;
    proxy_http_version 1.1;

    proxy_set_header Host $host;
    proxy_set_header X-Real-IP $remote_addr;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    proxy_set_header X-Forwarded-Proto $scheme;

    # WebSocket support (if needed)
    proxy_set_header Upgrade $http_upgrade;
    proxy_set_header Connection "upgrade";
}
```

Reload nginx:

```bash
sudo nginx -t && sudo nginx -s reload
```

Now accessible at: `https://yourdomain.com/api/`

---

## Authentication

### API Key (Simple)

```python
from fastapi import FastAPI, Header, HTTPException

API_KEY = "your-secret-key-here"  # Use environment variable!

app = FastAPI()

async def verify_api_key(x_api_key: str = Header(...)):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API key")
    return x_api_key

@app.get("/secure")
async def secure_endpoint(api_key: str = Depends(verify_api_key)):
    return {"message": "Authenticated!"}
```

Usage:

```bash
curl -H "X-API-Key: your-secret-key-here" http://localhost:8000/secure
```

### Environment Variables

Never hardcode secrets. Use environment variables:

```python
import os
API_KEY = os.environ.get("API_KEY", "default-dev-key")
```

Set in systemd:

```ini
[Service]
Environment="API_KEY=your-production-key"
```

Or use a `.env` file with `python-dotenv`:

```python
from dotenv import load_dotenv
load_dotenv()

API_KEY = os.getenv("API_KEY")
```

---

## Rate Limiting

Prevent abuse with rate limiting:

```python
from fastapi import FastAPI, Request
from slowapi import Limiter
from slowapi.util import get_remote_address

limiter = Limiter(key_func=get_remote_address)
app = FastAPI()
app.state.limiter = limiter

@app.get("/status")
@limiter.limit("10/minute")  # 10 requests per minute
async def get_status(request: Request):
    return {"status": "ok"}
```

Install: `pip install slowapi`

---

## CORS Configuration

Allow cross-origin requests (for web frontends):

```python
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://yourdomain.com"],  # Specific origins
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)
```

---

## Security Checklist

### Input Validation

- [x] Use Pydantic models for all inputs
- [x] Validate file paths (no `..` traversal)
- [x] Whitelist allowed commands
- [x] Use enums for limited choices

### Authentication

- [ ] Implement API key authentication
- [ ] Store keys in environment variables
- [ ] Use HTTPS only (nginx handles this)
- [ ] Rotate keys regularly

### Rate Limiting

- [ ] Limit requests per IP
- [ ] Limit requests per API key
- [ ] Return 429 when exceeded

### Logging

- [ ] Log all requests
- [ ] Log authentication failures
- [ ] Don't log sensitive data (passwords, keys)

### Network

- [ ] Bind to 127.0.0.1 (not 0.0.0.0)
- [ ] Use nginx as reverse proxy
- [ ] Enable HTTPS via Let's Encrypt

---

## Production Deployment Script

```bash
#!/bin/bash
# deploy-api.sh

set -e

echo "Deploying Shadow API..."

# Pull latest code
cd /var/www/zaylegend/mcp-servers/shadow-api
git pull origin main

# Install dependencies
pip install -r requirements.txt

# Restart service
sudo systemctl restart shadow-api

# Verify it's running
sleep 2
curl -s http://127.0.0.1:8000/ > /dev/null && echo "API is running" || echo "API failed to start"
```

---

## Monitoring

### Health Check Endpoint

```python
@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "timestamp": datetime.now().isoformat()
    }
```

### Cron Monitoring

Add to crontab:

```bash
*/5 * * * * curl -sf http://127.0.0.1:8000/health || echo "API down" | mail -s "Alert" admin@example.com
```

---

## MCP Server Security

MCP servers run locally via stdio, so network security is less of a concern. But:

### Whitelist Commands

```python
allowed = ["status", "apps", "task list"]
if command not in allowed:
    return error
```

### Separate Servers by Access Level

```
~/.claude.json:

{
  "mcpServers": {
    "read-only": {
      "command": "python3",
      "args": ["/path/to/read-only-server.py"]
    },
    "admin": {
      "command": "python3",
      "args": ["/path/to/admin-server.py"]
    }
  }
}
```

### Audit Logging

```python
import logging

logging.basicConfig(filename='/var/log/mcp-server.log')

@server.call_tool()
async def call_tool(name: str, arguments: dict):
    logging.info(f"Tool called: {name} args={arguments}")
    # ...
```

---

## Summary

| Component | Recommendation |
|-----------|----------------|
| **Process** | Systemd service |
| **Proxy** | Nginx reverse proxy |
| **Auth** | API keys in env vars |
| **Rate Limit** | slowapi or nginx |
| **TLS** | Let's Encrypt via nginx |
| **Monitoring** | Health check + cron |

---

## Course Complete!

You now know how to:

1. ✅ Build MCP servers for Claude
2. ✅ Create REST APIs with FastAPI
3. ✅ Deploy securely in production
4. ✅ Choose MCP vs API for your use case

### Code Reference

```
/var/www/zaylegend/mcp-servers/
├── shadow-server/     # MCP server
│   └── server.py
└── shadow-api/        # REST API
    └── api.py
```

---

*Back to [Course Index](index.md)*
