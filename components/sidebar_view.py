import streamlit as st
from streamlit_extras.buy_me_a_coffee import button as buymeacoffeebutton

from streamlit_extras.add_vertical_space import add_vertical_space

buy_me_a_coffe = """<script type="text/javascript" src="https://cdnjs.buymeacoffee.com/1.0.0/button.prod.min.js" data-name="bmc-button" data-slug="capnjohn" data-color="#FFDD00" data-emoji="🍺"  data-font="Cookie" data-text="Buy me a beer" data-outline-color="#000000" data-font-color="#000000" data-coffee-color="#ffffff" ></script>"""


def set_openai_api_key(api_key: str):
    st.session_state["OPENAI_API_KEY"] = api_key

def openai_ui():
    api_key_input = st.text_input(
        "OpenAI API Key",
        type="password",
        placeholder="Paste your OpenAI API key here (sk-...)",
        help="You can get your API key from https://platform.openai.com/account/api-keys.",  # noqa: E501
        value=st.session_state.get("OPENAI_API_KEY", ""),
    )

    if api_key_input:
        set_openai_api_key(api_key_input)

def sidebar_view():
    with st.sidebar:
        st.caption("version 0.0.1 Made by CaptnJohan  | [Github](https://github.com/CaptnJohn?tab=repositories)")

        st.title("\U0001F916 Gameo Chat")
        st.write("Generate game ideas with the help of GPT-3")
        st.caption("More model connections to will be added in the future.")

        st.title("Settings")
        modelOption = st.selectbox("Model", ["OpenAI"])

        if modelOption == "OpenAI":
            openai_ui()

        add_vertical_space(5)

        buymeacoffeebutton(username="capnjohn", floating=False, width=221)

    