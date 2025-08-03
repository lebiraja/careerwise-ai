# 🔧 Troubleshooting Guide

## Common Issues and Solutions

### 1. Frontend-Backend Connection Issues

**Problem**: `SyntaxError: No number after minus sign in JSON at position 1`

**Solution**: 
- Ensure the backend is running: `python -m uvicorn backend_api:app --host 0.0.0.0 --port 8000 --reload`
- Check if port 8000 is available: `netstat -an | findstr :8000`
- Test backend health: `curl http://localhost:8000/api/health`

### 2. Next.js Configuration Warnings

**Problem**: `Unrecognized key(s) in object: 'appDir' at "experimental"`

**Solution**: 
- The `appDir` option is deprecated in Next.js 14
- This has been fixed in the updated `next.config.js`

### 3. Backend Not Starting

**Problem**: Backend server fails to start

**Solutions**:
```bash
# Check Python dependencies
pip install -r requirements.txt

# Check if uvicorn is installed
pip install uvicorn fastapi

# Start backend manually
python -m uvicorn backend_api:app --host 0.0.0.0 --port 8000 --reload
```

### 4. Frontend Not Starting

**Problem**: Frontend server fails to start

**Solutions**:
```bash
# Check Node.js dependencies
npm install

# Clear Next.js cache
rm -rf .next
npm run dev
```

### 5. Port Conflicts

**Problem**: Port 8000 or 3000 is already in use

**Solutions**:
```bash
# Check what's using the ports
netstat -an | findstr :8000
netstat -an | findstr :3000

# Kill processes using the ports (Windows)
netstat -ano | findstr :8000
taskkill /PID <PID> /F
```

### 6. Environment Variables

**Problem**: Backend can't find environment variables

**Solution**: Create `.env` file in root directory:
```env
GITHUB_TOKEN=your_github_token_here
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USER=your_email@gmail.com
EMAIL_PASSWORD=your_app_password
```

### 7. CORS Issues

**Problem**: Frontend can't connect to backend due to CORS

**Solution**: The backend is configured with CORS for localhost:3000. If you're using a different port, update the CORS configuration in `backend_api.py`.

### 8. File Upload Issues

**Problem**: Resume file upload fails

**Solutions**:
- Ensure file is PDF format
- Check file size (should be under 10MB)
- Verify backend is running and accessible

### 9. GitHub API Issues

**Problem**: GitHub analysis fails

**Solutions**:
- Check your `GITHUB_TOKEN` in `.env`
- Ensure token has `public_repo` scope
- Verify GitHub username is correct and profile is public

### 10. Ollama Issues

**Problem**: AI mentoring fails

**Solutions**:
- Install Ollama: https://ollama.ai/
- Start Ollama service
- Pull the model: `ollama pull llama3.2:3b`

## Quick Fix Commands

### Start Both Services
```bash
# Option 1: Use the batch script (Windows)
start_development.bat

# Option 2: Manual startup
# Terminal 1 - Backend
python -m uvicorn backend_api:app --host 0.0.0.0 --port 8000 --reload

# Terminal 2 - Frontend
npm run dev
```

### Test Backend
```bash
# Health check
curl http://localhost:8000/api/health

# Test analysis endpoint
curl -X POST http://localhost:8000/api/analyze -F "github_username=octocat"
```

### Reset Everything
```bash
# Stop all processes
taskkill /F /IM python.exe
taskkill /F /IM node.exe

# Clear caches
rm -rf .next
rm -rf node_modules/.cache

# Reinstall dependencies
pip install -r requirements.txt
npm install

# Start fresh
start_development.bat
```

## Debug Mode

### Backend Debug
```bash
python -m uvicorn backend_api:app --host 0.0.0.0 --port 8000 --reload --log-level debug
```

### Frontend Debug
```bash
npm run dev -- --debug
```

## Environment Setup Checklist

- [ ] Python 3.8+ installed
- [ ] Node.js 18+ installed
- [ ] Dependencies installed: `pip install -r requirements.txt && npm install`
- [ ] `.env` file created with GitHub token
- [ ] Ollama installed and running (for AI features)
- [ ] Ports 8000 and 3000 available

## Still Having Issues?

1. **Check logs**: Look at both frontend and backend console output
2. **Test endpoints**: Use curl or Postman to test API endpoints directly
3. **Verify network**: Ensure no firewall is blocking localhost connections
4. **Check versions**: Ensure you're using compatible versions of all dependencies

## Support

If you're still experiencing issues:
1. Check the console output for specific error messages
2. Verify all dependencies are installed correctly
3. Ensure both services are running on the correct ports
4. Test the backend API directly using curl or a REST client 