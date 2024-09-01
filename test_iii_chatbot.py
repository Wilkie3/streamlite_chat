import unittest
import streamlit as st
from unittest.mock import patch, MagicMock
from app import get_flowise_response, query  # Replace 'your_module' with your actual module name

class TestChatbotApp(unittest.TestCase):
    
    @patch('app.requests.post')
    def test_query_function(self, mock_post):
        # Mock a successful response
        mock_response = MagicMock()
        mock_response.json.return_value = {'text': 'This is a test response'}
        mock_post.return_value = mock_response

        # Test with a normal payload
        payload = {"question": "What's the weather today?"}
        response = query(payload)
        self.assertEqual(response['text'], 'This is a test response')
        mock_post.assert_called_once_with("https://wilkie-hf-space-tuto.hf.space/api/v1/prediction/71a43c0e-b730-4fbe-8506-47c653d39095", json=payload)
        
        # Mock a failed response
        mock_response.json.return_value = {}
        mock_post.return_value = mock_response
        response = query(payload)
        self.assertEqual(response, {})  # Expecting an empty dictionary

    @patch('app.query')
    def test_get_flowise_response(self, mock_query):
        # Mock the successful response
        mock_query.return_value = {'text': 'This is a mock response'}
        response = get_flowise_response("Hello")
        self.assertEqual(response, 'This is a mock response')
        mock_query.assert_called_once_with({"question": "Hello"})

        # Mock a response with no 'text' field
        mock_query.return_value = {}
        response = get_flowise_response("Hello")
        self.assertEqual(response, 'Error: Unable to get a response from the API.')

    @patch('app.query')
    def test_get_flowise_response_edge_cases(self, mock_query):
        # Test empty input
        mock_query.return_value = {'text': 'No input provided'}
        response = get_flowise_response("")
        self.assertEqual(response, 'No input provided')

        # Test special character input
        mock_query.return_value = {'text': 'Received special characters'}
        response = get_flowise_response("!@#$%^&*()")
        self.assertEqual(response, 'Received special characters')

        # Mock an API failure
        mock_query.return_value = {'error': 'API is down'}
        response = get_flowise_response("Test input")
        self.assertEqual(response, 'Error: Unable to get a response from the API.')

    @patch('app.st.text_input')  # Mock Streamlit's text input
    @patch('app.st.session_state', {'input': '', 'generated': [], 'past': []})
    def test_app_run(self, mock_text_input):
        # Simulate user input
        mock_text_input.return_value = "How's the weather?"

        # Check initial session state
        self.assertEqual(st.session_state['input'], '')
        self.assertEqual(st.session_state['generated'], [])
        self.assertEqual(st.session_state['past'], [])

        # Simulate running the app with user input
        st.session_state['input'] = mock_text_input()
        st.session_state['past'].append(st.session_state['input'])
        st.session_state['generated'].append("Sunny with a chance of rain.")

        # Check updated session state
        self.assertEqual(st.session_state['input'], "How's the weather?")
        self.assertEqual(st.session_state['past'], ["How's the weather?"])
        self.assertEqual(st.session_state['generated'], ["Sunny with a chance of rain."])

if __name__ == '__main__':
    unittest.main()
