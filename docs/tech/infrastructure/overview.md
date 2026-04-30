---
tags:
  - infrastructure
  - tech
---

# Portfolio Infrastructure Overview

## 🏗️ Architecture Summary

**zaylegend.com** is a comprehensive portfolio platform built with a modern microservices architecture, featuring:

- **Domain**: zaylegend.com with SSL/TLS encryption
- **Server**: Ubuntu Linux with Nginx reverse proxy
- **Containerization**: Docker-based microservices
- **CI/CD**: GitHub Actions workflows
- **Version Control**: Git with automated deployment

## 🔧 Technology Stack

### **Core Infrastructure**

- **Operating System**: Ubuntu Linux 5.15.0-151
- **Web Server**: Nginx (reverse proxy + static file serving)
- **Containerization**: Docker + Docker Compose
- **SSL**: Let's Encrypt certificates
- **Process Management**: systemd

### **Application Stack**

- **Frontend**: React/Vite applications
- **Backend**: Node.js services
- **Static Sites**: Direct HTML serving
- **Networking**: Docker bridge networks

## 🌐 Service Architecture

```
Internet → zaylegend.com (SSL) → Nginx → Docker Services
                                  ↓
┌─────────────────────────────────────────────────────────────┐
│                    Nginx Reverse Proxy                     │
│                   (Port 80/443)                           │
└─────────────────────────────────────────────────────────────┘
                                  │
    ┌─────────────────────────────────────────────────────────────┐
    │                   Internal Routing                         │
    └─────────────────────────────────────────────────────────────┘
                                  │
        ┌─────────┬─────────┬─────────┬─────────┬─────────┬─────────┐
        │Portfolio│Knowledge│ Apps    │Services │Projects │ Tools   │
        │  8080   │  Static │Containers│  API   │ Pages  │ Utils   │
        └─────────┴─────────┴─────────┴─────────┴─────────┴─────────┘
```

## 📊 Service Inventory

### **Running Containers**

| Service | Port | Container | Status | Description |
| --- | --- | --- | --- | --- |
| Portfolio | 8080 | Static | Active | Main portfolio site |
| Knowledge Base | Static | Files | Active | Static HTML knowledge base |
| Chord Genesis | 3001 | React | Active | Music chord generation tool |
| Fineline | 3003 | React | Active | Personal journaling app |
| Game Hub | 3004 | React | Active | Retro game collection |
| DJ Visualizer | 3005 | React | Active | Audio visualization tool |
| Spritegen | 3006 | React | Active | Sprite generation tool |
| Voice Assistant | 3007 | React+Node | Unhealthy | Voice AI interface |
| Voice Assistant API | 5007 | Node.js | Healthy | Backend service |
| Zen Reset | 8081 | Static | Active | Meditation/wellness app |

## 🔄 Deployment Strategy

### **Container Orchestration**

- **Primary**: Individual Docker containers per service
- **Networking**: Bridge networks for service isolation
- **Volumes**: Local persistence for data
- **Restart Policy**: `unless-stopped` for resilience

### **CI/CD Pipeline**

1. **GitHub Actions** trigger on `main` branch push
2. **Test Phase**: Linting, building, Docker image creation
3. **Deploy Phase**: Automated deployment notifications
4. **Manual Deploy**: Local server-side scripts

### **Git Workflow**

- **Feature Branches** → **Main Branch** → **Production**
- Automated commit generation with change detection
- SSH key authentication for GitHub
- Local commits with automatic descriptions

## 🔐 Security Features

### **SSL/TLS Configuration**

- Let's Encrypt certificates with auto-renewal
- HTTPS redirect for all traffic
- Security headers (HSTS, X-Frame-Options, CSP)

### **Network Security**

- Internal service communication via Docker networks
- Nginx rate limiting and request filtering
- Isolated container environments

### **Access Control**

- SSH key-based git authentication
- Container isolation
- Nginx proxy protection

## 📈 Performance Optimizations

### **Caching Strategy**

- Static asset caching (1 year expiry)
- Gzip compression for text content
- Optimized Docker images

### **Load Balancing**

- Nginx upstream configurations
- Health check monitoring
- Graceful service restarts

## 🛠️ Management Tools

### **Deployment Scripts**

- `/var/www/zaylegend/deploy-portfolio-app.sh` - Individual app deployment
- `/var/www/zaylegend/git-push-all.sh` - Mass git operations
- `/var/www/zaylegend/portfolio-master.sh` - Infrastructure management

### **Monitoring & Maintenance**

- Docker container health checks
- Nginx access/error logs
- Service status monitoring via systemctl

## 🎯 Benefits of This Architecture

### **Scalability**

- Independent service scaling
- Easy addition of new applications
- Horizontal scaling capabilities

### **Maintainability**

- Service isolation for easier debugging
- Standardized deployment processes
- Version-controlled infrastructure

### **Reliability**

- Container restart policies
- Service health monitoring
- Automated backup through git

### **Developer Experience**

- Consistent development environments
- Automated deployment workflows
- Comprehensive documentation

---

**Last Updated**: November 2024  
**Maintained By**: Isayah Young Burke  
**Infrastructure Version**: v2.0
