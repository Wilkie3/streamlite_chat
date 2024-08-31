#!/bin/sh
ngrok http streamlit:8501 --log=stdout &
sleep 15
curl --silent http://127.0.0.1:4040/api/tunnels | jq -r '.tunnels[0].public_url'