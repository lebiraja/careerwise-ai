export interface ResumeData {
  name: string;
  skills: string[];
  education: string;
  warnings?: string[];
  error?: string;
}

export interface GitHubData {
  repo_count: number;
  languages: string[];
  total_stars: number;
  readme_quality: string;
  error?: string;
}

export interface AnalysisData {
  resume: ResumeData;
  github: GitHubData;
  advice: string;
}

export interface FileUploadProps {
  onFileSelect: (file: File) => void;
  acceptedTypes: string[];
}

export interface AnalysisResultsProps {
  data: AnalysisData;
} 