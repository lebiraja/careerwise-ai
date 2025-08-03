#!/bin/bash
# Docker Setup Script for CareerWise AI
# Bash script for Linux/macOS

echo "🚀 Setting up CareerWise AI with Docker..."

# Check if Docker is running
if ! command -v docker &> /dev/null; then
    echo "❌ Docker is not installed. Please install Docker first."
    exit 1
fi

if ! docker info &> /dev/null; then
    echo "❌ Docker is not running. Please start Docker first."
    exit 1
fi

echo "✅ Docker is installed and running"

# Check if docker-compose is available
if ! command -v docker-compose &> /dev/null; then
    echo "❌ Docker Compose is not available. Please install Docker Compose."
    exit 1
fi

echo "✅ Docker Compose is available"

# Check if .env file exists
if [ -f ".env" ]; then
    echo "✅ .env file found"
else
    echo "⚠️  .env file not found. Creating template..."
    cat > .env << EOF
GITHUB_TOKEN=your_github_personal_access_token
EMAIL_ADDRESS=your_email@gmail.com
EMAIL_PASSWORD=your_app_specific_password
EOF
    echo "📝 Please edit .env file with your credentials before continuing"
    exit 1
fi

echo "🔨 Building and starting containers..."
docker-compose up --build -d

echo "⏳ Waiting for services to start..."
sleep 10

# Pull Ollama model
echo "📥 Pulling Ollama model (llama3.2:3b)..."
docker exec ollama_service ollama pull llama3.2:3b

echo "✅ Setup complete!"
echo "🌐 CareerWise AI is running at: http://localhost:8501"
echo "🤖 Ollama API is running at: http://localhost:11434"

echo ""
echo "📋 Useful commands:"
echo "  Stop services:    docker-compose down"
echo "  View logs:        docker-compose logs -f"
echo "  Restart:          docker-compose restart"
