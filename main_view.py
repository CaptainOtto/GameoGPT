
import streamlit as st

# Gameo components
from components.game_generation_view import game_generation_view
from components.sidebar_view import sidebar_view
from components.chat_view import chat_view

def ui_main_view():
    game_gen_view_tab, chat_view_tab = st.tabs(["GameGen", "Chat"])
                               
    sidebar_view()

    with game_gen_view_tab:
        game_generation_view()

    with chat_view_tab:
        chat_view()
