import { NextRequest, NextResponse } from 'next/server';

export async function POST(request: NextRequest) {
  try {
    // Handle FormData from frontend
    const formData = await request.formData();
    const githubUsername = formData.get('githubUsername') as string;
    const email = formData.get('email') as string;
    const resumeFile = formData.get('resumeFile') as File;

    if (!githubUsername) {
      return NextResponse.json(
        { error: 'GitHub username is required' },
        { status: 400 }
      );
    }

    // Prepare form data for backend
    const backendFormData = new FormData();
    backendFormData.append('github_username', githubUsername);
    if (email) {
      backendFormData.append('email', email);
    }
    
    // Add resume file if provided
    if (resumeFile && resumeFile.size > 0) {
      backendFormData.append('resume_file', resumeFile, resumeFile.name);
    }

    // Call Python backend
    const backendUrl = process.env.BACKEND_URL || 'http://localhost:8000';
    
    try {
      const response = await fetch(`${backendUrl}/api/analyze`, {
        method: 'POST',
        body: backendFormData,
      });

      if (!response.ok) {
        const errorText = await response.text();
        let errorMessage = 'Analysis failed';
        
        try {
          const errorData = JSON.parse(errorText);
          errorMessage = errorData.detail || errorData.error || errorMessage;
        } catch {
          errorMessage = errorText || errorMessage;
        }
        
        throw new Error(errorMessage);
      }

      const data = await response.json();
      return NextResponse.json(data);
    } catch (fetchError) {
      console.error('Backend connection error:', fetchError);
      throw new Error(
        fetchError instanceof Error 
          ? fetchError.message 
          : 'Backend server is not running. Please start the Python backend server.'
      );
    }
  } catch (error) {
    console.error('Analysis error:', error);
    return NextResponse.json(
      { 
        error: error instanceof Error 
          ? error.message 
          : 'Failed to analyze profile. Please ensure the backend server is running.' 
      },
      { status: 500 }
    );
  }
} 