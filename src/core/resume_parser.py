import pdfplumber
import re
from typing import Dict, List

def parse_resume(pdf_path: str) -> Dict[str, any]:
    """
    Parse a PDF resume to extract name, skills, education, and other details using pdfplumber.
    Returns a dictionary with extracted data.
    """
    try:
        text = ""
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                text += page.extract_text() or ""

        resume_data = {
            "name": "",
            "skills": [],
            "education": "",
            "projects": [],
            "languages": [],
            "certifications": []
        }

        lines = text.split("\n")
        resume_data["name"] = lines[0].strip() if lines else "Unknown"

        skill_keywords = [
            "python", "java", "javascript", "sql", "machine learning", "flask",
            "django", "react", "node.js", "git", "docker", "aws", "tensorflow"
        ]
        skills_section = re.search(r"skills.*?(?:\n|$)(.*?)(?:\n\n|$)", text, re.I | re.S)
        if skills_section:
            skills_text = skills_section.group(1).lower()
            resume_data["skills"] = [
                skill for skill in skill_keywords if skill in skills_text
            ]

        education_pattern = re.search(
            r"(bachelor|master|ph\.?d|B\.?Sc|M\.?Sc).*?(?:\n|$)(.*?)(?:\n\n|$)",
            text, re.I | re.S
        )
        if education_pattern:
            resume_data["education"] = education_pattern.group(0).strip()

        language_keywords = ["python", "java", "javascript", "c++", "sql"]
        resume_data["languages"] = [
            lang for lang in language_keywords if lang in resume_data["skills"]
        ]

        if not resume_data["skills"]:
            resume_data["warnings"] = ["No skills section detected. Consider adding one."]

        return resume_data

    except Exception as e:
        return {"error": f"Failed to parse resume: {str(e)}"}