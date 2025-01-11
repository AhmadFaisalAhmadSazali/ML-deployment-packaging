ARG PYTHON_VERSION=3.12.8
FROM python:${PYTHON_VERSION}-slim AS base

# Avoid writing .pyc files and enable unbuffered logging
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory
WORKDIR /app

# Create a non-privileged user
ARG UID=10001
RUN adduser \
    --disabled-password \
    --gecos "" \
    --home "/nonexistent" \
    --shell "/sbin/nologin" \
    --no-create-home \
    --uid "${UID}" \
    appuser

# Install dependencies using a cache mount
# Ensure the requirements.txt is passed during build time
COPY requirements.txt .
RUN --mount=type=cache,target=/root/.cache/pip \
    pip install --no-cache-dir -r requirements.txt

# Switch to the non-privileged user
USER appuser

# Copy only the necessary files
COPY core ./core
COPY main.py .

# Expose the port FastAPI listens on
EXPOSE 8000

# Run the application using the fastapi CLI
CMD ["fastapi", "run", "main.py", "--host", "0.0.0.0", "--port", "8000"]