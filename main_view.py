
import streamlit as st

# Gameo components
from components.game_generation_view import game_generation_view
from components.sidebar_view import sidebar_view

def ui_main_view():
                               
    sidebar_view()

    game_generation_view()

