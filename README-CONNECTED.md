# CareerWise AI - Connected System

A full-stack application with TypeScript frontend and Python backend for career mentoring and analysis.

## 🏗️ Architecture

### Frontend (TypeScript/Next.js)
- **Framework**: Next.js 14 with App Router
- **Language**: TypeScript for type safety
- **Styling**: Tailwind CSS with Streamlit color scheme
- **UI Components**: React with Framer Motion animations
- **File Upload**: Drag & drop with react-dropzone
- **API Integration**: RESTful communication with Python backend

### Backend (Python/FastAPI)
- **Framework**: FastAPI for high-performance API
- **Core Modules**: Resume parsing, GitHub analysis, AI mentoring
- **File Processing**: PDF resume parsing with pdfplumber
- **GitHub Integration**: Repository analysis with PyGithub
- **AI Integration**: Ollama LLM for career advice
- **Email Service**: Weekly report generation

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- Node.js 18+
- Git

### 1. Clone and Setup
```bash
git clone <repository-url>
cd career_mentor_ai
```

### 2. Install Dependencies

**Backend (Python):**
```bash
pip install -r requirements.txt
```

**Frontend (Node.js):**
```bash
npm install
```

### 3. Environment Configuration

Create `.env` file in the root directory:
```env
# GitHub API Token (required for GitHub analysis)
GITHUB_TOKEN=your_github_token_here

# Email Configuration (for weekly reports)
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USER=your_email@gmail.com
EMAIL_PASSWORD=your_app_password

# Backend URL (for frontend)
BACKEND_URL=http://localhost:8000
```

### 4. Start Development Servers

**Option 1: Automated Startup**
```bash
python start_dev.py
```

**Option 2: Manual Startup**

Terminal 1 (Backend):
```bash
python backend_api.py
```

Terminal 2 (Frontend):
```bash
npm run dev
```

### 5. Access the Application
- **Frontend**: http://localhost:3000
- **Backend API**: http://localhost:8000
- **API Documentation**: http://localhost:8000/docs

## 📁 Project Structure

```
career_mentor_ai/
├── app/                    # Next.js frontend
│   ├── api/               # Frontend API routes
│   ├── globals.css        # Global styles
│   ├── layout.tsx         # Root layout
│   └── page.tsx           # Main page
├── components/            # React components
├── types/                # TypeScript definitions
├── src/                  # Python backend modules
│   ├── core/             # Core analysis modules
│   │   ├── resume_parser.py
│   │   ├── github_analyzer.py
│   │   ├── mentor_brain.py
│   │   └── emailer.py
│   └── utils/            # Utility functions
├── backend_api.py        # FastAPI backend server
├── start_dev.py          # Development startup script
├── requirements.txt      # Python dependencies
├── package.json          # Node.js dependencies
└── README files
```

## 🔌 API Endpoints

### Analysis Endpoint
```http
POST /api/analyze
Content-Type: multipart/form-data

Parameters:
- github_username: string (required)
- email: string (optional)
- resume_file: file (optional, PDF)

Response:
{
  "resume": {
    "name": "string",
    "skills": ["string"],
    "education": "string",
    "warnings": ["string"]
  },
  "github": {
    "repo_count": number,
    "languages": ["string"],
    "total_stars": number,
    "readme_quality": "string"
  },
  "advice": "string"
}
```

### Report Endpoint
```http
POST /api/send-report
Content-Type: application/json

Body:
{
  "email": "string",
  "github_username": "string"
}

Response:
{
  "success": boolean,
  "message": "string"
}
```

## 🎯 Features

### Frontend Features
- **Modern UI/UX**: Professional design with smooth animations
- **File Upload**: Drag & drop PDF resume upload
- **Real-time Feedback**: Loading states and progress indicators
- **Responsive Design**: Works on all devices
- **Error Handling**: User-friendly error messages
- **Success Feedback**: Confirmation messages

### Backend Features
- **Resume Parsing**: Extract skills, education, and experience from PDFs
- **GitHub Analysis**: Repository analysis and language detection
- **AI Mentoring**: Ollama LLM for personalized career advice
- **Email Reports**: Weekly insights and recommendations
- **API Documentation**: Auto-generated with FastAPI
- **CORS Support**: Configured for frontend communication

## 🔧 Development

### Backend Development
```bash
# Install dependencies
pip install -r requirements.txt

# Run backend server
python backend_api.py

# Or with uvicorn directly
uvicorn backend_api:app --reload --host 0.0.0.0 --port 8000
```

### Frontend Development
```bash
# Install dependencies
npm install

# Development server
npm run dev

# Build for production
npm run build

# Type checking
npm run type-check
```

### API Testing
```bash
# Test backend health
curl http://localhost:8000/api/health

# Test analysis endpoint
curl -X POST http://localhost:8000/api/analyze \
  -F "github_username=octocat" \
  -F "email=test@example.com"
```

## 🚀 Deployment

### Backend Deployment
```bash
# Production with uvicorn
uvicorn backend_api:app --host 0.0.0.0 --port 8000

# With Docker
docker build -t careerwise-backend .
docker run -p 8000:8000 careerwise-backend
```

### Frontend Deployment
```bash
# Build for production
npm run build

# Deploy to Vercel
vercel --prod

# Or deploy to other platforms
npm run export  # Static export
```

## 🔧 Configuration

### Environment Variables

**Backend (.env):**
```env
GITHUB_TOKEN=your_github_token
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USER=your_email@gmail.com
EMAIL_PASSWORD=your_app_password
```

**Frontend (.env.local):**
```env
BACKEND_URL=http://localhost:8000
NEXT_PUBLIC_API_URL=http://localhost:8000
```

### GitHub Token Setup
1. Go to GitHub Settings > Developer settings > Personal access tokens
2. Generate a new token with `public_repo` scope
3. Add to your `.env` file

### Email Configuration
1. Enable 2-factor authentication on your Gmail
2. Generate an app password
3. Add email credentials to `.env` file

## 🐛 Troubleshooting

### Common Issues

**Backend Issues:**
- **GitHub API errors**: Check your `GITHUB_TOKEN` in `.env`
- **Ollama errors**: Ensure Ollama is running locally
- **Email errors**: Verify email credentials in `.env`

**Frontend Issues:**
- **API connection errors**: Check `BACKEND_URL` in `.env.local`
- **Build errors**: Run `npm install` and clear cache
- **Type errors**: Run `npm run type-check`

**General Issues:**
- **Port conflicts**: Change ports in startup scripts
- **CORS errors**: Check CORS configuration in `backend_api.py`
- **File upload errors**: Ensure PDF files are valid

### Debug Mode
```bash
# Backend with debug logging
uvicorn backend_api:app --reload --log-level debug

# Frontend with debug info
npm run dev -- --debug
```

## 📊 Monitoring

### Health Checks
- **Backend**: http://localhost:8000/api/health
- **Frontend**: Built-in Next.js health checks

### API Documentation
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test both frontend and backend
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License.

---

**Built with ❤️ using Next.js, React, TypeScript, FastAPI, and Python** 