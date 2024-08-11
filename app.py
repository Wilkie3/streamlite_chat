import streamlit as st
from streamlit_chat import message
import requests

# FlowiseAI API configuration
API_URL = "https://wilkie-hf-space-tuto.hf.space/api/v1/prediction/44ea4a5d-ba88-4f29-813c-47f71225c429"

def query(payload):
    response = requests.post(API_URL, json=payload)
    return response.json()

def get_flowise_response(user_input):
    payload = {
        "question": user_input
    }
    response = query(payload)
    
    if 'text' in response:
        return response['text']
    else:
        return f"Error: {response}"

if 'history' not in st.session_state:
    st.session_state['history'] = []

if 'generated' not in st.session_state:
    st.session_state['generated'] = ["Hello! Ask me anything about the weather or any other topic 🤖"]

if 'past' not in st.session_state:
    st.session_state['past'] = ["Hey! 👋"]

# Container for the chat history
response_container = st.container()
# Container for the user's text input
container = st.container()

with container:
    with st.form(key='my_form', clear_on_submit=True):
        user_input = st.text_input("Query:", placeholder="Talk to the chatbot here (:", key='input')
        submit_button = st.form_submit_button(label='Send')
        
    if submit_button and user_input:
        output = get_flowise_response(user_input)
        
        st.session_state['past'].append(user_input)
        st.session_state['generated'].append(output)

if st.session_state['generated']:
    with response_container:
        for i in range(len(st.session_state['generated'])):
            message(st.session_state["past"][i], is_user=True, key=str(i) + '_user', avatar_style="big-smile")
            message(st.session_state["generated"][i], key=str(i), avatar_style="thumbs")
