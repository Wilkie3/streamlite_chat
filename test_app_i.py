import pytest
import streamlit as st
from app import get_flowise_response

@pytest.fixture
def mock_streamlit_session_state():
    """
    Fixture to mock Streamlit session state for testing.
    """
    st.session_state.clear()  # Ensure a clean session state for every test
    st.session_state['input'] = "What's the weather today?"
    st.session_state['submit_button'] = True  # Simulate the button click
    st.session_state['history'] = []
    st.session_state['generated'] = ["Hello! Ask me anything about the weather or any other topic 🤖"]
    st.session_state['past'] = ["Hey! 👋"]

def test_get_flowise_response(monkeypatch):
    # Mock the API response
    mock_response = {"text": "It's sunny today!"}

    def mock_query(payload):
        return mock_response

    monkeypatch.setattr('app.query', mock_query)

    # Test the response from get_flowise_response
    user_input = "What is the weather like today?"
    output = get_flowise_response(user_input)
    
    assert output == "It's sunny today!"

def test_streamlit_interaction(monkeypatch, mock_streamlit_session_state):
    # Mock the API response
    mock_response = {"text": "It's sunny today!"}

    def mock_query(payload):
        return mock_response

    monkeypatch.setattr('app.query', mock_query)

    # Simulate the app behavior when the user clicks the button
    if st.session_state['submit_button'] and st.session_state['input']:
        output = get_flowise_response(st.session_state['input'])
        st.session_state['past'].append(st.session_state['input'])
        st.session_state['generated'].append(output)

        # Verify the session state is updated correctly
        assert st.session_state['past'][-1] == "What's the weather today?"
        assert st.session_state['generated'][-1] == "It's sunny today!"
        assert len(st.session_state['generated']) == 2  # One initial message and one response