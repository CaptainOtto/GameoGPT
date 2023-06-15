import os

# Dev 
from apikey import apikey

# Gameo Chat
from game_instructions import GameInstructions
from sidebar import sidebar

# streamlit
import streamlit as st
from streamlit_chat import message

# langchain
from langchain.llms  import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain
from langchain.memory import ConversationBufferMemory

os.environ['OPENAI_API_KEY'] = apikey
llm = OpenAI(temperature=1.2)

st.set_page_config(page_title="Gameo Chat - An LLM-powered Streamlit app")

sidebar()

engineOption = st.selectbox("Engine", ["Unreal Engine", "Unity", "Godot"])
dimensionOption = st.selectbox("Dimensions", ["2D", "3D"])
artStyle = st.selectbox("Art Style", ["Realistic", "Stylized Realism", "Stylized", "Pixel art", "Low Poly"])
genre = st.multiselect("Genre", ["Survival", "Fighting", "Racing", "Puzzle", "Action", "Fps", "Strategy", "Rpg", "Stealth"])

gameInstructions = GameInstructions(engineOption, dimensionOption, artStyle, genre, "")

optionalDescription = st.text_input("Description", "")

if(optionalDescription):
    gameInstructions.description = optionalDescription

if st.button("Generate"):
    
    st.header("Game Idea")

    gameInstructions.printSelection()

    st.write("---")

    highConcept_template = PromptTemplate(
        input_variables = ['instructions'],
        template = 'I want a high concept for a game based on these: {instructions}'
    )

    high_concept_memory = ConversationBufferMemory(input_key='instructions', memory_key='chat_history')
    game_idea_chain = LLMChain(llm=llm, prompt = highConcept_template, verbose=True,  output_key='high_concept', memory=high_concept_memory)

    game_idea_result = game_idea_chain.run(gameInstructions.getOptionsAsString())

    message(game_idea_result)

    st.download_button("Download", game_idea_result)
    
