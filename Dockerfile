# ---------------------------------------------------------
# Base Image
# ---------------------------------------------------------
FROM python:3.12-slim

# ---------------------------------------------------------
# Environment Variables
# ---------------------------------------------------------
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

# ---------------------------------------------------------
# Create Non-Root User
# ---------------------------------------------------------
RUN groupadd --system appgroup && \
    useradd --system --gid appgroup --create-home appuser

# ---------------------------------------------------------
# Working Directory
# ---------------------------------------------------------
WORKDIR /app

# ---------------------------------------------------------
# Install Python Dependencies
# ---------------------------------------------------------
COPY requirements.txt .

RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# ---------------------------------------------------------
# Copy Application
# ---------------------------------------------------------
COPY . .

# ---------------------------------------------------------
# File Permissions
# ---------------------------------------------------------
RUN chown -R appuser:appgroup /app

USER appuser

# ---------------------------------------------------------
# Application Port
# ---------------------------------------------------------
EXPOSE 5000

# ---------------------------------------------------------
# Health Check
# ---------------------------------------------------------
HEALTHCHECK --interval=30s --timeout=5s --start-period=30s --retries=3 \
CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:5000/health')"

# ---------------------------------------------------------
# Start Application
# ---------------------------------------------------------
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--workers", "2", "--threads", "4", "--timeout", "60", "run:app"]