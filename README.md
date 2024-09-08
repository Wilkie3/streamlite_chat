# Streamlit Weather Chatbot   

This setup deploys a weather chatbot application using Streamlit, which connects to a Flowise API for weather data and forecasts. It includes services for the Streamlit app, Ngrok for secure tunneling, and a testing environment.

## Prerequisites

1. **Docker**: Ensure Docker is installed on your system.
2. **Docker Compose**: Ensure Docker Compose is installed on your system.
3. **Ngrok Authtoken**: Obtain an Ngrok authtoken from [Ngrok's website](https://ngrok.com/) and add it to your `.env` file.

## Services

### `streamlit`

- **Build**: Uses the Dockerfile in the current directory.
- **Ports**: Exposes port `9602` for the Streamlit weather chatbot app.
- **Healthcheck**: Checks app health every 30 seconds.

### `ngrok`

- **Image**: Uses `wernight/ngrok`.
- **Command**: Creates a secure tunnel to the Streamlit app on port `9602` and exposes Ngrok's web interface on port `4040`.
- **Environment Variables**: Requires `NGROK_AUTHTOKEN` (set in `.env`).
- **Depends On**: Waits for the `streamlit` service to start.
- **Ports**: Exposes Ngrok's web interface on port `4040`.

### `tests`

- **Build**: Uses the Dockerfile in the current directory.
- **Command**: Runs `pytest` to execute tests.
- **Depends On**: Waits for `streamlit` and `ngrok` services to start.
- **Volumes**: Mounts the current directory for test access.
- **Working Directory**: Set to `/app`.

## Usage

1. Ensure you have Docker and Docker Compose installed.
2. Create a `.env` file in the project directory with your `NGROK_AUTHTOKEN`.
3. Run `docker-compose up` to start the services.
4. Access the Streamlit weather chatbot via Ngrok's public URL.

