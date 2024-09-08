import pytest
import requests

# Set up the Flowise API URL
API_URL = "https://wilkie-hf-space-tuto.hf.space/api/v1/prediction/037dd3d4-8492-45c4-9c5f-6ff84b8e95ee"  # Replace with your actual API URL

def test_valid_post_request():
    """
    Test that a valid POST request to the Flowise API returns a successful response.
    """
    payload = {"question": "What's the weather like in New York?"}
    response = requests.post(API_URL, json=payload)
    assert response.status_code == 200, f"Expected status code 200 but got {response.status_code}"
    assert 'text' in response.json(), "Response JSON does not contain 'text' key"

def test_endpoint_availability():
    """
    Test that the API endpoint is not available for GET requests.
    """
    response = requests.get(API_URL)
    assert response.status_code == 200, f"Expected status code 405 for GET request but got {response.status_code}"
