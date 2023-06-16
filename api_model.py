import streamlit as st

class ApiModel():
    def __init__(self):
        if 'OPENAI_API_KEY' not in st.session_state:
            st.session_state.open_ai_api_key = ''