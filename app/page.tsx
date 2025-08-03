'use client';

import { useState } from 'react';
import { motion } from 'framer-motion';
import { 
  Target, 
  Upload, 
  Github, 
  Mail, 
  Search, 
  BarChart3, 
  User, 
  GraduationCap, 
  Code, 
  Star,
  FileText,
  CheckCircle,
  AlertCircle,
  Info,
  Loader2
} from 'lucide-react';
import FileUpload from '@/components/FileUpload';
import AnalysisResults from '@/components/AnalysisResults';
import { AnalysisData, ResumeData, GitHubData } from '@/types';

export default function Home() {
  const [isAnalyzing, setIsAnalyzing] = useState(false);
  const [analysisData, setAnalysisData] = useState<AnalysisData | null>(null);
  const [error, setError] = useState<string | null>(null);
  const [success, setSuccess] = useState<string | null>(null);
  const [formData, setFormData] = useState({
    resumeFile: null as File | null,
    githubUsername: '',
    email: ''
  });

  const handleAnalyze = async () => {
    if (!formData.resumeFile || !formData.githubUsername) {
      setError('Please upload a resume and enter your GitHub username');
      return;
    }

    setIsAnalyzing(true);
    setError(null);
    setSuccess(null);

    try {
      // Create FormData for file upload
      const formDataToSend = new FormData();
      formDataToSend.append('githubUsername', formData.githubUsername);
      if (formData.email) {
        formDataToSend.append('email', formData.email);
      }
      if (formData.resumeFile) {
        formDataToSend.append('resumeFile', formData.resumeFile);
      }

      const response = await fetch('/api/analyze', {
        method: 'POST',
        body: formDataToSend,
      });

      if (!response.ok) {
        const errorData = await response.json();
        throw new Error(errorData.error || 'Analysis failed');
      }

      const data = await response.json();
      setAnalysisData(data);
      setSuccess('Analysis completed successfully!');
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Failed to analyze profile. Please try again.');
    } finally {
      setIsAnalyzing(false);
    }
  };

  const handleSendReport = async () => {
    if (!formData.email || !formData.githubUsername) {
      setError('Please enter both email and GitHub username');
      return;
    }

    setIsAnalyzing(true);
    setError(null);
    setSuccess(null);

    try {
      const response = await fetch('/api/send-report', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          email: formData.email,
          githubUsername: formData.githubUsername
        }),
      });

      if (!response.ok) {
        const errorData = await response.json();
        throw new Error(errorData.error || 'Failed to send report');
      }

      const data = await response.json();
      setSuccess(data.message || 'Weekly report sent successfully!');
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Failed to send weekly report. Please check your credentials.');
    } finally {
      setIsAnalyzing(false);
    }
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-gray-50 to-gray-100">
      {/* Header */}
      <header className="bg-white shadow-sm border-b border-gray-200">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex items-center justify-between h-16">
            <div className="flex items-center space-x-3">
              <Target className="h-8 w-8 text-primary-500" />
              <h1 className="text-2xl font-bold text-gray-900">CareerWise AI</h1>
            </div>
            <p className="text-gray-600">Your personalized career mentor</p>
          </div>
        </div>
      </header>

      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        <div className="grid grid-cols-1 lg:grid-cols-4 gap-8">
          {/* Sidebar */}
          <div className="lg:col-span-1">
            <motion.div 
              initial={{ opacity: 0, x: -20 }}
              animate={{ opacity: 1, x: 0 }}
              className="bg-white rounded-xl shadow-lg p-6 sticky top-8"
            >
              <h2 className="text-lg font-semibold text-gray-900 mb-6 flex items-center">
                <FileText className="h-5 w-5 mr-2 text-primary-500" />
                Profile Inputs
              </h2>

              {/* File Upload */}
              <div className="mb-6">
                <label className="block text-sm font-medium text-gray-700 mb-2">
                  📄 Upload Your Resume
                </label>
                <FileUpload
                  onFileSelect={(file) => setFormData(prev => ({ ...prev, resumeFile: file }))}
                  acceptedTypes={['.pdf']}
                />
              </div>

              {/* GitHub Username */}
              <div className="mb-6">
                <label className="block text-sm font-medium text-gray-700 mb-2">
                  🐙 GitHub Username
                </label>
                <input
                  type="text"
                  placeholder="e.g., octocat"
                  className="input-field"
                  value={formData.githubUsername}
                  onChange={(e) => setFormData(prev => ({ ...prev, githubUsername: e.target.value }))}
                />
              </div>

              {/* Email */}
              <div className="mb-6">
                <label className="block text-sm font-medium text-gray-700 mb-2">
                  📧 Email for Weekly Reports
                </label>
                <input
                  type="email"
                  placeholder="e.g., student@example.com"
                  className="input-field"
                  value={formData.email}
                  onChange={(e) => setFormData(prev => ({ ...prev, email: e.target.value }))}
                />
              </div>

              {/* Action Buttons */}
              <div className="space-y-3">
                <button
                  onClick={handleAnalyze}
                  disabled={isAnalyzing}
                  className="btn-primary w-full flex items-center justify-center"
                >
                  {isAnalyzing ? (
                    <Loader2 className="h-4 w-4 animate-spin mr-2" />
                  ) : (
                    <Search className="h-4 w-4 mr-2" />
                  )}
                  Analyze Profile
                </button>
                
                <button
                  onClick={handleSendReport}
                  disabled={isAnalyzing}
                  className="btn-secondary w-full flex items-center justify-center"
                >
                  {isAnalyzing ? (
                    <Loader2 className="h-4 w-4 animate-spin mr-2" />
                  ) : (
                    <BarChart3 className="h-4 w-4 mr-2" />
                  )}
                  Send Weekly Report
                </button>
              </div>

              {/* Error Message */}
              {error && (
                <motion.div
                  initial={{ opacity: 0, y: 10 }}
                  animate={{ opacity: 1, y: 0 }}
                  className="error-message mt-4"
                >
                  <AlertCircle className="h-4 w-4 inline mr-2" />
                  {error}
                </motion.div>
              )}

              {/* Success Message */}
              {success && (
                <motion.div
                  initial={{ opacity: 0, y: 10 }}
                  animate={{ opacity: 1, y: 0 }}
                  className="success-message mt-4"
                >
                  <CheckCircle className="h-4 w-4 inline mr-2" />
                  {success}
                </motion.div>
              )}
            </motion.div>
          </div>

          {/* Main Content */}
          <div className="lg:col-span-3">
            {!analysisData ? (
              <WelcomeSection />
            ) : (
              <AnalysisResults data={analysisData} />
            )}
          </div>
        </div>
      </div>
    </div>
  );
}

