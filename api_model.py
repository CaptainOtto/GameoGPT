import streamlit as st

class ApiModel():
    def __init__(self):
        if 'open_ai_api_key' not in st.session_state:
            st.session_state.open_ai_api_key = ''
            
        print("TEST" + st.session_state.open_ai_api_key)