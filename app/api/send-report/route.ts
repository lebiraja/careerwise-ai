import { NextRequest, NextResponse } from 'next/server';

export async function POST(request: NextRequest) {
  try {
    const body = await request.json();
    const { email, githubUsername } = body;

    if (!email || !githubUsername) {
      return NextResponse.json(
        { error: 'Email and GitHub username are required' },
        { status: 400 }
      );
    }

    // Call Python backend
    const backendUrl = process.env.BACKEND_URL || 'http://localhost:8000';
    
    try {
      const response = await fetch(`${backendUrl}/api/send-report`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          email: email,
          github_username: githubUsername
        }),
      });

      if (!response.ok) {
        const errorText = await response.text();
        let errorMessage = 'Failed to send report';
        
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
    console.error('Send report error:', error);
    return NextResponse.json(
      { 
        error: error instanceof Error 
          ? error.message 
          : 'Failed to send weekly report. Please ensure the backend server is running.' 
      },
      { status: 500 }
    );
  }
} 