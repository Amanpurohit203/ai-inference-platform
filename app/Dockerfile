# --- Stage 1: Build dependencies ---
FROM python:3.12-slim AS builder

WORKDIR /app

# Install build essentials in case any wheels need local compilation
RUN apt-get update && apt-get install -y --no-install-recommends gcc build-essential && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir --user torch --index-url https://download.pytorch.org/whl/cpu
RUN pip install --no-cache-dir --user -r requirements.txt
# --- Stage 2: Final runtime ---
FROM python:3.12-slim

WORKDIR /app

# Copy the pre-installed python packages from builder stage
COPY --from=builder /root/.local /root/.local

# Copy your local app/ folder into the container's /app/app/ directory
COPY main.py .

# Setup Environment Variables
ENV PATH=/root/.local/bin:$PATH
ENV HF_HOME=/app/hf_cache
ENV PYTHONUNBUFFERED=1

# Pre-create the HuggingFace cache directory
RUN mkdir -p /app/hf_cache

EXPOSE 8000

# Health check targeting your explicit /health route
HEALTHCHECK --interval=30s --timeout=5s --start-period=30s \
  CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:8000/health')" || exit 1

# Start Uvicorn targeting app.main:app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]