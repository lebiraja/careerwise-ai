CareerWise AI
An intelligent career mentor AI that analyzes student resumes and GitHub profiles to provide personalized career guidance using Ollama LLM.
Setup

Clone the repository:
git clone https://github.com/your-repo/careerwise-ai.git
cd careerwise-ai


Install dependencies:
pip install -r requirements.txt


Install and start Ollama:
# Install Ollama (follow https://ollama.ai)
ollama pull mistral
ollama serve


Set environment variables in a .env file:
GITHUB_TOKEN=your_github_personal_access_token
EMAIL_ADDRESS=your_email@gmail.com
EMAIL_PASSWORD=your_app_specific_password


Run the app:
streamlit run app.py



Features

Resume Parsing: Extracts name, skills, and education from PDF resumes.
GitHub Analysis: Analyzes public repos, languages, stars, and activity.
Mentor Advice: Provides learning resources, job roles, and project ideas via Ollama LLM.
Weekly Email: Sends a summarized progress report.

Folder Structure

app.py: Main Streamlit application.
resume_parser.py: PDF resume parsing logic.
github_analyzer.py: GitHub API analysis.
mentor_brain.py: Ollama LLM recommendation logic.
emailer.py: Email sending module.
templates/report_template.html: HTML email template.
static/style.css: Custom CSS for Streamlit UI.
requirements.txt: Python dependencies.
README.md: Project documentation.

Notes

Ensure Ollama is running (ollama serve) with the mistral model pulled.
Email requires a Gmail app-specific password (generate in Google Account settings).
GitHub token enhances API rate limits (generate in GitHub > Settings > Developer settings).
Test with a sample PDF resume and a public GitHub username (e.g., octocat).

 