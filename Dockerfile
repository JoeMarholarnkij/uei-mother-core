# Optimized Multi-Cloud Dockerfile for Render.com & Hugging Face Spaces
FROM python:3.11-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt gunicorn

# Copy application files
COPY uei_mother_cloud_v2.py .
COPY push_network/ ./push_network/
COPY docs/ ./docs/

# Default Environment
ENV PORT=7860
ENV MANDATE="Do Good No Lie No Harm Gratitude"
ENV SYSTEM_STATE="ABSOLUTE_PHYSICAL_REALITY"

# Expose port for Cloud platforms
EXPOSE 7860
EXPOSE 8080

# Run Flask application via Gunicorn WSGI
CMD exec gunicorn --bind 0.0.0.0:${PORT:-7860} uei_mother_cloud_v2:app
