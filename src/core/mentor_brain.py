from typing import Dict, Any
import ollama

def get_mentor_advice(resume_data: Dict[str, Any], github_data: Dict[str, Any]) -> str:
    """
    Generate career advice using Ollama LLM based on resume and GitHub data.
    Returns a markdown-formatted string with recommendations.
    """
    try:
        # Prepare prompt
        prompt = f"""
You are a friendly and smart career counselor. Given the following resume and GitHub summary for a student, provide:

- A list of 3 recommended learning resources (e.g., courses, books, tutorials).
- 2 potential internships or job roles they should apply for.
- 2 innovative project ideas to improve their portfolio.

**Resume Data:**
- Name: {resume_data.get('name', 'N/A')}
- Skills: {', '.join(resume_data.get('skills', [])) or 'None'}
- Education: {resume_data.get('education', 'N/A')}
- Languages: {', '.join(resume_data.get('languages', [])) or 'None'}

**GitHub Data:**
- Repositories: {github_data.get('repo_count', 0)}
- Languages: {', '.join(github_data.get('languages', [])) or 'None'}
- Total Stars: {github_data.get('total_stars', 0)}
- Commit Frequency: {github_data.get('commit_frequency', 0):.2f} commits/repo
- README Quality: {github_data.get('readme_quality', 'N/A')}

Provide the response in markdown format with clear headings and bullet points.
"""

        # Use Ollama LLM
        response = ollama.generate(model="llama3.2:3b", prompt=prompt)
        advice = response.get("response", "")

        # Ensure response is in markdown
        if not advice.strip():
            raise Exception("Empty response from Ollama")

        return advice

    except Exception as e:
        # Fallback response if Ollama fails
        return f"""
## Career Recommendations

### Learning Resources
- **Coursera: Python for Everybody** - Strengthen Python skills.
- **freeCodeCamp: JavaScript Algorithms** - Improve JS and problem-solving.
- **Book: 'Clean Code' by Robert C. Martin** - Learn coding best practices.

### Potential Roles
- **Software Engineering Intern** - Apply to tech startups or mid-size firms.
- **Data Analyst Intern** - Leverage Python and SQL skills.

### Project Ideas
- **Personal Finance Tracker** - Build a web app using Flask and SQLite.
- **GitHub Stats Dashboard** - Create a React app to visualize repo activity.

**Note**: Failed to connect to Ollama: {str(e)}. Please ensure Ollama is running.
"""