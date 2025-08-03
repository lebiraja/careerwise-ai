#!/usr/bin/env python3
"""
Development startup script for CareerWise AI
Runs both the FastAPI backend and provides instructions for the frontend
"""

import subprocess
import sys
import time
import os
from pathlib import Path

def check_dependencies():
    """Check if required dependencies are installed"""
    try:
        import fastapi
        import uvicorn
        print("✅ FastAPI dependencies found")
    except ImportError:
        print("❌ FastAPI not found. Installing dependencies...")
        subprocess.run([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
    
    # Check if Node.js is available
    try:
        subprocess.run(["npm", "--version"], capture_output=True, check=True)
        print("✅ Node.js/npm found")
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("❌ Node.js/npm not found. Please install Node.js to run the frontend.")
        return False
    
    return True

def start_backend():
    """Start the FastAPI backend server"""
    print("🚀 Starting FastAPI backend server...")
    try:
        subprocess.run([
            sys.executable, "-m", "uvicorn", 
            "backend_api:app",
            "--host", "0.0.0.0",
            "--port", "8000",
            "--reload"
        ])
    except KeyboardInterrupt:
        print("\n👋 Backend server stopped")

def main():
    """Main startup function"""
    print("🎯 CareerWise AI - Development Startup")
    print("=" * 50)
    
    # Check dependencies
    if not check_dependencies():
        sys.exit(1)
    
    print("\n📋 Starting services...")
    print("1. Backend API (FastAPI) - http://localhost:8000")
    print("2. Frontend (Next.js) - http://localhost:3000")
    print("\n💡 To start the frontend, run: npm run dev")
    print("💡 To view API docs, visit: http://localhost:8000/docs")
    
    # Start backend
    start_backend()

if __name__ == "__main__":
    main() 