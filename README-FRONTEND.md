# CareerWise AI - TypeScript Frontend

A modern, professional TypeScript frontend for the CareerWise AI application, built with Next.js, React, and Tailwind CSS.

## 🎨 Features

- **Modern UI/UX**: Professional design with smooth animations and transitions
- **TypeScript**: Full type safety and better development experience
- **Responsive Design**: Works perfectly on desktop, tablet, and mobile
- **Streamlit Color Scheme**: Maintains the original Streamlit color palette
- **Drag & Drop**: Professional file upload with drag and drop functionality
- **Real-time Feedback**: Loading states, progress indicators, and error handling
- **Component-based**: Modular, reusable components

## 🚀 Quick Start

### Prerequisites

- Node.js 18+ 
- npm or yarn

### Installation

1. **Install dependencies:**
   ```bash
   npm install
   ```

2. **Start development server:**
   ```bash
   npm run dev
   ```

3. **Open your browser:**
   Navigate to [http://localhost:3000](http://localhost:3000)

## 📁 Project Structure

```
app/
├── api/                    # API routes
│   ├── analyze/           # Profile analysis endpoint
│   └── send-report/       # Weekly report endpoint
├── globals.css            # Global styles and Tailwind
├── layout.tsx             # Root layout component
└── page.tsx               # Main page component

components/
├── AnalysisResults.tsx    # Results display component
└── FileUpload.tsx         # File upload component

types/
└── index.ts              # TypeScript type definitions
```

## 🎯 Key Components

### Main Page (`app/page.tsx`)
- Welcome section with feature highlights
- Sidebar with form inputs
- File upload with drag & drop
- Analysis results display

### File Upload (`components/FileUpload.tsx`)
- Drag and drop functionality
- File type validation
- Visual feedback for uploads
- File removal capability

### Analysis Results (`components/AnalysisResults.tsx`)
- Resume analysis display
- GitHub profile insights
- Career recommendations
- Professional metrics cards

## 🎨 Design System

### Color Palette (Streamlit Theme)
- **Primary**: `#1f77b4` (Streamlit Blue)
- **Success**: `#28a745` (Green)
- **Error**: `#dc3545` (Red)
- **Warning**: `#ffc107` (Yellow)
- **Info**: `#17a2b8` (Cyan)

### Typography
- **Font**: Inter (Google Fonts)
- **Weights**: 300, 400, 500, 600, 700

### Components
- **Cards**: Rounded corners, subtle shadows
- **Buttons**: Hover effects, loading states
- **Inputs**: Focus states, validation styling
- **Messages**: Color-coded success/error/info states

## 🔧 Development

### Available Scripts

```bash
# Development
npm run dev          # Start development server
npm run build        # Build for production
npm run start        # Start production server
npm run lint         # Run ESLint
npm run type-check   # Run TypeScript type checking
```

### Environment Variables

Create a `.env.local` file for environment variables:

```env
NEXT_PUBLIC_API_URL=http://localhost:8000
```

## 🔌 API Integration

The frontend is designed to work with your Python backend. Update the API routes in `app/api/` to connect to your actual backend endpoints:

### Analysis Endpoint
- **Route**: `/api/analyze`
- **Method**: POST
- **Body**: `{ githubUsername, email }`
- **Response**: `{ resume, github, advice }`

### Report Endpoint
- **Route**: `/api/send-report`
- **Method**: POST
- **Body**: `{ email, githubUsername }`
- **Response**: `{ success, message }`

## 🎨 Customization

### Styling
- Modify `tailwind.config.js` for theme changes
- Update `app/globals.css` for custom styles
- Component-specific styles in each component file

### Components
- All components are modular and reusable
- Props are fully typed with TypeScript
- Easy to extend and customize

## 📱 Responsive Design

The application is fully responsive with breakpoints:
- **Mobile**: < 768px
- **Tablet**: 768px - 1024px
- **Desktop**: > 1024px

## 🚀 Deployment

### Vercel (Recommended)
1. Connect your GitHub repository
2. Vercel will auto-detect Next.js
3. Deploy with one click

### Other Platforms
- **Netlify**: Use `npm run build` and deploy `out/` directory
- **AWS Amplify**: Connect repository and auto-deploy
- **Docker**: Use the provided Dockerfile

## 🔗 Backend Integration

To connect with your Python backend:

1. **Update API routes** in `app/api/` to call your backend
2. **Configure CORS** in your Python backend
3. **Set environment variables** for API endpoints
4. **Test integration** with real data

## 📄 License

This project is part of the CareerWise AI application.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

---

**Built with ❤️ using Next.js, React, TypeScript, and Tailwind CSS** 