# CareerWise AI

Your personalized career mentor for students. A comprehensive application that analyzes resumes, GitHub profiles, and provides tailored career recommendations.

## 🚀 Quick Start

### Frontend (TypeScript/Next.js)

The application now features a modern TypeScript frontend built with Next.js and Tailwind CSS.

```bash
# Install dependencies
npm install

# Start development server
npm run dev

# Open http://localhost:3000
```

### Backend (Python)

The Python backend provides the core analysis functionality.

```bash
# Install Python dependencies
pip install -r requirements.txt

# Run the backend server
python main.py
```

## 🏗️ Architecture

### Frontend (TypeScript/Next.js)
- **Framework**: Next.js 14 with App Router
- **Language**: TypeScript for type safety
- **Styling**: Tailwind CSS with custom Streamlit color scheme
- **UI Components**: React with Framer Motion animations
- **File Upload**: Drag & drop with react-dropzone
- **State Management**: React hooks and context

### Backend (Python)
- **Core Analysis**: Resume parsing, GitHub analysis, mentor advice
- **Email Service**: Weekly report generation and sending
- **API**: RESTful endpoints for frontend communication

## 📁 Project Structure

```
career_mentor_ai/
├── app/                    # Next.js frontend
│   ├── api/               # API routes
│   ├── globals.css        # Global styles
│   ├── layout.tsx         # Root layout
│   └── page.tsx           # Main page
├── components/            # React components
├── types/                # TypeScript definitions
├── src/                  # Python backend
│   ├── core/             # Core analysis modules
│   ├── utils/            # Utility functions
│   └── ui/               # (Legacy Streamlit UI)
├── static/               # Static assets
├── templates/            # Email templates
├── docker/               # Docker configuration
└── scripts/              # Deployment scripts
```

## 🎨 Features

### Frontend Features
- **Modern UI/UX**: Professional design with smooth animations
- **Responsive Design**: Works on all devices
- **Drag & Drop**: Professional file upload experience
- **Real-time Feedback**: Loading states and progress indicators
- **Type Safety**: Full TypeScript implementation
- **Streamlit Theme**: Maintains original color scheme

### Backend Features
- **Resume Parsing**: Extract skills, education, and experience
- **GitHub Analysis**: Repository analysis and language detection
- **Career Recommendations**: AI-powered career advice
- **Email Reports**: Weekly insights and recommendations
- **Error Handling**: Comprehensive error management

## 🔧 Development

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

# Linting
npm run lint
```

### Backend Development

```bash
# Install Python dependencies
pip install -r requirements.txt

# Run backend server
python main.py

# Run with Docker
docker-compose up
```

## 🎯 Key Components

### Frontend Components
- **FileUpload**: Drag & drop file upload with validation
- **AnalysisResults**: Professional results display
- **WelcomeSection**: Feature highlights and tips
- **API Routes**: Backend communication endpoints

### Backend Modules
- **resume_parser.py**: PDF resume analysis
- **github_analyzer.py**: GitHub profile analysis
- **mentor_brain.py**: AI career recommendations
- **emailer.py**: Email report generation

## 🚀 Deployment

### Frontend Deployment
- **Vercel**: Recommended for Next.js
- **Netlify**: Static site deployment
- **Docker**: Containerized deployment

### Backend Deployment
- **Docker**: Containerized with docker-compose
- **Cloud Platforms**: AWS, GCP, Azure
- **VPS**: Traditional server deployment

## 🔌 API Integration

The frontend communicates with the backend via RESTful APIs:

### Analysis Endpoint
```typescript
POST /api/analyze
{
  "githubUsername": "string",
  "email": "string"
}
```

### Report Endpoint
```typescript
POST /api/send-report
{
  "email": "string",
  "githubUsername": "string"
}
```

## 🎨 Design System

### Color Palette
- **Primary**: `#1f77b4` (Streamlit Blue)
- **Success**: `#28a745` (Green)
- **Error**: `#dc3545` (Red)
- **Warning**: `#ffc107` (Yellow)
- **Info**: `#17a2b8` (Cyan)

### Typography
- **Font**: Inter (Google Fonts)
- **Weights**: 300, 400, 500, 600, 700

## 📱 Responsive Design

The application is fully responsive:
- **Mobile**: < 768px
- **Tablet**: 768px - 1024px
- **Desktop**: > 1024px

## 🔧 Configuration

### Environment Variables

Create `.env.local` for frontend:
```env
NEXT_PUBLIC_API_URL=http://localhost:8000
```

### Backend Configuration

Update `src/utils/config.py` for backend settings.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License.

---

**Built with ❤️ using Next.js, React, TypeScript, Python, and Tailwind CSS**
