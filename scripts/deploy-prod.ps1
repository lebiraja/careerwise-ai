# Production Deployment Script for CareerWise AI
# PowerShell script for Windows - Uses Docker Hub image

Write-Host "🚀 Deploying CareerWise AI from Docker Hub..." -ForegroundColor Green

# Check if Docker is running
try {
    docker --version | Out-Null
    Write-Host "✅ Docker is installed and running" -ForegroundColor Green
}
catch {
    Write-Host "❌ Docker is not installed or not running. Please install Docker Desktop first." -ForegroundColor Red
    exit 1
}

# Check if docker-compose is available
try {
    docker-compose --version | Out-Null
    Write-Host "✅ Docker Compose is available" -ForegroundColor Green
}
catch {
    Write-Host "❌ Docker Compose is not available. Please install Docker Compose." -ForegroundColor Red
    exit 1
}

# Check if .env file exists
if (Test-Path ".env") {
    Write-Host "✅ .env file found" -ForegroundColor Green
} else {
    Write-Host "⚠️  .env file not found. Creating template..." -ForegroundColor Yellow
    @"
GITHUB_TOKEN=your_github_personal_access_token
EMAIL_ADDRESS=your_email@gmail.com
EMAIL_PASSWORD=your_app_specific_password
"@ | Out-File -FilePath ".env" -Encoding utf8
    Write-Host "📝 Please edit .env file with your credentials before continuing" -ForegroundColor Yellow
    exit 1
}

Write-Host "📥 Pulling latest images from Docker Hub..." -ForegroundColor Blue
docker-compose -f docker-compose.prod.yml pull

Write-Host "🔨 Starting services..." -ForegroundColor Blue
docker-compose -f docker-compose.prod.yml up -d

Write-Host "⏳ Waiting for services to start..." -ForegroundColor Blue
Start-Sleep -Seconds 10

# Pull Ollama model
Write-Host "📥 Pulling Ollama model (llama3.2:3b)..." -ForegroundColor Blue
docker exec ollama_service ollama pull llama3.2:3b

Write-Host "✅ Deployment complete!" -ForegroundColor Green
Write-Host "🌐 CareerWise AI is running at: http://localhost:8501" -ForegroundColor Cyan
Write-Host "🤖 Ollama API is running at: http://localhost:11434" -ForegroundColor Cyan

Write-Host "`n📋 Useful commands:" -ForegroundColor Yellow
Write-Host "  Stop services:    docker-compose -f docker-compose.prod.yml down" -ForegroundColor White
Write-Host "  View logs:        docker-compose -f docker-compose.prod.yml logs -f" -ForegroundColor White
Write-Host "  Restart:          docker-compose -f docker-compose.prod.yml restart" -ForegroundColor White
Write-Host "  Update:           docker-compose -f docker-compose.prod.yml pull && docker-compose -f docker-compose.prod.yml up -d" -ForegroundColor White
