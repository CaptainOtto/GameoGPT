import os
import streamlit as st

# langchain
from langchain.llms  import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain
from langchain.memory import ConversationBufferMemory

from models import models


def generate_result():
    os.environ['OPENAI_API_KEY'] = st.session_state["OPENAI_API_KEY"]
    llm = OpenAI(temperature=1.2, max_tokens=100)

    highConcept_template = PromptTemplate(
        input_variables = ['instructions'],
        template = 'I want a high concept for a game based on these: {instructions}'
    )

    high_concept_memory = ConversationBufferMemory(input_key='instructions', memory_key='chat_history')
    game_idea_chain = LLMChain(llm=llm, prompt = highConcept_template, verbose=True,  output_key='high_concept', memory=high_concept_memory)

    game_idea_result = game_idea_chain.run(models.game_gen_models.getOptionsAsString())

    return game_idea_result