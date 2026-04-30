---
tags:
  - infrastructure
  - tech
---

# Docker Containerization Strategy

## 🐳 Container Architecture Overview

### **Philosophy**

- **Microservices Approach**: Each application runs in isolation
- **Standardized Environments**: Consistent runtime across development and production
- **Resource Optimization**: Minimal container footprints with multi-stage builds
- **Service Discovery**: Docker networks for inter-service communication

## 📦 Container Inventory

### **Production Containers**

| Container | Image | Port Mapping | Network | Status | Resources |
| --- | --- | --- | --- | --- | --- |
| **chord-genesis** | `chord-genesis:latest` | `3001:80` | zaylegend-apps | ✅ Healthy | React + Nginx |
| **fineline** | `fineline:latest` | `3003:80` | zaylegend-apps | ✅ Healthy | React + Nginx |
| **game-hub** | `game-hub:latest` | `3004:80` | zaylegend-apps | ✅ Healthy | React + Nginx |
| **dj-visualizer** | `apps_dj-visualizer` | `3005:80` | zaylegend-apps | ✅ Healthy | React + WebGL |
| **spritegen** | `apps_spritegen` | `3006:80` | zaylegend-apps | ✅ Healthy | React + Canvas |
| **voice-assistant-frontend** | `voice-assistant_frontend` | `3007:80` | voice-network | ⚠️ Unhealthy | React + WebRTC |
| **voice-assistant-backend** | `voice-assistant_backend` | `5007:5001` | voice-network | ✅ Healthy | Node.js API |
| **zen-reset** | `zen-reset:latest` | `8081:80` | default | ✅ Healthy | Static HTML |

### **Container Resource Usage**

```
# Real-time container stats
CONTAINER           CPU %     MEM USAGE     MEM %     NET I/O
chord-genesis       0.01%     45.2MB        0.48%     1.2kB / 648B
fineline            0.00%     42.1MB        0.45%     896B / 432B  
game-hub            0.02%     48.7MB        0.52%     2.1kB / 1.2kB
dj-visualizer       0.01%     44.3MB        0.47%     1.8kB / 924B
spritegen           0.00%     43.9MB        0.47%     1.1kB / 567B
voice-assistant-fe  0.05%     52.3MB        0.56%     3.4kB / 2.1kB
voice-assistant-be  0.08%     78.9MB        0.84%     4.7kB / 3.2kB
zen-reset           0.00%     12.8MB        0.14%     432B / 234B
```

## 🏗️ Build Strategy

### **Multi-Stage Build Pattern**

#### **Standard React Application Dockerfile**

```
# Stage 1: Build Environment
FROM node:18-alpine AS builder
WORKDIR /app

# Copy dependency files
COPY package*.json ./
RUN npm ci --only=production

# Copy source code and build
COPY . .
ARG VITE_BASE_PATH=/app-name/
ENV VITE_BASE_PATH=$VITE_BASE_PATH
RUN npm run build

# Stage 2: Production Environment  
FROM nginx:alpine AS production
COPY --from=builder /app/dist /usr/share/nginx/html

# Custom nginx configuration
COPY nginx.conf /etc/nginx/conf.d/default.conf

# Health check
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
  CMD curl -f http://localhost/ || exit 1

EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
```

#### **Node.js Backend Dockerfile**

```
# Voice Assistant Backend Example
FROM node:18-alpine AS base
WORKDIR /app

# Install dependencies
COPY package*.json ./
RUN npm ci --only=production

# Copy application code
COPY . .

# Create non-root user
RUN addgroup -g 1001 -S nodejs && \
    adduser -S nodejs -u 1001

# Switch to non-root user
USER nodejs

# Health check for API
HEALTHCHECK --interval=30s --timeout=3s --start-period=10s --retries=3 \
  CMD curl -f http://localhost:5001/health || exit 1

EXPOSE 5001
CMD ["node", "server.js"]
```

### **Nginx Configuration Templates**

#### **React SPA Configuration**

```
# Standard SPA nginx.conf
server {
    listen 80;
    server_name localhost;
    root /usr/share/nginx/html;
    index index.html;

    # Handle SPA routing
    location / {
        try_files $uri $uri/ /index.html;
    }

    # Cache static assets
    location ~* \.(js|css|png|jpg|jpeg|gif|ico|svg|woff|woff2|ttf|eot)$ {
        expires 1y;
        add_header Cache-Control "public, immutable";
        access_log off;
    }

    # Gzip compression
    gzip on;
    gzip_types text/plain text/css application/json application/javascript text/xml application/xml application/xml+rss text/javascript;
    gzip_min_length 1000;

    # Security headers
    add_header X-Frame-Options "SAMEORIGIN" always;
    add_header X-Content-Type-Options "nosniff" always;
    add_header Referrer-Policy "no-referrer-when-downgrade" always;
}
```

## 🌐 Network Architecture

### **Docker Networks**

#### **Application Network**

```
# zaylegend-apps bridge network
networks:
  app-network:
    driver: bridge
    name: zaylegend-apps
    ipam:
      driver: default
      config:
        - subnet: 172.19.0.0/16
          gateway: 172.19.0.1
```