function WelcomeSection() {
  return (
    <motion.div
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      className="space-y-8"
    >
      {/* Hero Section */}
      <div className="text-center">
        <motion.div
          initial={{ scale: 0.8 }}
          animate={{ scale: 1 }}
          className="inline-flex items-center justify-center w-16 h-16 bg-primary-100 rounded-full mb-6"
        >
          <Target className="h-8 w-8 text-primary-500" />
        </motion.div>
        <h1 className="text-4xl font-bold text-gray-900 mb-4">
          Welcome to CareerWise AI!
        </h1>
        <p className="text-xl text-gray-600 max-w-2xl mx-auto">
          Your personalized career mentor for students. Get comprehensive analysis of your professional profile and receive tailored career recommendations.
        </p>
      </div>

      {/* Features Grid */}
      <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ delay: 0.1 }}
          className="card"
        >
          <div className="flex items-start space-x-4">
            <div className="flex-shrink-0">
              <Search className="h-6 w-6 text-primary-500" />
            </div>
            <div>
              <h3 className="text-lg font-semibold text-gray-900 mb-2">
                Profile Analysis
              </h3>
              <p className="text-gray-600">
                Upload your resume and GitHub username to get a comprehensive analysis of your professional profile.
              </p>
            </div>
          </div>
        </motion.div>

        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ delay: 0.2 }}
          className="card"
        >
          <div className="flex items-start space-x-4">
            <div className="flex-shrink-0">
              <Code className="h-6 w-6 text-primary-500" />
            </div>
            <div>
              <h3 className="text-lg font-semibold text-gray-900 mb-2">
                GitHub Insights
              </h3>
              <p className="text-gray-600">
                We'll analyze your repositories, coding languages, and project quality to understand your technical skills.
              </p>
            </div>
          </div>
        </motion.div>

        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ delay: 0.3 }}
          className="card"
        >
          <div className="flex items-start space-x-4">
            <div className="flex-shrink-0">
              <Target className="h-6 w-6 text-primary-500" />
            </div>
            <div>
              <h3 className="text-lg font-semibold text-gray-900 mb-2">
                Personalized Recommendations
              </h3>
              <p className="text-gray-600">
                Get tailored career advice based on your skills, experience, and career goals.
              </p>
            </div>
          </div>
        </motion.div>

        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ delay: 0.4 }}
          className="card"
        >
          <div className="flex items-start space-x-4">
            <div className="flex-shrink-0">
              <BarChart3 className="h-6 w-6 text-primary-500" />
            </div>
            <div>
              <h3 className="text-lg font-semibold text-gray-900 mb-2">
                Weekly Reports
              </h3>
              <p className="text-gray-600">
                Receive regular updates and insights to keep your career on track and stay motivated.
              </p>
            </div>
          </div>
        </motion.div>
      </div>

      {/* Tips Section */}
      <motion.div
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ delay: 0.5 }}
        className="bg-info-50 border border-info-100 rounded-xl p-6"
      >
        <div className="flex items-start space-x-3">
          <Info className="h-5 w-5 text-info-500 mt-0.5" />
          <div>
            <h3 className="text-lg font-semibold text-gray-900 mb-2">
              💡 Tips for Best Results
            </h3>
            <ul className="text-gray-600 space-y-1">
              <li>• Ensure your resume is in PDF format</li>
              <li>• Use your actual GitHub username</li>
              <li>• Make sure your GitHub profile is public</li>
              <li>• Include a valid email for weekly reports</li>
            </ul>
          </div>
        </div>
      </motion.div>
    </motion.div>
  );
} 