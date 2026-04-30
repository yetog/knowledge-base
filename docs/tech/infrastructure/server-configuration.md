---
tags:
  - infrastructure
  - tech
---

# Server Configuration Documentation

## 🖥️ Server Infrastructure Overview

### **System Specifications**

- **Operating System**: Ubuntu Linux 5.15.0-151-generic
- **Server Architecture**: x86\_64
- **Deployment Environment**: Cloud VPS
- **Domain**: zaylegend.com (with SSL/TLS)
- **Primary Services**: Nginx, Docker, Git, Node.js

### **Directory Structure**

```
/var/www/zaylegend/
├── apps/                          # Application containers
│   ├── chord-genesis/            # Music generation app
│   ├── dj-visualizer/           # Audio visualization
│   ├── fineline/                # Personal journal
│   ├── game-hub/               # Game collection
│   ├── knowledge-base/         # Static knowledge base
│   ├── spritegen/              # Sprite generator
│   ├── voice-assistant/        # AI voice interface
│   ├── contentforge/           # Content creation
│   └── docker-compose.yml     # Service orchestration
├── portfolio/                   # Main portfolio site
├── scripts/                     # Management scripts
├── infrastructure-docs/         # This documentation
├── deploy-portfolio-app.sh     # App deployment script
├── git-push-all.sh            # Git management script
└── *.sh                       # Various utility scripts
```

## 🌐 Nginx Configuration

### **Main Configuration Structure**

#### **Primary Config**: `/etc/nginx/conf.d/portfolio.conf`

```
# Auto-generated NGINX configuration for portfolio
server {
    listen 80;
    listen 443 ssl http2;
    server_name zaylegend.com www.zaylegend.com;

    # SSL Configuration
    ssl_certificate /etc/letsencrypt/live/zaylegend.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/zaylegend.com/privkey.pem;
    include /etc/letsencrypt/options-ssl-nginx.conf;
    ssl_dhparam /etc/letsencrypt/ssl-dhparams.pem;

    # Security Headers
    add_header X-Frame-Options "SAMEORIGIN" always;
    add_header X-Content-Type-Options "nosniff" always;
    add_header Referrer-Policy "no-referrer-when-downgrade" always;
    add_header X-XSS-Protection "1; mode=block" always;

    # Performance Optimization
    gzip on;
    gzip_vary on;
    gzip_min_length 1024;
    gzip_types text/plain text/css text/xml text/javascript 
               application/javascript application/xml+rss application/json;
}
```

### **Service Routing Configuration**

#### **Application Proxy Routes**

| Path | Target | Container | Description |
| --- | --- | --- | --- |
| `/` | `127.0.0.1:8080` | Portfolio Main | Root portfolio site |
| `/knowledge-base/` | Static Files | File System | HTML knowledge base |
| `/chord-genesis/` | `127.0.0.1:3001` | React App | Music generation |
| `/fineline/` | `127.0.0.1:3003` | React App | Personal journal |
| `/game-hub/` | `127.0.0.1:3004` | React App | Game collection |
| `/dj-visualizer/` | `127.0.0.1:3005` | React App | Audio visualization |
| `/spritegen/` | `127.0.0.1:3006` | React App | Sprite generation |
| `/voice-assistant/` | `127.0.0.1:3007` | React + API | Voice interface |
| `/zen-reset/` | `127.0.0.1:8081` | Static App | Wellness tool |

#### **Specialized Route Configurations**

**Static File Serving (Knowledge Base):**

```
location /knowledge-base/ {
    alias /var/www/zaylegend/apps/knowledge-base/;
    index index.html;
    try_files $uri $uri/ $uri.html /knowledge-base/index.html;

    # Cache optimization for static assets
    location ~* \.(css|js|png|jpg|jpeg|gif|ico|svg|woff|woff2|ttf|eot)$ {
        expires 1y;
        add_header Cache-Control "public, immutable";
    }
}
```

**WebSocket Support (Voice Assistant):**

