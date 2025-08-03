# CareerWise AI

**CareerWise AI** is an intelligent career mentoring tool designed to analyze student resumes and GitHub profiles, providing personalized career guidance using the advanced Ollama LLM. It helps students gain insights into their strengths and areas for improvement, making informed decisions about their career paths.

## 🎯 Project Overview

CareerWise AI bridges the gap between academic learning and industry requirements by providing data-driven career insights. The application combines resume analysis, GitHub profile evaluation, and AI-powered recommendations to help students:

- **Identify skill gaps** in their current profile
- **Discover relevant learning resources** tailored to their background
- **Explore suitable job roles** based on their skills and interests
- **Receive actionable project ideas** to enhance their portfolio
- **Track progress** through automated weekly reports

### 🏗️ System Architecture

The application follows a modular architecture with clear separation of concerns:

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Streamlit UI  │    │  Resume Parser  │    │ GitHub Analyzer │
│                 │────┤                 │    │                 │
│  - File Upload  │    │  - PDF Extract  │    │  - API Calls    │
│  - User Input   │    │  - Text Parse   │    │  - Repo Analysis│
│  - Results View │    │  - Skill Extract│    │  - Lang Detection│
└─────────────────┘    └─────────────────┘    └─────────────────┘
         │                        │                        │
         └────────────────────────┼────────────────────────┘
                                  │
                   ┌─────────────────┐    ┌─────────────────┐
                   │  Mentor Brain   │    │     Emailer     │
                   │                 │    │                 │
                   │  - Ollama LLM   │    │  - SMTP Client  │
                   │  - Prompt Eng   │    │  - HTML Reports │
                   │  - Response Gen │    │  - Schedule Send│
                   └─────────────────┘    └─────────────────┘
```

### 🔄 Application Workflow

The application follows a comprehensive analysis workflow:

1. **Data Collection Phase**
   - User uploads PDF resume
   - User provides GitHub username
   - System validates inputs

2. **Analysis Phase**
   - Resume parsing extracts structured data
   - GitHub API fetches repository information
   - Data validation and error handling

3. **Intelligence Phase**
   - Ollama LLM processes combined data
   - Generates personalized recommendations
   - Formats output for presentation

4. **Delivery Phase**
   - Real-time results displayed in UI
   - Optional email report generation
   - Progress tracking and analytics

---

## Installation and Setup

### Clone the Repository

```bash
git clone https://github.com/your-repo/careerwise-ai.git
cd careerwise-ai
```

### Install Dependencies

Ensure you have Python installed, then run:

```bash
pip install -r requirements.txt
```

### Environment Configuration

Create a `.env` file by copying `.env.example`:

```
GITHUB_TOKEN=your_github_personal_access_token
EMAIL_ADDRESS=your_email@gmail.com
EMAIL_PASSWORD=your_app_specific_password
```

### Docker Setup

#### Docker Compose
Ensure Docker is installed, then start services using:

```bash
docker-compose up --build
```

For production, use:

```bash
docker-compose -f docker-compose.prod.yml up --build
```

---

## Usage Instructions

### Run the Application

#### Option 1: Using the main entry point (Recommended)
```bash
python main.py
```

#### Option 2: Using Streamlit directly
```bash
streamlit run src/ui/streamlit_app.py
```

#### Option 3: Using Docker
```bash
cd docker/
docker-compose up --build
```

Visit `http://localhost:8501` in your browser to access the interface.

### Features Overview

- **Resume Parsing:** Extracts key details such as name, skills, and education from PDF resumes.
- **GitHub Analysis:** Analyzes repositories, languages used, star ratings, and contribution frequency.
- **Mentor Advice:** Offers learning resources, job role suggestions, and project ideas using Ollama LLM.
- **Weekly Email Report:** Sends a summary report of progress via email.

---

## Project Structure

```
career_mentor_ai/
├── src/                           # Source code directory
│   ├── __init__.py               # Package initialization
│   ├── core/                     # Core business logic
│   │   ├── __init__.py          # Core package initialization
│   │   ├── resume_parser.py     # PDF resume parsing logic
│   │   ├── github_analyzer.py   # GitHub API analysis
│   │   ├── mentor_brain.py      # Ollama LLM recommendation engine
│   │   └── emailer.py           # Email report functionality
│   ├── ui/                      # User interface components
│   │   ├── __init__.py          # UI package initialization
│   │   └── streamlit_app.py     # Main Streamlit application
│   └── utils/                   # Utility modules
│       ├── __init__.py          # Utils package initialization
│       └── config.py            # Configuration management
├── static/                      # Static assets
│   └── css/
│       └── style.css           # Application styling
├── templates/                   # Template files
│   └── email/
│       └── report_template.html # HTML email template
├── scripts/                     # Deployment and setup scripts
│   ├── docker-setup.ps1        # Windows Docker setup
│   ├── docker-setup.sh         # Unix Docker setup
│   └── deploy-prod.ps1          # Production deployment
├── docker/                      # Docker configuration
│   ├── Dockerfile              # Container definition
│   ├── docker-compose.yml      # Development composition
│   └── docker-compose.prod.yml # Production composition
├── config/                      # Configuration files
│   └── .env.example           # Environment variables template
├── docs/                        # Documentation
│   └── README.md               # Project documentation
├── main.py                      # Application entry point
├── requirements.txt             # Python dependencies
├── .gitignore                  # Git ignore rules
└── .dockerignore               # Docker ignore rules
```

### Module Descriptions

#### Core Modules (`src/core/`)
- **`resume_parser.py`**: Extracts structured data from PDF resumes using pdfplumber
- **`github_analyzer.py`**: Analyzes GitHub profiles via API to gather repository metrics
- **`mentor_brain.py`**: Generates personalized career advice using Ollama LLM
- **`emailer.py`**: Sends formatted email reports with career insights

#### UI Modules (`src/ui/`)
- **`streamlit_app.py`**: Main web application interface with file uploads and results display

#### Utility Modules (`src/utils/`)
- **`config.py`**: Centralized configuration management and environment variable handling

---

## Configuration and Environment Variables

### .env Settings

- **GITHUB_TOKEN:** Personal access token for GitHub API requests.
- **EMAIL_ADDRESS:** Email address used to send reports.
- **EMAIL_PASSWORD:** App-specific password generated in Gmail settings.

---

## Docker and Deployment

### Dockerfile

- **Base Image:** Uses Python 3.12-slim.
- **Health Checks:** Ensures the application is running correctly.
- **Environment Variables:** Includes Streamlit server configuration.

### Docker Compose

- **Service Definitions:** Includes application and necessary services like Ollama.
- **Volume Management:** Uses Docker volumes for data persistence.

---

## Contributing Guidelines

We welcome contributions! Please fork the repository and create a pull request. Ensure all new features are covered by tests.

---

## License

This project is licensed under the MIT License. See the LICENSE file for details.

---

## Credits

Special thanks to the contributors and open-source libraries utilized in this project.

---
 