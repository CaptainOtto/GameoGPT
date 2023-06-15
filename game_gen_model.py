import streamlit as st

class GameGenModel:
    def __init__(self, engine, dimension, artStyle, genre, description):
        self.engine = engine
        self.dimension = dimension
        self.artStyle = artStyle
        self.genre = genre
        self.description = description

    def getOptionsAsString(self):
        return f"Engine: {self.engine}, Dimension: {self.dimension}, Art Style: {self.artStyle}, Genre: {self.genre}, Description: {self.description}"
    
    def printSelection(self):
        st.subheader("Instructions:")

        st.write(f"Engine: {self.engine}")
        st.write(f"Dimension: {self.dimension}")
        st.write(f"Art Style: {self.artStyle}")
        st.write(f"Genre: {self.genre}")
        st.write(f"Description: {self.description}")

