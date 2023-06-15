import streamlit as st
from streamlit_extras.add_vertical_space import add_vertical_space

def sidebar():
    with st.sidebar:
        st.title("\U0001F916 Gameo Chat")
        st.write("Generate game ideas with the help of GPT-3")

        modelOption = st.selectbox("Model", ["OpenAI"])

        if modelOption == "OpenAI":
            st.text_input("API Key", "")

        add_vertical_space(5)
        st.write("Made by Johan")