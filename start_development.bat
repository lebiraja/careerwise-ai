@echo off
echo 🎯 CareerWise AI - Development Startup
echo ======================================

echo.
echo 📋 Starting services...
echo 1. Backend API (FastAPI) - http://localhost:8000
echo 2. Frontend (Next.js) - http://localhost:3000
echo.

echo 🚀 Starting Backend Server...
start "Backend Server" cmd /k "python -m uvicorn backend_api:app --host 0.0.0.0 --port 8000 --reload"

echo ⏳ Waiting for backend to start...
timeout /t 3 /nobreak > nul

echo 🌐 Starting Frontend Server...
start "Frontend Server" cmd /k "npm run dev"

echo.
echo ✅ Both servers are starting...
echo.
echo 📍 Access Points:
echo    Frontend: http://localhost:3000
echo    Backend API: http://localhost:8000
echo    API Docs: http://localhost:8000/docs
echo.
echo 💡 Press any key to close this window...
pause > nul 