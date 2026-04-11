# Development Workflows

Complete guides for application integration, CI/CD deployment, and portfolio management workflows based on production implementations.

## App Integration Guide

A comprehensive checklist and automation for adding new React/Vite applications to the zaylegend.com portfolio infrastructure.

### Quick Start

```bash
./scripts/add-new-app.sh <app-name> <port> <github-url> [app-title] [description]
```

### Manual Integration Checklist

If you need to add an app manually, follow this checklist:

#### 1. Repository Setup ✅

- [ ] Clone app to `/var/www/zaylegend/apps/`
- [ ] Ensure app has `package.json` with build script
- [ ] Test local build: `npm run build`

#### 2. React Router Configuration ✅

**Critical: This prevents 404 errors!**

In `src/App.tsx` or `src/App.jsx`:

```tsx
// ❌ Wrong (causes 404s)
<BrowserRouter>

// ✅ Correct
<BrowserRouter basename="/app-name">
```

#### 3. Vite Configuration ✅

In `vite.config.ts`:

```typescript
export default defineConfig({
 base: process.env.VITE_BASE_PATH || '/app-name/',
 // ... other config
});
```

#### 4. Docker Configuration ✅

Create `Dockerfile` with proper build args:

```dockerfile
# Build args for base path configuration
ARG VITE_BASE_PATH=/app-name/
ENV VITE_BASE_PATH=${VITE_BASE_PATH}
```

### Port Management

**Assigned Ports:**

- 8080: Portfolio main site
- 8081: zen-reset
- 3002: chord-genesis
- 3003: fineline
- 3004: game-hub
- 3005: dj-visualizer
- 3006: spritegen
- **Available: 3007, 3008, 3009...**

### Common Issues & Solutions

**Issue: 404 "User attempted to access non-existent route"**  
**Cause:** Missing `basename` in BrowserRouter  
**Fix:** Add `basename="/app-name"` to BrowserRouter

**Issue: Assets return 404**  
**Cause:** Missing base path in vite.config  
**Fix:** Add `base: '/app-name/'` to vite.config

**Issue: Docker build uses wrong paths**  
**Cause:** Missing VITE\_BASE\_PATH build arg  
**Fix:** Use `--build-arg VITE_BASE_PATH=/app-name/`