#### **Service-Specific Networks**

```
# Voice Assistant dedicated network
voice-network:
  driver: bridge
  name: voice-assistant-network
  internal: false  # Allows external access
```

### **Port Management Strategy**

#### **Port Allocation**

```
System Ports (Reserved):
- 80: HTTP (Nginx)
- 443: HTTPS (Nginx)
- 22: SSH
- 3000: Development (reserved)

Application Ports:
- 3001: Chord Genesis
- 3003: Fineline  
- 3004: Game Hub
- 3005: DJ Visualizer
- 3006: Spritegen
- 3007: Voice Assistant Frontend
- 3008-3020: Available for new apps

API Ports:
- 5007: Voice Assistant Backend
- 5008-5020: Available for APIs

Utility Ports:
- 8080: Portfolio Main (internal)
- 8081: Zen Reset
- 8082-8090: Available for utilities
```

## 📋 Docker Compose Orchestration

### **Multi-Service Composition**

```
# /var/www/zaylegend/apps/docker-compose.yml
version: '3.8'

services:
  dj-visualizer:
    build: ./dj-visualizer
    container_name: dj-visualizer
    ports: ["3005:80"]
    restart: unless-stopped
    networks: [app-network]
    labels:
      - "app.name=dj-visualizer"
      - "app.description=Audio visualization and DJ tools"
    environment:
      - NODE_ENV=production
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost/"]
      interval: 30s
      timeout: 10s
      retries: 3

networks:
  app-network:
    driver: bridge
    name: zaylegend-apps
```

### **Service-Specific Compositions**

#### **Voice Assistant (Multi-Container)**

```
# /var/www/zaylegend/apps/voice-assistant/docker-compose.yml
version: '3.8'

services:
  voice-assistant-frontend:
    build: ./frontend
    container_name: voice-assistant-frontend
    ports: ["3007:80"]
    depends_on: [voice-assistant-backend]
    networks: [voice-network]
    environment:
      - REACT_APP_API_URL=http://voice-assistant-backend:5001

  voice-assistant-backend:
    build: ./backend  
    container_name: voice-assistant-backend
    ports: ["5007:5001"]
    networks: [voice-network]
    volumes:
      - voice-data:/app/data
    environment:
      - NODE_ENV=production
      - PORT=5001

volumes:
  voice-data:
    driver: local

networks:
  voice-network:
    driver: bridge
```

## 🔧 Container Management

### **Deployment Scripts**

#### **Individual App Deployment**

```
# /var/www/zaylegend/deploy-portfolio-app.sh
./deploy-portfolio-app.sh <app-name> <port> [rebuild]

# Examples:
./deploy-portfolio-app.sh fineline 3003 rebuild  # Force rebuild
./deploy-portfolio-app.sh new-app 3008           # Deploy new app
```

#### **Mass Container Operations**

```
# Start all services
docker-compose -f /var/www/zaylegend/apps/docker-compose.yml up -d

# Restart specific service
docker-compose restart dj-visualizer

# View all container logs
docker-compose logs -f --tail=50

# Update all containers
docker-compose pull && docker-compose up -d
```

### **Health Monitoring**

#### **Container Health Checks**

```
# Check container health status
docker ps --format "table {{.Names}}\t{{.Status}}\t{{.Ports}}"

# Monitor unhealthy containers
docker ps --filter health=unhealthy

# Inspect health check details
docker inspect --format='{{json .State.Health}}' container-name
```

#### **Resource Monitoring**

```
# Real-time stats
docker stats

# Resource usage by container
docker system df

# Container logs with timestamps
docker logs -t --since="1h" container-name
```

## 🎯 Optimization Strategies

### **Image Size Optimization**

1. **Multi-stage builds** to exclude build dependencies
2. **Alpine Linux** base images for minimal footprint
3. **Dependency optimization** with `npm ci --only=production`
4. **Layer caching** for faster rebuilds

### **Performance Tuning**

1. **Resource limits** to prevent container sprawl
2. **Health checks** for automatic recovery
3. **Restart policies** for high availability
4. **Network optimization** with bridge networks

### **Security Hardening**

1. **Non-root users** in containers
2. **Read-only file systems** where possible
3. **Minimal attack surface** with distroless images
4. **Network segmentation** with Docker networks

## 📊 Monitoring & Maintenance

### **Container Lifecycle Management**

```
# Automated cleanup
docker system prune -a --filter "until=72h"

# Image management
docker image prune -a --filter "until=7d"

# Log rotation
docker logs --since="7d" container-name > /var/log/app.log
```

### **Backup Strategy**

```
# Volume backups
docker run --rm -v volume-name:/backup-source busybox tar -czf - /backup-source > backup.tar.gz

# Configuration backups
tar -czf docker-configs-$(date +%Y%m%d).tar.gz /var/www/zaylegend/apps/*/Dockerfile /var/www/zaylegend/apps/*/docker-compose.yml
```

---

**Container Runtime**: Docker 24.0+  
**Orchestration**: Docker Compose v3.8  
**Total Containers**: 8 active services  
**Resource Utilization**: ~400MB total memory, <1% CPU  
**Uptime**: 99.9% availability with auto-restart policies
