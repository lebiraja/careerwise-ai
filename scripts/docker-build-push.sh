#!/bin/bash
set -e

# Configuration
IMAGE_NAME="lebiraja/careerwise-ai"
DOCKERFILE_PATH="docker/Dockerfile"
BUILD_CONTEXT="."
TAG="${1:-latest}"
PUSH="${2:-true}"

echo "🐳 CareerWise AI Docker Build & Push Script"
echo "=================================================="

# Check if Docker is running
echo "🔍 Checking Docker status..."
if ! docker version > /dev/null 2>&1; then
    echo "❌ Docker is not running. Please start Docker first."
    exit 1
fi
echo "✅ Docker is running"

# Check if we're logged into DockerHub
echo "🔐 Checking DockerHub authentication..."
if ! docker info | grep -q "Username"; then
    echo "⚠️  Not logged into DockerHub. Please run 'docker login' first."
    read -p "Do you want to login now? (y/n): " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        docker login
    else
        echo "❌ DockerHub login required for pushing images"
        exit 1
    fi
else
    echo "✅ Logged into DockerHub"
fi

# Build the Docker image
echo "🏗️  Building Docker image..."
echo "   Image: $IMAGE_NAME:$TAG"
echo "   Context: $BUILD_CONTEXT"
echo "   Dockerfile: $DOCKERFILE_PATH"

docker build -t "$IMAGE_NAME:$TAG" -f "$DOCKERFILE_PATH" "$BUILD_CONTEXT"
echo "✅ Docker image built successfully!"

# Tag as latest if not already
if [ "$TAG" != "latest" ]; then
    echo "🏷️  Tagging image as latest..."
    docker tag "$IMAGE_NAME:$TAG" "$IMAGE_NAME:latest"
    echo "✅ Tagged as latest"
fi

# Push to DockerHub
if [ "$PUSH" = "true" ]; then
    echo "🚀 Pushing to DockerHub..."
    
    # Push the specific tag
    echo "   Pushing $IMAGE_NAME:$TAG..."
    docker push "$IMAGE_NAME:$TAG"
    
    # Push latest if we tagged it
    if [ "$TAG" != "latest" ]; then
        echo "   Pushing $IMAGE_NAME:latest..."
        docker push "$IMAGE_NAME:latest"
    fi
    
    echo "✅ Successfully pushed to DockerHub!"
else
    echo "⏭️  Skipping push to DockerHub (as requested)"
fi

# Show final image info
echo "📋 Final Image Information:"
docker images | grep "$IMAGE_NAME"

echo ""
echo "🎉 Build and push completed successfully!"
echo "🔗 DockerHub: https://hub.docker.com/r/${IMAGE_NAME}"
echo "🚀 Run with: docker run -p 8501:8501 $IMAGE_NAME:$TAG"
