import streamlit as st
from main_view import ui_main_view
from models import models

def main():
    st.set_page_config(page_title="Gameo Chat - An LLM-powered Streamlit app")

    hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """

    st.markdown(hide_streamlit_style, unsafe_allow_html=True)

    ui_main_view()

main()
