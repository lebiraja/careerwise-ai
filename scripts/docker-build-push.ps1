#!/usr/bin/env pwsh
<#
.SYNOPSIS
    Build and push CareerWise AI Docker image to DockerHub

.DESCRIPTION
    This script builds the Docker image for CareerWise AI and pushes it to DockerHub.
    It handles tagging, versioning, and provides comprehensive error handling.

.PARAMETER Tag
    The tag for the Docker image (default: latest)

.PARAMETER Push
    Whether to push to DockerHub after building (default: true)

.EXAMPLE
    .\docker-build-push.ps1
    .\docker-build-push.ps1 -Tag "v1.0.0"
    .\docker-build-push.ps1 -Tag "dev" -Push $false
#>

param(
    [string]$Tag = "latest",
    [bool]$Push = $true
)

# Configuration
$IMAGE_NAME = "lebiraja/careerwise-ai"
$DOCKERFILE_PATH = "docker/Dockerfile"
$BUILD_CONTEXT = "."

Write-Host "🐳 CareerWise AI Docker Build & Push Script" -ForegroundColor Cyan
Write-Host "=" * 50

# Check if Docker is running
Write-Host "🔍 Checking Docker status..." -ForegroundColor Yellow
try {
    docker version | Out-Null
    Write-Host "✅ Docker is running" -ForegroundColor Green
} catch {
    Write-Host "❌ Docker is not running. Please start Docker Desktop first." -ForegroundColor Red
    exit 1
}

# Check if we're logged into DockerHub
Write-Host "🔐 Checking DockerHub authentication..." -ForegroundColor Yellow
$dockerInfo = docker info 2>&1 | Select-String "Username"
if ($dockerInfo) {
    Write-Host "✅ Logged into DockerHub" -ForegroundColor Green
} else {
    Write-Host "⚠️  Not logged into DockerHub. Please run 'docker login' first." -ForegroundColor Yellow
    $loginChoice = Read-Host "Do you want to login now? (y/n)"
    if ($loginChoice -eq "y" -or $loginChoice -eq "Y") {
        docker login
        if ($LASTEXITCODE -ne 0) {
            Write-Host "❌ Failed to login to DockerHub" -ForegroundColor Red
            exit 1
        }
    } else {
        Write-Host "❌ DockerHub login required for pushing images" -ForegroundColor Red
        exit 1
    }
}

# Build the Docker image
Write-Host "🏗️  Building Docker image..." -ForegroundColor Yellow
Write-Host "   Image: $IMAGE_NAME:$Tag" -ForegroundColor Cyan
Write-Host "   Context: $BUILD_CONTEXT" -ForegroundColor Cyan
Write-Host "   Dockerfile: $DOCKERFILE_PATH" -ForegroundColor Cyan

$buildCommand = "docker build -t ${IMAGE_NAME}:${Tag} -f $DOCKERFILE_PATH $BUILD_CONTEXT"
Write-Host "   Command: $buildCommand" -ForegroundColor Gray

Invoke-Expression $buildCommand

if ($LASTEXITCODE -ne 0) {
    Write-Host "❌ Docker build failed!" -ForegroundColor Red
    exit 1
}

Write-Host "✅ Docker image built successfully!" -ForegroundColor Green

# Tag as latest if not already
if ($Tag -ne "latest") {
    Write-Host "🏷️  Tagging image as latest..." -ForegroundColor Yellow
    docker tag "${IMAGE_NAME}:${Tag}" "${IMAGE_NAME}:latest"
    if ($LASTEXITCODE -ne 0) {
        Write-Host "⚠️  Failed to tag as latest" -ForegroundColor Yellow
    } else {
        Write-Host "✅ Tagged as latest" -ForegroundColor Green
    }
}

# Push to DockerHub
if ($Push) {
    Write-Host "🚀 Pushing to DockerHub..." -ForegroundColor Yellow
    
    # Push the specific tag
    Write-Host "   Pushing ${IMAGE_NAME}:${Tag}..." -ForegroundColor Cyan
    docker push "${IMAGE_NAME}:${Tag}"
    if ($LASTEXITCODE -ne 0) {
        Write-Host "❌ Failed to push ${IMAGE_NAME}:${Tag}" -ForegroundColor Red
        exit 1
    }
    
    # Push latest if we tagged it
    if ($Tag -ne "latest") {
        Write-Host "   Pushing ${IMAGE_NAME}:latest..." -ForegroundColor Cyan
        docker push "${IMAGE_NAME}:latest"
        if ($LASTEXITCODE -ne 0) {
            Write-Host "⚠️  Failed to push latest tag" -ForegroundColor Yellow
        }
    }
    
    Write-Host "✅ Successfully pushed to DockerHub!" -ForegroundColor Green
} else {
    Write-Host "⏭️  Skipping push to DockerHub (as requested)" -ForegroundColor Yellow
}

# Show final image info
Write-Host "📋 Final Image Information:" -ForegroundColor Cyan
docker images | Select-String $IMAGE_NAME

Write-Host "`n🎉 Build and push completed successfully!" -ForegroundColor Green
Write-Host "🔗 DockerHub: https://hub.docker.com/r/$($IMAGE_NAME.Replace('/', '/r/'))" -ForegroundColor Cyan
Write-Host "🚀 Run with: docker run -p 8501:8501 ${IMAGE_NAME}:${Tag}" -ForegroundColor Cyan
