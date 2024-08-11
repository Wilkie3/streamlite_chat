# Streamlit Chatbot with ngrok

This project sets up a simple Streamlit chatbot application and exposes it to the internet using ngrok.

## Prerequisites

- Docker
- Docker Compose
- ngrok account with authtoken

## Setup

1. Clone the repository.
2. Replace `<your_ngrok_authtoken>` in the `docker-compose.yml` file with your actual ngrok authtoken.
3. Build and run the Docker containers:

   ```bash
   docker-compose up --build
