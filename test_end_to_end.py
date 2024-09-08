import requests
import pytest
import time

@pytest.fixture(scope="module")
def app_url():
    # URL of the Streamlit app running locally
    return 'http://streamlit:9602/'

def test_streamlit_app_status(app_url):
    # Wait for Streamlit to be fully up
    time.sleep(30)

    # Check access to the Streamlit app via the local address
    response = requests.get(app_url)
    print(f"GET request to Streamlit app returned status code: {response.status_code}")

    assert response.status_code == 200, f"Failed to access the Streamlit app. Status code: {response.status_code}"