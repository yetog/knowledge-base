# Automation Tools

Production-ready deployment scripts and automation tools for managing containerized portfolio applications. These tools streamline the deployment process and ensure consistent, reliable application management.

## Portfolio App Deployment Script

A comprehensive bash script for deploying React/Vite applications as Docker containers with nginx integration. This script handles the entire deployment lifecycle from building to testing and provides detailed feedback throughout the process.

### 📋 Overview

The `deploy-portfolio-app.sh` script automates the deployment of portfolio applications by:

- Building Docker images with proper environment configuration
- Managing container lifecycle (stop, remove, start)
- Performing health checks and validation
- Providing nginx configuration guidance
- Testing JavaScript asset delivery
- Offering comprehensive deployment feedback

### 🚀 Key Features

#### Intelligent Port Management

- **Port Conflict Detection**: Automatically detects if the specified port is already in use
- **Container Recognition**: Identifies if the port is used by the same app (for rebuilds) or different container
- **Interactive Rebuilds**: Prompts user for rebuild confirmation when container exists
- **Force Rebuild Option**: Supports `rebuild` parameter for automated rebuilds

#### Comprehensive Validation

- **Directory Validation**: Ensures app directory exists before deployment
- **Required Files Check**: Validates presence of Dockerfile and package.json
- **Container Health Checks**: Tests container responsiveness after deployment
- **Asset Validation**: Verifies JavaScript files are serving correctly

#### Production-Ready Features

- **Error Handling**: Graceful failure handling with helpful error messages
- **Colored Output**: Clear, color-coded status messages for better readability
- **Restart Policies**: Configures containers with `unless-stopped` restart policy
- **nginx Integration**: Provides complete nginx configuration templates

### 📖 Usage Examples

```bash
# Deploy a new application
./deploy-portfolio-app.sh my-app 3003

# Force rebuild an existing application
./deploy-portfolio-app.sh chord-genesis 3001 rebuild

# Deploy with automatic rebuild confirmation
./deploy-portfolio-app.sh fineline 3008 rebuild
```

### 🔄 Deployment Workflow

1. **Validation Phase**
   - Validate command line arguments
   - Check app directory exists
   - Verify required files present
   - Check port availability
2. **Container Management**
   - Stop existing container if rebuilding
   - Remove old container and cleanup
   - Build new Docker image with proper base path
3. **Deployment Phase**
   - Start new container with correct port mapping
   - Configure restart policy for production
   - Wait for container initialization
4. **Testing & Validation**
   - Perform container health check
   - Test nginx proxy accessibility
   - Validate JavaScript asset delivery
   - Generate deployment summary

### 💬 Output Features

#### Color-Coded Messages

- 🔵 **Info**: General process information
- 🟢 **Success**: Successful operations
- 🟡 **Warning**: Non-critical issues requiring attention
- 🔴 **Error**: Critical failures requiring action

#### Deployment Summary

The script provides a comprehensive deployment summary including:

- App name and container details
- Port mappings and URLs
- Container status and health
- Useful management commands
- nginx configuration guidance

### 🌐 nginx Integration

When nginx configuration is needed, the script automatically generates the required configuration block:

```nginx
# Auto-generated nginx configuration
location /app-name {
 return 301 /app-name/;
}

location /app-name/ {
 proxy_pass http://127.0.0.1:PORT/;
 proxy_set_header Host $host;
 proxy_set_header X-Real-IP $remote_addr;
 proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
 proxy_set_header X-Forwarded-Proto $scheme;
 proxy_set_header X-Forwarded-Host $host;
 proxy_set_header X-Forwarded-Port $server_port;
 proxy_http_version 1.1;
 proxy_set_header Upgrade $http_upgrade;
 proxy_set_header Connection "upgrade";
 proxy_connect_timeout 30s;
 proxy_send_timeout 30s;
 proxy_read_timeout 30s;
}
```

### 🛡️ Error Handling & Recovery

#### Common Issues & Solutions

**Port Already in Use**

- Script detects port conflicts automatically
- Offers interactive rebuild for same-app conflicts
- Prevents accidental overwrites of different apps

**Missing Dependencies**

- Validates Dockerfile and package.json presence
- Provides helpful guidance for missing files
- References integration templates for setup

**Container Health Issues**

- Performs automatic health checks after deployment
- Provides debugging commands when issues occur
- Tests both direct container access and nginx proxy

### 🔧 Management Commands

The script provides useful commands for ongoing app management:

```bash
# View application logs
docker logs app-name

# Restart application
docker restart app-name

# Rebuild application
./deploy-portfolio-app.sh app-name port rebuild

# Access container shell
docker exec -it app-name sh

# Monitor all containers
docker ps | grep 300
```

### 📚 Best Practices

#### Port Assignment Strategy

- **Range**: Use ports 3008-3020 for portfolio apps
- **Documentation**: Keep a record of port assignments
- **Conflicts**: Always check for conflicts before deployment
- **Testing**: Test both direct and nginx access after deployment

