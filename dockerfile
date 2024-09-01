# Dockerfile
FROM python:3.10

ENV PIP_VERSION=24.2

# Set the working directory
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
#RUN echo "NGROK_AUTHTOKEN is: $NGROK_AUTHTOKEN"
#RUN pip install --upgrade --no-cache-dir pip
RUN pip3 install --no-cache-dir -r requirements.txt

# Copy the Streamlit app to the container
COPY app.py .

# Expose the port that Streamlit uses
EXPOSE 8501

# Command to run the app
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=127.0.0.1"]
