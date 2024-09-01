import unittest
from unittest.mock import patch, MagicMock
import requests
from app import get_flowise_response, query  # Replace 'your_module' with the name of your Python file

class TestChatbotApp(unittest.TestCase):
    
    @patch('app.requests.post')  # Mocking requests.post to avoid real HTTP calls
    def test_query_function(self, mock_post):
        # Define the mock response
        mock_response = MagicMock()
        mock_response.json.return_value = {'text': 'This is a test response'}
        mock_post.return_value = mock_response

        # Call the query function
        payload = {"question": "What's the weather today?"}
        response = query(payload)

        # Verify the response
        self.assertEqual(response['text'], 'This is a test response')
        mock_post.assert_called_once_with("https://wilkie-hf-space-tuto.hf.space/api/v1/prediction/71a43c0e-b730-4fbe-8506-47c653d39095", json=payload)
    
    @patch('app.query')  # Mock the query function to avoid real API calls
    def test_get_flowise_response(self, mock_query):
        # Define the mock return value of the query function
        mock_query.return_value = {'text': 'This is a mock response'}
        
        # Call the get_flowise_response function
        response = get_flowise_response("Hello")
        
        # Verify the response
        self.assertEqual(response, 'This is a mock response')
        mock_query.assert_called_once_with({"question": "Hello"})

        # Test the error case
        mock_query.return_value = {}  # No 'text' in response
        response = get_flowise_response("Hello")
        self.assertEqual(response, 'Error: Unable to get a response from the API.')

if __name__ == '__main__':
    unittest.main()