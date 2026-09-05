# Building REST Endpoints

Create practical API endpoints for server management.

---

## Status Endpoint

```python
from fastapi import FastAPI
from pydantic import BaseModel
import subprocess
from datetime import datetime

app = FastAPI(title="Shadow API")

class StatusResponse(BaseModel):
    timestamp: str
    disk: str
    memory: str
    uptime: str
    load: str
    docker_containers: int
    nginx: str

@app.get("/status", response_model=StatusResponse)
async def get_status():
    return StatusResponse(
        timestamp=datetime.now().isoformat(),
        disk=subprocess.getoutput("df -h / | tail -1 | awk '{print $3\"/\"$2}'"),
        memory=subprocess.getoutput("free -h | awk '/Mem:/ {print $3\"/\"$2}'"),
        uptime=subprocess.getoutput("uptime -p"),
        load=subprocess.getoutput("cat /proc/loadavg | awk '{print $1}'"),
        docker_containers=int(subprocess.getoutput("docker ps -q | wc -l")),
        nginx=subprocess.getoutput("systemctl is-active nginx")
    )
```

Test:
```bash
curl http://localhost:8000/status
```

---

## Apps Endpoints

### List All Apps

```python
@app.get("/apps")
async def list_apps():
    result = subprocess.getoutput("brain apps 2>/dev/null")
    return {"output": result}
```

### App Health Check

```python
@app.get("/apps/health")
async def apps_health():
    result = subprocess.getoutput("brain apps health 2>/dev/null")

    # Parse into structured data
    apps = []
    for line in result.strip().split('\n'):
        if '✓' in line or '✗' in line:
            status = "up" if '✓' in line else "down"
            parts = line.split()
            name = parts[-1] if parts else "unknown"
            apps.append({"name": name, "status": status})

    return {"apps": apps, "raw": result}
```

---

## Docker Endpoints

### List Containers

```python
@app.get("/docker")
async def docker_list(all: bool = False):
    flag = "-a" if all else ""
    result = subprocess.getoutput(
        f"docker ps {flag} --format '{{{{.Names}}}}|{{{{.Status}}}}|{{{{.Ports}}}}'"
    )

    containers = []
    for line in result.strip().split('\n'):
        if '|' in line:
            parts = line.split('|')
            containers.append({
                "name": parts[0],
                "status": parts[1] if len(parts) > 1 else "",
                "ports": parts[2] if len(parts) > 2 else ""
            })

    return {"containers": containers, "count": len(containers)}
```

### Restart Container

```python
from fastapi import HTTPException

@app.post("/docker/{name}/restart")
async def restart_container(name: str):
    # Check container exists
    check = subprocess.getoutput(f"docker ps -a --filter name=^{name}$ -q")
    if not check:
        raise HTTPException(status_code=404, detail=f"Container not found: {name}")

    # Restart it
    result = subprocess.run(
        ["docker", "restart", name],
        capture_output=True, text=True
    )

    if result.returncode == 0:
        return {"restarted": name, "success": True}
    else:
        raise HTTPException(status_code=500, detail=result.stderr)
```

---

## Email Endpoint

```python
class EmailRequest(BaseModel):
    to: str
    subject: str
    body: str

class EmailResponse(BaseModel):
    success: bool
    message: str

@app.post("/email", response_model=EmailResponse)
async def send_email(email: EmailRequest):
    result = subprocess.run(
        ["shadow-mail", "send", email.to, email.subject, email.body],
        capture_output=True, text=True
    )

    success = result.returncode == 0
    return EmailResponse(
        success=success,
        message="Email sent" if success else result.stderr.strip()
    )
```

---

## Brain CLI Wrapper

```python
class BrainCommand(BaseModel):
    command: str

@app.post("/brain")
async def run_brain(cmd: BrainCommand):
    allowed = ["status", "apps", "apps health", "task list", "task all"]

    if cmd.command not in allowed:
        raise HTTPException(
            status_code=400,
            detail=f"Command not allowed. Use: {allowed}"
        )

    result = subprocess.getoutput(f"brain {cmd.command}")
    return {"command": cmd.command, "output": result}
```

---

## Log Reader

```python
@app.get("/logs/{log_name}")
async def read_log(log_name: str, lines: int = 20):
    log_map = {
        "shadow-mail": "/var/log/shadow-mail.log",
        "maintenance": "/var/log/server-maintenance.log",
        "backup": "/var/log/shadow-backup.log",
        "nginx-access": "/var/log/nginx/access.log",
        "nginx-error": "/var/log/nginx/error.log"
    }

    if log_name not in log_map:
        raise HTTPException(
            status_code=404,
            detail=f"Unknown log. Choose from: {list(log_map.keys())}"
        )

    log_path = log_map[log_name]

    if not os.path.exists(log_path):
        return {"log": log_name, "lines": [], "message": "File not found"}

    result = subprocess.getoutput(f"tail -{lines} {log_path}")
    return {
        "log": log_name,
        "path": log_path,
        "lines": result.split('\n')
    }
```

---

## Task Management

```python
class TaskCreate(BaseModel):
    title: str
    priority: int = 3

@app.get("/tasks")
async def list_tasks():
    result = subprocess.getoutput("brain task list")
    return {"output": result}

@app.post("/tasks")
async def create_task(task: TaskCreate):
    result = subprocess.run(
        ["brain", "task", "add", task.title],
        capture_output=True, text=True
    )
    return {"created": task.title, "success": result.returncode == 0}

@app.post("/tasks/{id}/complete")
async def complete_task(id: int):
    result = subprocess.run(
        ["brain", "task", "done", str(id)],
        capture_output=True, text=True
    )
    return {"id": id, "completed": result.returncode == 0}
```

---

## Complete Example

See the full implementation at:

```
/var/www/zaylegend/mcp-servers/shadow-api/api.py
```

Run it:

```bash
cd /var/www/zaylegend/mcp-servers/shadow-api
python api.py
```

Visit: http://localhost:8000/docs

---

*Continue to [Deployment & Security](deployment-security.md) →*
