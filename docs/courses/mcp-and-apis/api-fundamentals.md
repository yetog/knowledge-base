# REST API Fundamentals

Learn how to build REST APIs with FastAPI - auto-generated docs, type validation, and clean design.

---

## Why FastAPI?

FastAPI is a modern Python web framework that makes building APIs fast:

| Feature | Benefit |
|---------|---------|
| **Auto-generated docs** | Swagger UI at `/docs` |
| **Type validation** | Pydantic catches errors |
| **Async support** | Handle concurrent requests |
| **Fast** | One of the fastest Python frameworks |

---

## MCP vs REST API

| Feature | MCP | REST API |
|---------|-----|----------|
| **Who calls it** | Claude directly | Any HTTP client |
| **Protocol** | stdio | HTTP |
| **Discovery** | Tool definitions | OpenAPI/Swagger |
| **Use case** | AI assistant tools | External integrations |

**Use MCP when:** Claude needs direct access to tools
**Use API when:** Scripts, webhooks, or external apps need access

---

## Your First API

```python
from fastapi import FastAPI

app = FastAPI(title="My API", version="1.0.0")

@app.get("/")
async def root():
    return {"message": "Hello, World!"}
```

Run it:

```bash
pip install fastapi uvicorn
uvicorn main:app --reload
```

Visit:
- API: http://localhost:8000/
- Docs: http://localhost:8000/docs

---

## HTTP Methods

### GET - Retrieve Data

```python
@app.get("/status")
async def get_status():
    return {"status": "running"}

# With path parameter
@app.get("/apps/{name}")
async def get_app(name: str):
    return {"name": name}

# With query parameter
@app.get("/logs")
async def get_logs(lines: int = 20):
    return {"lines": lines}
```

### POST - Create/Execute

```python
from pydantic import BaseModel

class EmailRequest(BaseModel):
    to: str
    subject: str
    body: str

@app.post("/email")
async def send_email(email: EmailRequest):
    # Send email
    return {"sent": True, "to": email.to}
```

### PUT - Update

```python
class TaskUpdate(BaseModel):
    title: str
    status: str

@app.put("/tasks/{id}")
async def update_task(id: int, task: TaskUpdate):
    return {"id": id, "updated": True}
```

### DELETE - Remove

```python
@app.delete("/tasks/{id}")
async def delete_task(id: int):
    return {"id": id, "deleted": True}
```

---

## Request Models (Pydantic)

Define request body structure with type hints:

```python
from pydantic import BaseModel
from typing import Optional

class CreateTask(BaseModel):
    title: str
    priority: int = 3  # Default value
    description: Optional[str] = None  # Optional field

@app.post("/tasks")
async def create_task(task: CreateTask):
    # task.title, task.priority, task.description
    return {"created": task.title}
```

FastAPI automatically:
- Validates types
- Returns 422 for invalid data
- Documents the schema in Swagger

---

## Response Models

Define what your API returns:

```python
class StatusResponse(BaseModel):
    disk: str
    memory: str
    containers: int
    timestamp: str

@app.get("/status", response_model=StatusResponse)
async def get_status():
    return StatusResponse(
        disk="55G/388G",
        memory="4G/16G",
        containers=23,
        timestamp="2026-05-24T12:00:00"
    )
```

---

## Error Handling

```python
from fastapi import HTTPException

@app.get("/apps/{name}")
async def get_app(name: str):
    app = find_app(name)

    if not app:
        raise HTTPException(
            status_code=404,
            detail=f"App not found: {name}"
        )

    return app

@app.post("/brain")
async def run_command(command: str):
    allowed = ["status", "apps"]

    if command not in allowed:
        raise HTTPException(
            status_code=400,
            detail=f"Command not allowed. Use: {allowed}"
        )

    return {"output": run(command)}
```

---

## Path and Query Parameters

```python
# Path parameter - required, part of URL
@app.get("/apps/{name}")
async def get_app(name: str):
    return {"name": name}

# Query parameter - optional, after ?
@app.get("/docker")
async def docker_list(all: bool = False, limit: int = 10):
    # /docker?all=true&limit=5
    return {"all": all, "limit": limit}

# Combined
@app.get("/logs/{name}")
async def get_logs(name: str, lines: int = 20):
    # /logs/nginx?lines=50
    return {"name": name, "lines": lines}
```

---

## Auto-Generated Documentation

FastAPI creates interactive docs automatically:

### Swagger UI
`http://localhost:8000/docs`

- Try endpoints directly
- See request/response schemas
- Test with real data

### ReDoc
`http://localhost:8000/redoc`

- Clean, readable documentation
- Good for sharing with others

---

## Structuring Your API

```python
from fastapi import FastAPI
from pydantic import BaseModel
import subprocess
from datetime import datetime

app = FastAPI(
    title="Shadow API",
    description="Server management API",
    version="1.0.0"
)

# ============ MODELS ============

class StatusResponse(BaseModel):
    timestamp: str
    disk: str
    memory: str

class EmailRequest(BaseModel):
    to: str
    subject: str
    body: str

# ============ ENDPOINTS ============

@app.get("/")
async def root():
    return {"name": "Shadow API", "version": "1.0.0"}

@app.get("/status", response_model=StatusResponse)
async def get_status():
    return StatusResponse(
        timestamp=datetime.now().isoformat(),
        disk=subprocess.getoutput("df -h / | tail -1 | awk '{print $3}'"),
        memory=subprocess.getoutput("free -h | awk '/Mem:/ {print $3}'")
    )

@app.post("/email")
async def send_email(email: EmailRequest):
    # Implementation
    return {"success": True}
```

---

## Testing Your API

### With curl

```bash
# GET request
curl http://localhost:8000/status

# GET with query params
curl "http://localhost:8000/docker?all=true"

# POST with JSON body
curl -X POST http://localhost:8000/email \
  -H "Content-Type: application/json" \
  -d '{"to": "test@example.com", "subject": "Hi", "body": "Hello"}'
```

### With Python

```python
import requests

# GET
r = requests.get("http://localhost:8000/status")
print(r.json())

# POST
r = requests.post("http://localhost:8000/email", json={
    "to": "test@example.com",
    "subject": "Hi",
    "body": "Hello"
})
print(r.json())
```

---

## Next Steps

- [Building REST Endpoints](api-building-endpoints.md) - Practical endpoint examples
- [Deployment & Security](deployment-security.md) - Production setup

---

*Continue to [Building REST Endpoints](api-building-endpoints.md) →*
