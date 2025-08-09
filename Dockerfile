# Multi-stage Dockerfile for CareerWise AI
# Stage 1: Build the Next.js frontend
FROM node:18-alpine AS frontend-builder

WORKDIR /app/frontend

# Copy package files
COPY package*.json ./
RUN npm ci --only=production

# Copy frontend source
COPY app ./app
COPY components ./components
COPY types ./types
COPY next.config.js ./
COPY tsconfig.json ./
COPY tailwind.config.js ./
COPY postcss.config.js ./
COPY next-env.d.ts ./

# Create public directory if it doesn't exist
RUN mkdir -p public

# Build the frontend
RUN npm run build

# Stage 2: Setup Python backend
FROM python:3.12-slim AS backend-builder

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copy Python requirements
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Install Ollama client
RUN pip install ollama

# Stage 3: Final production image
FROM python:3.12-slim AS production

WORKDIR /app

# Install system dependencies and Node.js
RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    curl \
    && curl -fsSL https://deb.nodesource.com/setup_18.x | bash - \
    && apt-get install -y nodejs \
    && rm -rf /var/lib/apt/lists/*

# Copy Python dependencies from backend-builder
COPY --from=backend-builder /usr/local/lib/python3.12/site-packages /usr/local/lib/python3.12/site-packages
COPY --from=backend-builder /usr/local/bin /usr/local/bin

# Copy frontend build from frontend-builder
COPY --from=frontend-builder /app/frontend/.next ./.next
COPY --from=frontend-builder /app/frontend/public ./public
COPY --from=frontend-builder /app/frontend/package*.json ./
COPY --from=frontend-builder /app/frontend/next.config.js ./

# Install only production dependencies for frontend
RUN npm ci --only=production

# Copy Python application code
COPY src ./src
COPY backend_api.py .
COPY main.py .
COPY templates ./templates
COPY static ./static

# Create directories for uploads and temp files
RUN mkdir -p temp uploads logs

# Copy configuration files
COPY config ./config

# Create a startup script
RUN echo '#!/bin/bash\n\
# Start the FastAPI backend in the background\n\
python backend_api.py &\n\
BACKEND_PID=$!\n\
\n\
# Start the Next.js frontend in the background\n\
npm start &\n\
FRONTEND_PID=$!\n\
\n\
# Wait for any process to exit\n\
wait -n\n\
\n\
# Exit with status of process that exited first\n\
exit $?' > /app/start.sh && chmod +x /app/start.sh

# Expose ports
EXPOSE 3000 8000 8501

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
  CMD curl -f http://localhost:3000/api/health || curl -f http://localhost:8000/api/health || exit 1

# Set environment variables
ENV NODE_ENV=production
ENV PYTHONPATH=/app/src
ENV PYTHONUNBUFFERED=1

# Start both services
CMD ["/app/start.sh"]
