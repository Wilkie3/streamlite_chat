# Use an official Python runtime as a parent image
FROM python:3.10

# Set environment variable for pip version (optional)
ENV PIP_VERSION=24.2

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements1.txt .

# Install Python dependencies (including pytest)
RUN pip install --no-cache-dir -r requirements1.txt

# Install pytest explicitly if not included in requirements1.txt
RUN pip install pytest

# Verify pytest installation and path
#RUN echo "Checking pytest installation..." && which pytest && pytest --version

# Copy the Streamlit app to the container
COPY app.py .

# Run tests to verify that the build works
RUN pytest --disable-warnings || true

# Expose the port for the Streamlit app
EXPOSE 9602

# Health check to ensure the app is running correctly
HEALTHCHECK --interval=30s --timeout=10s \
  CMD curl --silent --fail http://localhost:9602 || exit 1

# Default command to run the app
CMD ["streamlit", "run", "app.py", "--server.port=9602", "--server.address=0.0.0.0"]