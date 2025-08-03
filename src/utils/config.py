"""
Configuration utilities for CareerWise AI
"""

import os
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class Config:
    """Configuration class for CareerWise AI"""
    
    # Project paths
    PROJECT_ROOT = Path(__file__).parent.parent.parent
    TEMPLATES_DIR = PROJECT_ROOT / "templates"
    STATIC_DIR = PROJECT_ROOT / "static"
    
    # Environment variables
    GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
    EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
    EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
    
    # Application settings
    STREAMLIT_PORT = 8501
    OLLAMA_MODEL = "llama3.2:3b"
    
    # Email settings
    SMTP_SERVER = "smtp.gmail.com"
    SMTP_PORT = 587
    
    @classmethod
    def validate_config(cls):
        """Validate required configuration"""
        missing = []
        
        if not cls.GITHUB_TOKEN:
            missing.append("GITHUB_TOKEN")
        if not cls.EMAIL_ADDRESS:
            missing.append("EMAIL_ADDRESS")
        if not cls.EMAIL_PASSWORD:
            missing.append("EMAIL_PASSWORD")
            
        if missing:
            raise ValueError(f"Missing required environment variables: {', '.join(missing)}")
        
        return True
