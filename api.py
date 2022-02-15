import openai
import streamlit as st

openai.api_key = st.secrets["OPENAI_API_KEY"]

def openai_completion(transformed_user_input, selected_temperature, selected_tokens):
    response = openai.Completion.create(
        engine="code-davinci-001", 
        prompt=transformed_user_input, 
        temperature=selected_temperature,
        max_tokens=selected_tokens
    )
    code_response = response["choices"][0]["text"]
    return code_response