'use client';

import { motion } from 'framer-motion';
import { 
  User, 
  GraduationCap, 
  Code, 
  Star, 
  FileText, 
  Github, 
  Target,
  CheckCircle,
  AlertTriangle,
  TrendingUp
} from 'lucide-react';
import { AnalysisResultsProps } from '@/types';

export default function AnalysisResults({ data }: AnalysisResultsProps) {
  const { resume, github, advice } = data;

  return (
    <motion.div
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      className="space-y-8"
    >
      {/* Resume Analysis */}
      <motion.div
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ delay: 0.1 }}
        className="card"
      >
        <div className="flex items-center space-x-3 mb-6">
          <FileText className="h-6 w-6 text-primary-500" />
          <h2 className="text-2xl font-bold text-gray-900">📄 Resume Analysis</h2>
        </div>

        {resume.error ? (
          <div className="error-message">
            <AlertTriangle className="h-5 w-5 inline mr-2" />
            {resume.error}
          </div>
        ) : (
          <div className="space-y-6">
            {/* Personal Information */}
            <div>
              <h3 className="text-lg font-semibold text-gray-900 mb-4 flex items-center">
                <User className="h-5 w-5 mr-2 text-primary-500" />
                Personal Information
              </h3>
              <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                <div className="bg-gray-50 rounded-lg p-4">
                  <div className="flex items-center space-x-2 mb-2">
                    <User className="h-4 w-4 text-gray-500" />
                    <span className="text-sm font-medium text-gray-600">Name</span>
                  </div>
                  <p className="text-lg font-semibold text-gray-900">{resume.name}</p>
                </div>
                <div className="bg-gray-50 rounded-lg p-4">
                  <div className="flex items-center space-x-2 mb-2">
                    <GraduationCap className="h-4 w-4 text-gray-500" />
                    <span className="text-sm font-medium text-gray-600">Education</span>
                  </div>
                  <p className="text-lg font-semibold text-gray-900">{resume.education}</p>
                </div>
              </div>
            </div>

            {/* Skills */}
            <div>
              <h3 className="text-lg font-semibold text-gray-900 mb-4 flex items-center">
                <Code className="h-5 w-5 mr-2 text-primary-500" />
                Skills
              </h3>
              {resume.skills.length > 0 ? (
                <div className="flex flex-wrap gap-2">
                  {resume.skills.map((skill, index) => (
                    <motion.span
                      key={index}
                      initial={{ opacity: 0, scale: 0.8 }}
                      animate={{ opacity: 1, scale: 1 }}
                      transition={{ delay: index * 0.1 }}
                      className="bg-primary-100 text-primary-700 px-3 py-1 rounded-full text-sm font-medium"
                    >
                      {skill}
                    </motion.span>
                  ))}
                </div>
              ) : (
                <p className="text-gray-500 italic">No skills detected</p>
              )}
            </div>

            {/* Warnings */}
            {resume.warnings && resume.warnings.length > 0 && (
              <div>
                <h3 className="text-lg font-semibold text-gray-900 mb-4 flex items-center">
                  <AlertTriangle className="h-5 w-5 mr-2 text-warning-500" />
                  Resume Warnings
                </h3>
                <div className="space-y-2">
                  {resume.warnings.map((warning, index) => (
                    <div key={index} className="warning-message">
                      <AlertTriangle className="h-4 w-4 inline mr-2" />
                      {warning}
                    </div>
                  ))}
                </div>
              </div>
            )}
          </div>
        )}
      </motion.div>

      {/* GitHub Analysis */}
      <motion.div
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ delay: 0.2 }}
        className="card"
      >
        <div className="flex items-center space-x-3 mb-6">
          <Github className="h-6 w-6 text-primary-500" />
          <h2 className="text-2xl font-bold text-gray-900">🐙 GitHub Analysis</h2>
        </div>

        {github.error ? (
          <div className="error-message">
            <AlertTriangle className="h-5 w-5 inline mr-2" />
            {github.error}
          </div>
        ) : (
          <div className="space-y-6">
            {/* Metrics */}
            <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
              <div className="bg-gray-50 rounded-lg p-4 text-center">
                <div className="flex items-center justify-center mb-2">
                  <Code className="h-6 w-6 text-primary-500" />
                </div>
                <p className="text-2xl font-bold text-gray-900">{github.repo_count}</p>
                <p className="text-sm text-gray-600">Repositories</p>
              </div>
              <div className="bg-gray-50 rounded-lg p-4 text-center">
                <div className="flex items-center justify-center mb-2">
                  <Star className="h-6 w-6 text-primary-500" />
                </div>
                <p className="text-2xl font-bold text-gray-900">{github.total_stars}</p>
                <p className="text-sm text-gray-600">Total Stars</p>
              </div>
              <div className="bg-gray-50 rounded-lg p-4 text-center">
                <div className="flex items-center justify-center mb-2">
                  <TrendingUp className="h-6 w-6 text-primary-500" />
                </div>
                <p className="text-2xl font-bold text-gray-900">{github.readme_quality}</p>
                <p className="text-sm text-gray-600">README Quality</p>
              </div>
            </div>

            {/* Languages */}
            {github.languages.length > 0 && (
              <div>
                <h3 className="text-lg font-semibold text-gray-900 mb-4 flex items-center">
                  <Code className="h-5 w-5 mr-2 text-primary-500" />
                  Programming Languages
                </h3>
                <div className="grid grid-cols-2 md:grid-cols-4 gap-3">
                  {github.languages.map((language, index) => (
                    <motion.div
                      key={index}
                      initial={{ opacity: 0, y: 10 }}
                      animate={{ opacity: 1, y: 0 }}
                      transition={{ delay: index * 0.1 }}
                      className="bg-primary-50 border border-primary-200 rounded-lg p-3 text-center"
                    >
                      <p className="font-medium text-primary-700">{language}</p>
                    </motion.div>
                  ))}
                </div>
              </div>
            )}
          </div>
        )}
      </motion.div>

      {/* Career Recommendations */}
      <motion.div
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ delay: 0.3 }}
        className="card"
      >
        <div className="flex items-center space-x-3 mb-6">
          <Target className="h-6 w-6 text-primary-500" />
          <h2 className="text-2xl font-bold text-gray-900">🎯 Career Recommendations</h2>
        </div>
        
        <div className="prose prose-gray max-w-none">
          <div className="bg-primary-50 border border-primary-200 rounded-lg p-6">
            <div className="flex items-start space-x-3">
              <CheckCircle className="h-5 w-5 text-primary-500 mt-1 flex-shrink-0" />
              <div className="text-gray-700 leading-relaxed">
                {advice.split('\n').map((paragraph, index) => (
                  <p key={index} className="mb-4 last:mb-0">
                    {paragraph}
                  </p>
                ))}
              </div>
            </div>
          </div>
        </div>
      </motion.div>
    </motion.div>
  );
} 