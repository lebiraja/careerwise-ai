#!/usr/bin/env python3
"""
CareerWise AI - FastAPI Backend
Provides REST API endpoints for the TypeScript frontend
"""

from fastapi import FastAPI, HTTPException, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import Optional, Dict, Any
import tempfile
import os
import sys
from pathlib import Path

# Add src to path for imports
src_path = Path(__file__).parent / "src"
sys.path.insert(0, str(src_path))

from core.resume_parser import parse_resume
from core.github_analyzer import analyze_github
from core.mentor_brain import get_mentor_advice
from core.emailer import send_email_report

# Load environment variables
from dotenv import load_dotenv
load_dotenv()

app = FastAPI(
    title="CareerWise AI API",
    description="Backend API for CareerWise AI - Career mentoring application",
    version="1.0.0"
)

# Configure CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Pydantic models for request/response
class AnalysisRequest(BaseModel):
    github_username: str
    email: Optional[str] = None

class ReportRequest(BaseModel):
    email: str
    github_username: str

class AnalysisResponse(BaseModel):
    resume: Dict[str, Any]
    github: Dict[str, Any]
    advice: str

class ReportResponse(BaseModel):
    success: bool
    message: str

@app.get("/")
async def root():
    """Health check endpoint"""
    return {"message": "CareerWise AI API is running!", "version": "1.0.0"}

@app.post("/api/analyze", response_model=AnalysisResponse)
async def analyze_profile(
    github_username: str = Form(...),
    email: Optional[str] = Form(None),
    resume_file: Optional[UploadFile] = File(None)
):
    """
    Analyze a user's profile using resume and GitHub data
    """
    try:
        # Validate inputs
        if not github_username:
            raise HTTPException(status_code=400, detail="GitHub username is required")
        
        # Initialize response data
        resume_data = {
            "name": "Sample User",
            "skills": ["Python", "JavaScript", "React", "Node.js"],
            "education": "Bachelor's in Computer Science",
            "warnings": []
        }
        
        # Parse resume if provided
        if resume_file:
            try:
                # Save uploaded file temporarily
                with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
                    content = await resume_file.read()
                    tmp_file.write(content)
                    tmp_file_path = tmp_file.name
                
                # Parse resume
                parsed_resume = parse_resume(tmp_file_path)
                
                # Clean up temp file
                os.unlink(tmp_file_path)
                
                if "error" not in parsed_resume:
                    resume_data = parsed_resume
                else:
                    resume_data["warnings"].append(parsed_resume["error"])
                    
            except Exception as e:
                resume_data["warnings"].append(f"Failed to parse resume: {str(e)}")
        
        # Analyze GitHub profile
        github_data = analyze_github(github_username)
        
        if "error" in github_data:
            raise HTTPException(status_code=400, detail=github_data["error"])
        
        # Generate mentor advice
        advice = get_mentor_advice(resume_data, github_data)
        
        return AnalysisResponse(
            resume=resume_data,
            github=github_data,
            advice=advice
        )
        
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Analysis failed: {str(e)}")

@app.post("/api/send-report", response_model=ReportResponse)
async def send_weekly_report(request: ReportRequest):
    """
    Send a weekly career report via email
    """
    try:
        # Validate inputs
        if not request.email or not request.github_username:
            raise HTTPException(
                status_code=400, 
                detail="Email and GitHub username are required"
            )
        
        # Analyze GitHub for report
        github_data = analyze_github(request.github_username)
        
        if "error" in github_data:
            raise HTTPException(status_code=400, detail=github_data["error"])
        
        # Send email report
        success = send_email_report(request.email, github_data)
        
        if success:
            return ReportResponse(
                success=True,
                message="Weekly report sent successfully!"
            )
        else:
            raise HTTPException(
                status_code=500,
                detail="Failed to send email. Check your email configuration."
            )
            
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=500, 
            detail=f"Failed to send report: {str(e)}"
        )

@app.get("/api/health")
async def health_check():
    """Health check for the API"""
    return {
        "status": "healthy",
        "version": "1.0.0",
        "services": {
            "resume_parser": "available",
            "github_analyzer": "available",
            "mentor_brain": "available",
            "emailer": "available"
        }
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "backend_api:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    ) 