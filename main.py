import os
import streamlit as st
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

st.title("OH Test streamlit auth")
user_input = st.text_input("Instructions", "Enter your instructions here")

st.code(user_input, language="python")