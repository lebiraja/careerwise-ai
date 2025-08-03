# CareerWise AI

🚀 **Streamlit Application** - An intelligent career mentoring tool that analyzes student resumes and GitHub profiles to provide personalized career guidance using Ollama LLM.

## Quick Start

1. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Configure Environment**
   ```bash
   cp config/.env.example .env
   # Edit .env with your credentials
   ```

3. **Run Application**
   ```bash
   python main.py
   ```

4. **Access Application**
   Open `http://localhost:8501` in your browser

## Documentation

For detailed documentation, installation guides, and project structure, see:
📚 [**Full Documentation**](docs/README.md)

## Project Structure

```
📁 src/           # Source code (core logic, UI, utilities)
📁 docker/        # Docker configuration files
📁 scripts/       # Setup and deployment scripts
📁 config/        # Configuration files
📁 docs/          # Detailed documentation
```

## Features

- 📄 **Resume Analysis** - Extract skills, education, and experience from PDFs
- 🐙 **GitHub Integration** - Analyze repositories and coding activity
- 🤖 **AI Mentoring** - Get personalized career advice using Ollama LLM
- 📧 **Progress Reports** - Receive weekly email summaries

## Docker Deployment

```bash
# Development
cd docker/
docker-compose up --build

# Production
docker-compose -f docker-compose.prod.yml up --build
```

## Support

For questions or issues, please check the [documentation](docs/README.md) or open an issue.