```
location /voice-assistant/ {
    proxy_pass http://127.0.0.1:3007/;
    proxy_http_version 1.1;
    proxy_set_header Upgrade $http_upgrade;
    proxy_set_header Connection "upgrade";

    # Extended timeouts for voice processing
    proxy_connect_timeout 60s;
    proxy_send_timeout 60s;
    proxy_read_timeout 60s;

    # Large file uploads for audio
    client_max_body_size 50M;
}
```

## 🐳 Docker Infrastructure

### **Container Runtime Configuration**

#### **Docker Service Status**

```
# Docker daemon configuration
● docker.service - Docker Application Container Engine
     Loaded: loaded (/lib/systemd/system/docker.service; enabled; vendor preset: enabled)
     Active: active (running) since Sat 2025-08-02 23:03:00 UTC; 3 months 19 days ago
     Memory: 1.6G
     CPU: 1h 48min 31.267s
```

#### **Network Configuration**

```
# Docker networks
docker network ls
NETWORK ID     NAME                    DRIVER    SCOPE
bridge         bridge                  bridge    local
zaylegend-apps zaylegend-apps          bridge    local  
voice-network  voice-assistant-network bridge    local
```

### **Container Resource Allocation**

#### **Memory and CPU Limits**

```
# Default resource constraints
services:
  app:
    deploy:
      resources:
        limits:
          memory: 128M
          cpus: '0.5'
        reservations:
          memory: 64M
          cpus: '0.25'
```

#### **Health Check Configuration**

```
# Standard health check pattern
healthcheck:
  test: ["CMD", "curl", "-f", "http://localhost/"]
  interval: 30s
  timeout: 10s
  retries: 3
  start_period: 5s
```

## 🔒 Security Configuration

### **SSL/TLS Setup**

#### **Let's Encrypt Configuration**

```
# Certificate location and renewal
Certificates: /etc/letsencrypt/live/zaylegend.com/
├── fullchain.pem    # Full certificate chain
├── privkey.pem      # Private key
├── cert.pem         # Domain certificate
└── chain.pem        # Intermediate certificates

# Auto-renewal via cron
0 12 * * * /usr/bin/certbot renew --quiet
```

#### **SSL Security Settings**

```
# Modern SSL configuration
ssl_protocols TLSv1.2 TLSv1.3;
ssl_ciphers ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-GCM-SHA384;
ssl_prefer_server_ciphers off;

# Security headers
add_header Strict-Transport-Security "max-age=63072000" always;
add_header X-Frame-Options "SAMEORIGIN" always;
add_header X-Content-Type-Options "nosniff" always;
```

### **SSH Configuration**

#### **Key-Based Authentication**

```
# SSH keys for GitHub integration
~/.ssh/
├── github_actions_deploy      # Primary deployment key
├── github_actions_deploy.pub  
├── claude_code_ed25519        # Secondary key
└── claude_code_ed25519.pub
```

#### **Git Authentication Setup**

```
# SSH config for GitHub
Host github.com
    HostName github.com
    User git
    IdentityFile ~/.ssh/github_actions_deploy
    IdentitiesOnly yes
```

## ⚙️ Service Management

### **System Services**

#### **Nginx Service**

```
● nginx.service - A high performance web server and a reverse proxy server
     Loaded: loaded (/lib/systemd/system/nginx.service; enabled; vendor preset: enabled)
     Active: active (running) since Tue 2025-10-07 03:11:56 UTC; 1 month 15 days ago
     Tasks: 7 (limit: 9435)
     Memory: 23.8M
     CPU: 51.365s
```

#### **Service Control Commands**

```
# Nginx management
sudo systemctl start nginx
sudo systemctl stop nginx
sudo systemctl reload nginx      # Graceful config reload
sudo systemctl restart nginx
sudo systemctl status nginx

# Docker management
sudo systemctl start docker
sudo systemctl enable docker
sudo systemctl status docker
```

### **Log Management**

#### **Service Logs Location**

