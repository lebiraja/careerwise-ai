"""
Core modules for CareerWise AI
Contains the main business logic and processing modules.
"""

from .resume_parser import parse_resume
from .github_analyzer import analyze_github
from .mentor_brain import get_mentor_advice
from .emailer import send_email_report

__all__ = [
    'parse_resume',
    'analyze_github', 
    'get_mentor_advice',
    'send_email_report'
]
