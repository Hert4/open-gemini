
FROM python:3.11-slim

# Set environment variables to prevent interactive prompts during package installation
ENV DEBIAN_FRONTEND=noninteractive
ENV PYTHONUNBUFFERED=1

# Install system dependencies
# python3-tk/tk are required for pyautogui (even with our fix, it's better to have them)
# git is often useful
RUN apt-get update && apt-get install -y \
    python3-tk \
    tk \
    tcl \
    git \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install the package
# We install with [os] extras if defined, but open-gemini pyproject.toml implies standard install covers basics
RUN pip install --no-cache-dir .

# Create a non-root user for security (optional but good practice, though for CLI tools often root is used in docker)
# USER appuser

# Entrypoint to run open-gemini
ENTRYPOINT ["open-gemini"]
