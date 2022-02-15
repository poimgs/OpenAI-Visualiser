from select import select
import streamlit as st
import helper
import api

# Main page components
def header():
    st.title("OpenAI Code Assistant")

def user_instructions_input():
    user_input = st.text_area("Instructions", "print hello world", height=200)
    return user_input

def openai_code(user_input, selected_temperature, selected_tokens):
    transformed_user_input = helper.transform_user_input_for_openai(user_input)
    code_response = api.openai_completion(transformed_user_input, selected_temperature, selected_tokens)
    
    st.write("## OpenAI's generated code")
    st.code(code_response)

    return transformed_user_input

def translated_instructions(transformed_user_input):
    with st.expander("Translated instructions for OpenAI"):
        st.code(transformed_user_input)

# Side bar components
def sidebar():
    selected_temperature = st.sidebar.slider("Variation", 0.0, 1.0, 0.0, 0.1)
    selected_tokens = st.sidebar.slider("Max words for OpenAI's generated code", 100, 1000, 300, 100)

    return selected_temperature, selected_tokens