#### Container Management

- **Naming**: Use consistent container names matching app names
- **Restart Policies**: Always use `unless-stopped` for production
- **Resource Limits**: Consider adding memory/CPU limits for production
- **Logs**: Regularly monitor container logs for issues

#### Deployment Safety

- **Testing**: Always test deployment in development first
- **Backups**: Consider backup strategies for persistent data
- **Rollback**: Keep previous images for quick rollback if needed
- **Monitoring**: Set up monitoring for production deployments

### 📍 Script Location & Access

**File Path:** `/var/www/zaylegend/deploy-portfolio-app.sh`

**Usage Instructions:**

1. Navigate to the zaylegend directory: `cd /var/www/zaylegend`
2. Make script executable: `chmod +x deploy-portfolio-app.sh`
3. Run deployment: `./deploy-portfolio-app.sh <app-name> <port> [rebuild]`

---

## 📄 Complete Script Source

Below is the complete source code of the portfolio deployment script:

```bash
#!/bin/bash
set -e

# Portfolio App Deployment Script
# Usage: ./deploy-portfolio-app.sh <app-name> <port> [rebuild]

APP_NAME="$1"
APP_PORT="$2"
REBUILD_FORCE="$3"

# Color codes for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Helper functions
log_info() { echo -e "${BLUE}ℹ️ $1${NC}"; }
log_success() { echo -e "${GREEN}✅ $1${NC}"; }
log_warning() { echo -e "${YELLOW}⚠️ $1${NC}"; }
log_error() { echo -e "${RED}❌ $1${NC}"; }

# Validation
if [[ -z "$APP_NAME" || -z "$APP_PORT" ]]; then
 log_error "Usage: $0 <app-name> <port> [rebuild]"
 echo ""
 echo "Examples:"
 echo " $0 fineline 3003 rebuild # Force rebuild fineline"
 echo " $0 new-app 3008 # Deploy new app"
 echo ""
 echo "Available ports: 3008-3020 (check with: docker ps | grep 300)"
 exit 1
fi

APP_DIR="/var/www/zaylegend/apps/${APP_NAME}"
BASE_PATH="/${APP_NAME}/"

# Check if app directory exists
if [[ ! -d "$APP_DIR" ]]; then
 log_error "App directory not found: $APP_DIR"
 log_info "Create the app directory and add your Vite project first"
 exit 1
fi

# Check if port is available
if docker ps | grep -q ":${APP_PORT}->"; then
 if [[ "$REBUILD_FORCE" != "rebuild" ]]; then
 log_warning "Port $APP_PORT is already in use"
 EXISTING_CONTAINER=$(docker ps --format "table {{.Names}}\t{{.Ports}}" | grep ":${APP_PORT}->" | awk '{print $1}')
 if [[ "$EXISTING_CONTAINER" == "$APP_NAME" ]]; then
 log_info "Existing container '$APP_NAME' found on port $APP_PORT"
 read -p "Do you want to rebuild it? (y/N): " -n 1 -r
 echo
 if [[ ! $REPLY =~ ^[Yy]$ ]]; then
 log_info "Deployment cancelled"
 exit 0
 fi
 REBUILD_FORCE="rebuild"
 else
 log_error "Port $APP_PORT is used by different container: $EXISTING_CONTAINER"
 exit 1
 fi
 fi
fi

log_info "Starting deployment of '$APP_NAME' on port $APP_PORT..."

# Step 1: Navigate to app directory
cd "$APP_DIR"
log_info "Working in: $(pwd)"

# Step 2: Check for required files
if [[ ! -f "Dockerfile" ]]; then
 log_error "Dockerfile not found in $APP_DIR"
 log_info "Create a Dockerfile using the template in APP-INTEGRATION-TEMPLATE.md"
 exit 1
fi

if [[ ! -f "package.json" ]]; then
 log_error "package.json not found - is this a Node.js app?"
 exit 1
fi

# Step 3: Stop and remove existing container if rebuilding
if [[ "$REBUILD_FORCE" == "rebuild" ]] || docker ps -a | grep -q "\\b${APP_NAME}\\b"; then
 log_info "Stopping existing container..."
 docker stop "$APP_NAME" 2>/dev/null || true
 docker rm "$APP_NAME" 2>/dev/null || true
 log_success "Existing container removed"
fi

# Step 4: Build new image
log_info "Building Docker image..."
docker build \
 --build-arg VITE_BASE_PATH="$BASE_PATH" \
 -t "${APP_NAME}:latest" \
 .

log_success "Docker image built successfully"

# Step 5: Start new container
log_info "Starting container on port $APP_PORT..."
docker run -d \
 --name "$APP_NAME" \
 -p "${APP_PORT}:80" \
 --restart unless-stopped \
 "${APP_NAME}:latest"

# Step 6: Wait for container to be ready
log_info "Waiting for container to start..."
sleep 3

# Step 7: Test container health
if curl -f -s "http://localhost:${APP_PORT}/" > /dev/null; then
 log_success "Container is healthy and responding"
else
 log_error "Container health check failed"
 log_info "Check logs with: docker logs $APP_NAME"
 exit 1
fi

# Step 8: Test through nginx (if nginx is configured)
NGINX_URL="https://zaylegend.com${BASE_PATH}"
if curl -f -s "$NGINX_URL" > /dev/null; then
 log_success "App accessible through nginx: $NGINX_URL"
else
 log_warning "App not accessible through nginx yet"
 log_info "You may need to add nginx configuration:"
 echo ""
 echo "Add this to /etc/nginx/conf.d/portfolio.conf:"
 echo ""
 echo " # $APP_NAME"
 echo " location /$APP_NAME {"
 echo " return 301 /$APP_NAME/;"
 echo " }"
 echo ""
 echo " location /$APP_NAME/ {"
 echo " proxy_pass http://127.0.0.1:$APP_PORT/;"
 echo " proxy_set_header Host \$host;"
 echo " proxy_set_header X-Real-IP \$remote_addr;"
 echo " proxy_set_header X-Forwarded-For \$proxy_add_x_forwarded_for;"
 echo " proxy_set_header X-Forwarded-Proto \$scheme;"
 echo " proxy_set_header X-Forwarded-Host \$host;"
 echo " proxy_set_header X-Forwarded-Port \$server_port;"
 echo " proxy_http_version 1.1;"
 echo " proxy_set_header Upgrade \$http_upgrade;"
 echo " proxy_set_header Connection \"upgrade\";"
 echo " proxy_connect_timeout 30s;"
 echo " proxy_send_timeout 30s;"
 echo " proxy_read_timeout 30s;"
 echo " }"
 echo ""
 echo "Then run: sudo nginx -t && sudo systemctl reload nginx"
fi

# Step 9: Show deployment summary
echo ""
log_success "🎉 Deployment completed successfully!"
echo ""
echo "📊 Deployment Summary:"
echo " App Name: $APP_NAME"
echo " Container Port: $APP_PORT"
echo " Base Path: $BASE_PATH"
echo " Container Status: $(docker inspect --format='{{.State.Status}}' $APP_NAME)"
echo " Direct Access: http://localhost:$APP_PORT/"
echo " Public URL: $NGINX_URL"
echo ""
echo "🔧 Useful Commands:"
echo " View logs: docker logs $APP_NAME"
echo " Restart: docker restart $APP_NAME"
echo " Rebuild: $0 $APP_NAME $APP_PORT rebuild"
echo " Shell access: docker exec -it $APP_NAME sh"
echo ""

# Step 10: Optional - Test JavaScript assets
log_info "Testing JavaScript assets..."
CONTAINER_HTML=$(curl -s "http://localhost:${APP_PORT}/")
JS_FILE=$(echo "$CONTAINER_HTML" | grep -o 'src="/[^"]*\.js"' | head -1 | sed 's/src="//; s/"//')

if [[ -n "$JS_FILE" ]]; then
 if curl -f -s "http://localhost:${APP_PORT}${JS_FILE}" | head -c 100 | grep -q "var\|function\|import\|export"; then
 log_success "JavaScript assets are serving correctly"
 else
 log_warning "JavaScript assets may not be serving correctly"
 fi
else
 log_warning "No JavaScript files detected in HTML"
fi

log_info "Deployment script completed! 🚀"
```

