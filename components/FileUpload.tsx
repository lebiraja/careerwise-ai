'use client';

import { useState, useCallback } from 'react';
import { useDropzone } from 'react-dropzone';
import { motion } from 'framer-motion';
import { Upload, FileText, X } from 'lucide-react';
import { FileUploadProps } from '@/types';

export default function FileUpload({ onFileSelect, acceptedTypes }: FileUploadProps) {
  const [selectedFile, setSelectedFile] = useState<File | null>(null);

  const onDrop = useCallback((acceptedFiles: File[]) => {
    const file = acceptedFiles[0];
    if (file) {
      setSelectedFile(file);
      onFileSelect(file);
    }
  }, [onFileSelect]);

  const { getRootProps, getInputProps, isDragActive } = useDropzone({
    onDrop,
    accept: {
      'application/pdf': acceptedTypes.includes('.pdf') ? ['.pdf'] : [],
    },
    multiple: false,
  });

  const { onClick, onKeyDown, onFocus, onBlur, onDragEnter, onDragLeave, onDragOver, onDrop: onDropHandler, ...rootProps } = getRootProps();

  const removeFile = () => {
    setSelectedFile(null);
    onFileSelect(null as any);
  };

  return (
    <div className="space-y-3">
      {!selectedFile ? (
        <motion.div
          onClick={onClick}
          onKeyDown={onKeyDown}
          onFocus={onFocus}
          onBlur={onBlur}
          onDragEnter={onDragEnter}
          onDragLeave={onDragLeave}
          onDragOver={onDragOver}
          onDrop={onDropHandler}
          tabIndex={rootProps.tabIndex}
          role={rootProps.role}
          className={`border-2 border-dashed rounded-lg p-6 text-center cursor-pointer transition-colors duration-200 ${
            isDragActive
              ? 'border-primary-500 bg-primary-50'
              : 'border-gray-300 hover:border-primary-400 hover:bg-gray-50'
          }`}
          whileHover={{ scale: 1.02 }}
          whileTap={{ scale: 0.98 }}
        >
          <input {...getInputProps()} />
          <Upload className="h-8 w-8 text-gray-400 mx-auto mb-3" />
          {isDragActive ? (
            <p className="text-primary-600 font-medium">Drop the file here...</p>
          ) : (
            <div>
              <p className="text-gray-600 font-medium mb-1">
                Click to upload or drag and drop
              </p>
              <p className="text-sm text-gray-500">
                PDF files only
              </p>
            </div>
          )}
        </motion.div>
      ) : (
        <motion.div
          initial={{ opacity: 0, y: 10 }}
          animate={{ opacity: 1, y: 0 }}
          className="bg-green-50 border border-green-200 rounded-lg p-4"
        >
          <div className="flex items-center justify-between">
            <div className="flex items-center space-x-3">
              <FileText className="h-5 w-5 text-green-600" />
              <div>
                <p className="text-sm font-medium text-green-800">
                  {selectedFile.name}
                </p>
                <p className="text-xs text-green-600">
                  {(selectedFile.size / 1024 / 1024).toFixed(2)} MB
                </p>
              </div>
            </div>
            <button
              onClick={removeFile}
              className="text-green-600 hover:text-green-800 transition-colors"
            >
              <X className="h-4 w-4" />
            </button>
          </div>
        </motion.div>
      )}
    </div>
  );
} 