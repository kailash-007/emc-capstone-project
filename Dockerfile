# Use official lightweight Python image
FROM python:3.12-slim

# Prevent Python from writing .pyc files & buffer stdout/stderr
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory
WORKDIR /app

# Copy requirements file to container
COPY emc-capstone-project-src/requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY emc-capstone-project-src/ /app/

# Expose the port your app runs on
EXPOSE 5000

# Start the app
CMD ["python3", "app.py"]