[View Complete App Integration Guide →  (opens new window)](https://github.com/yetog/portfolio/blob/main/APP_INTEGRATION_GUIDE.md)

---

## CI/CD Deployment Pipeline

Automated deployment workflows using GitHub Actions for zero-downtime deployments.

### Current Status ✅

Your portfolio has **WORKING CI/CD pipelines** that automatically deploy when you push to GitHub:

#### **Active Workflows:**

1. **Portfolio Deployment** (`deploy-portfolio.yml`) - Deploys main portfolio
2. **App Deployment** (`deploy-apps.yml`) - Deploys individual apps (fixed version)
3. **Enhanced App Deployment** (`deploy-new-apps.yml`) - New improved version

### How It Works 🔄

**Automatic Deployment Triggers:**

```bash
# Portfolio updates
git push origin main # Auto-deploys portfolio if portfolio files changed

# App updates 
git push origin main # Auto-deploys any apps with changes in apps/ directory
```

**Manual Deployment:**

```bash
# Via GitHub Actions web interface:
# 1. Go to your repo → Actions tab
# 2. Select "Deploy New Apps (Enhanced)"
# 3. Click "Run workflow"
# 4. Choose specific app or force deploy all
```

### What Happens When You Push 📤

**Portfolio Changes:**

1. GitHub detects push to main branch
2. Builds portfolio with `npm run build`
3. SSHs to your server (66.179.240.58)
4. Pulls latest code
5. Rebuilds portfolio
6. Reloads nginx
7. ✅ Live at [https://zaylegend.com  (opens new window)](https://zaylegend.com)

**App Changes:**

1. GitHub detects changes in `apps/` folder
2. Identifies which specific apps changed
3. For each changed app:
   - **Fixes React Router** (adds basename automatically!)
   - Builds app with correct base path
   - Creates optimized Docker image
   - Stops old container
   - Starts new container
   - Tests deployment
   - ✅ Live at [https://zaylegend.com/app-name/  (opens new window)](https://zaylegend.com/app-name/)

### Deployment Features 🎯

- **Automatic Router Fixes**: Detects React apps and adds `basename="/app-name"` to BrowserRouter
- **Docker Optimization**: Builds with correct `VITE_BASE_PATH`
- **Error Handling**: Creates backups before deployment
- **Zero Downtime**: Apps stay running during updates
- **Health Monitoring**: Tests apps after deployment

[View Complete CI/CD Guide →  (opens new window)](https://github.com/yetog/portfolio/blob/main/CI_CD_DEPLOYMENT_GUIDE.md)

---

## Conversational AI Setup

Modern ElevenLabs integration using the official `@elevenlabs/client` SDK for real-time voice conversations.

### Architecture Overview

```text
Frontend (Conversation SDK)
 ↓
 GET /api/signed-url (Backend)
 ↓
 ElevenLabs Conversational AI (Direct WebSocket)
```

### Key Features

- ✅ **One-click conversation start** - No complex setup required
- ✅ **Real-time mode detection** - Visual indicators when agent is speaking vs listening
- ✅ **Automatic microphone handling** - SDK manages all audio I/O
- ✅ **Error handling** - Graceful error messages and recovery
- ✅ **Secure authentication** - Uses signed URLs instead of exposing API keys

### Backend Setup

Environment Variables:

```env
ELEVEN_LABS_API_KEY=your_api_key_here
ELEVEN_LABS_AGENT_ID=your_agent_id_here
```

Endpoints:

- `GET /api/signed-url` - Get a signed URL for authentication
- `GET /api/agent-id` - Get the agent ID for public agents

### Frontend Implementation

```javascript
import { Conversation } from '@elevenlabs/client';

conversation = await Conversation.startSession({
 signedUrl: signedUrl, // Get from /api/signed-url
 onConnect: () => {},
 onDisconnect: () => {},
 onModeChange: (mode) => {}, // 'speaking' or 'listening'
 onError: (error) => {},
 onMessage: (message) => {}
});
```

### Benefits Over Previous Implementation

1. **Less Code**: ~200 lines vs 1000+ lines
2. **More Reliable**: Official SDK maintained by ElevenLabs
3. **Better UX**: Faster connection, lower latency
4. **Easier Maintenance**: No custom WebSocket/audio handling
5. **Future-proof**: Automatic updates to new features

[View Complete Conversational AI Guide →  (opens new window)](https://github.com/yetog/portfolio/blob/main/apps/voice-assistant/CONVERSATIONAL_AI_GUIDE.md)

---

## Best Practices

### Performance

- Use `npm run build` for production builds
- Enable gzip in nginx (already configured)
- Optimize images and assets
- Consider lazy loading for large apps

### Security

- Never commit secrets to repositories
- Use environment variables for API keys
- Keep dependencies updated
- Use HTTPS only (already configured)

### Monitoring

- Check `docker logs <app-name>` for errors
- Monitor nginx logs: `tail -f /var/log/nginx/access.log`
- Use `docker ps` to check container status

## Resources

- [Complete App Integration Guide  (opens new window)](https://github.com/yetog/portfolio/blob/main/APP_INTEGRATION_GUIDE.md)
- [Complete CI/CD Deployment Guide  (opens new window)](https://github.com/yetog/portfolio/blob/main/CI_CD_DEPLOYMENT_GUIDE.md)
- [Complete Conversational AI Guide  (opens new window)](https://github.com/yetog/portfolio/blob/main/apps/voice-assistant/CONVERSATIONAL_AI_GUIDE.md)
- [GitHub Actions Documentation  (opens new window)](https://docs.github.com/en/actions)
- [Docker Best Practices  (opens new window)](https://docs.docker.com/develop/dev-best-practices/)

---

*Last Updated: October 11, 2025*  
*Based on production implementations in the zaylegend.com portfolio*
