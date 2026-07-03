# -----------------------------------------------------------------------------
# Base Image
# -----------------------------------------------------------------------------
FROM python:3.12-slim

# -----------------------------------------------------------------------------
# Image Metadata
# -----------------------------------------------------------------------------
LABEL org.opencontainers.image.title="inventory-service" \
      org.opencontainers.image.description="Flask application demonstrating Argo Rollouts progressive delivery" \
      org.opencontainers.image.vendor="Murali Krishna" \
      org.opencontainers.image.licenses="MIT"

# -----------------------------------------------------------------------------
# Environment Variables
# -----------------------------------------------------------------------------
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    APP_HOME=/app

# -----------------------------------------------------------------------------
# Create Non-Root User
# -----------------------------------------------------------------------------
RUN groupadd --system appgroup && \
    useradd --system --gid appgroup --create-home appuser

# -----------------------------------------------------------------------------
# Working Directory
# -----------------------------------------------------------------------------
WORKDIR ${APP_HOME}

# -----------------------------------------------------------------------------
# Install Dependencies
# -----------------------------------------------------------------------------
COPY requirements.txt .

RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# -----------------------------------------------------------------------------
# Copy Application
# -----------------------------------------------------------------------------
COPY --chown=appuser:appgroup . .

# -----------------------------------------------------------------------------
# Switch to Non-Root User
# -----------------------------------------------------------------------------
USER appuser

# -----------------------------------------------------------------------------
# Expose Application Port
# -----------------------------------------------------------------------------
EXPOSE 5000

# -----------------------------------------------------------------------------
# Health Check
# -----------------------------------------------------------------------------
HEALTHCHECK --interval=30s --timeout=5s --start-period=30s --retries=3 CMD python -c "import urllib.request; urllib.request.urlopen('http://127.0.0.1:5000/health')"

# -----------------------------------------------------------------------------
# Start Application
# -----------------------------------------------------------------------------
CMD ["gunicorn", "--bind=0.0.0.0:5000", "--workers=2", "--threads=4", "--timeout=60", "run:app"]