```
# System logs
/var/log/nginx/
├── access.log      # HTTP access logs
├── error.log       # Nginx error logs
└── portfolio.log   # Custom application logs

# Docker container logs
docker logs <container-name>
docker logs --follow --tail 50 <container-name>

# System journal logs
journalctl -u nginx.service
journalctl -u docker.service
```

#### **Log Rotation Configuration**

```
# Logrotate configuration for Nginx
/etc/logrotate.d/nginx
/var/log/nginx/*.log {
    daily
    missingok
    rotate 52
    compress
    delaycompress
    notifempty
    create 644 www-data adm
}
```

## 🔍 Monitoring and Diagnostics

### **Health Check Scripts**

#### **System Health Monitoring**

```
#!/bin/bash
# /var/www/zaylegend/scripts/health-check.sh

echo "=== System Health Check ==="

# Check disk space
echo "Disk Usage:"
df -h | grep -E "/$|/var"

# Check memory usage  
echo "Memory Usage:"
free -h

# Check running services
echo "Service Status:"
systemctl is-active nginx docker

# Check container health
echo "Container Health:"
docker ps --format "table {{.Names}}\t{{.Status}}\t{{.Ports}}"

# Check application endpoints
echo "Application Health:"
for port in 3001 3003 3004 3005 3006 3007; do
    if curl -f -s "http://localhost:$port/" > /dev/null; then
        echo "Port $port: ✅ Healthy"
    else
        echo "Port $port: ❌ Unhealthy"
    fi
done
```

### **Performance Monitoring**

#### **Resource Usage Tracking**

```
# Real-time monitoring
htop              # Interactive process viewer
iotop             # Disk I/O monitoring  
netstat -tulpn    # Network connections
docker stats      # Container resource usage

# System information
uname -a          # System information
uptime            # System uptime and load
lscpu             # CPU information
```

#### **Application Performance**

```
# Response time monitoring
curl -w "@curl-format.txt" -o /dev/null -s "https://zaylegend.com/"

# Where curl-format.txt contains:
#     time_namelookup:  %{time_namelookup}\n
#     time_connect:     %{time_connect}\n
#     time_appconnect:  %{time_appconnect}\n
#     time_pretransfer: %{time_pretransfer}\n
#     time_redirect:    %{time_redirect}\n
#     time_starttransfer: %{time_starttransfer}\n
#     ----------\n
#     time_total:       %{time_total}\n
```

## 🛠️ Maintenance Procedures

### **Regular Maintenance Tasks**

#### **Weekly Maintenance**

```
#!/bin/bash
# /var/www/zaylegend/scripts/weekly-maintenance.sh

# Update system packages
sudo apt update && sudo apt upgrade -y

# Docker cleanup
docker system prune -f
docker image prune -a -f

# Certificate renewal check
sudo certbot renew --dry-run

# Log rotation
sudo logrotate -f /etc/logrotate.conf

# Backup critical configs
tar -czf /var/backups/portfolio-config-$(date +%Y%m%d).tar.gz \
  /etc/nginx/conf.d/portfolio.conf \
  /var/www/zaylegend/infrastructure-docs/ \
  /var/www/zaylegend/*.sh
```

#### **Emergency Procedures**

**Service Recovery:**

```
# Quick service restart
sudo systemctl restart nginx docker

# Container recovery
docker-compose -f /var/www/zaylegend/apps/docker-compose.yml restart

# Full system recovery
sudo reboot
```

**Backup and Restore:**

```
# Create full backup
rsync -av --exclude 'node_modules' /var/www/zaylegend/ /backup/zaylegend-$(date +%Y%m%d)/

# Restore from backup
rsync -av /backup/zaylegend-latest/ /var/www/zaylegend/
```

---

**Server Location**: Cloud VPS  
**Management Interface**: SSH + Web Dashboard  
**Backup Strategy**: Daily automated + Weekly manual  
**Monitoring**: Real-time health checks + Log aggregation  
**Maintenance Window**: Sunday 02:00-04:00 UTC
