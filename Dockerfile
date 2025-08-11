FROM python:3.12.9-slim-bullseye

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    libffi-dev \
    libssl-dev \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

# Expose the port the app runs on
EXPOSE 8000 

# Command to run the application
CMD ["python", "app.py"]