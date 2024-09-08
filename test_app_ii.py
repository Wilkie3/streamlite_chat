# test_app.py
import requests
import pytest
import time

@pytest.fixture(scope="module")
def app_url():
    # URL of the Streamlit app
    return 'http://streamlit:9602/'

def test_streamlit_app_status(app_url):
    time.sleep(45)  # Increased sleep time for app startup
    response = requests.get(app_url)
    assert response.status_code == 200, f"Failed to access the Streamlit app. Status code: {response.status_code}"