---

## 🔧 Additional Automation Tools

### Container Management Commands

Essential Docker commands for managing deployed applications:

```bash
# Monitor all portfolio containers
docker ps | grep -E "300[0-9]"

# View logs for specific app
docker logs -f app-name

# Restart all containers
docker restart $(docker ps -q)

# Clean up unused images
docker image prune -f

# Check container resource usage
docker stats
```

### nginx Management

Commands for managing nginx configuration and testing:

```bash
# Test nginx configuration
sudo nginx -t

# Reload nginx configuration
sudo systemctl reload nginx

# Check nginx status
sudo systemctl status nginx

# View nginx error logs
sudo tail -f /var/log/nginx/error.log

# Check proxy configuration
curl -I https://zaylegend.com/app-name/
```

### Monitoring & Health Checks

Scripts for monitoring application health and performance:

```bash
# Quick health check for all apps
for port in {3001..3020}; do
 if curl -f -s "http://localhost:$port/" > /dev/null; then
 echo "Port $port: ✅ Healthy"
 else
 echo "Port $port: ❌ Not responding"
 fi
done

# Check disk usage
df -h /var/www/zaylegend/

# Monitor system resources
htop
```

---

*These automation tools provide a robust foundation for managing containerized portfolio applications with Docker and nginx. The deployment script ensures consistent, reliable deployments while providing comprehensive feedback and error handling throughout the process.*
