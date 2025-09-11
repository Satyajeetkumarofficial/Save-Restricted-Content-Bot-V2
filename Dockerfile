# Use a supported Debian version (bookworm is stable)
FROM python:3.10-slim-bookworm

# Install dependencies in one layer to reduce image size
RUN apt-get update && apt-get upgrade -y && \
    apt-get install -y --no-install-recommends \
        git curl wget ffmpeg bash neofetch software-properties-common && \
    rm -rf /var/lib/apt/lists/*

# Copy requirements first (better Docker caching)
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir --upgrade pip wheel && \
    pip install --no-cache-dir -r requirements.txt

# Set working directory
WORKDIR /app
COPY . .

# Expose Flask port
EXPOSE 5000

# Run both Flask and your Python module
CMD flask run -h 0.0.0.0 -p 5000 & python3 -m devgagan
