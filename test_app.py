#done
import pytest
import requests
import json
from app import query, get_flowise_response

# Mock the API response for the query function
def mock_requests_post(*args, **kwargs):
    class MockResponse:
        def __init__(self, json_data, status_code):
            self.json_data = json_data
            self.status_code = status_code
        
        def json(self):
            return self.json_data
        
        @property
        def content(self):
            return json.dumps(self.json_data).encode()
    
    if args[0] == "https://wilkie-hf-space-tuto.hf.space/api/v1/prediction/037dd3d4-8492-45c4-9c5f-6ff84b8e95ee":
        return MockResponse({"text": "This is a response from the mock API."}, 200)
    return MockResponse({}, 404)

@pytest.fixture
def mock_requests(monkeypatch):
    monkeypatch.setattr(requests, "post", mock_requests_post)

def test_query_valid_response(mock_requests):
    payload = {"question": "What's the weather like?"}
    response = query(payload)
    assert response == {"text": "This is a response from the mock API."}

def test_query_invalid_response(mock_requests):
    # Modify the mock to return invalid JSON
    def mock_invalid_requests_post(*args, **kwargs):
        class MockInvalidResponse:
            @property
            def status_code(self):
                return 500
            
            @property
            def content(self):
                return b"Invalid JSON"
        
        return MockInvalidResponse()
    
    requests.post = mock_invalid_requests_post
    payload = {"question": "What's the weather like?"}
    response = query(payload)
    assert response == {}

def test_get_flowise_response(mock_requests):
    response = get_flowise_response("What's the weather like?")
    assert response == "This is a response from the mock API."

    # Test API error handling
    def mock_error_requests_post(*args, **kwargs):
        class MockErrorResponse:
            @property
            def status_code(self):
                return 500
            
            @property
            def content(self):
                return b""
        
        return MockErrorResponse()
    
    requests.post = mock_error_requests_post
    response = get_flowise_response("What's the weather like?")
    assert response == "Error: Unable to get a response from the API."
