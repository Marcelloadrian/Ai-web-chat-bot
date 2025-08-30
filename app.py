import streamlit as st
import os
from model import get_response

# Main application title and header
st.title("mini assignment c2")
st.header("welcome to my code this code is made by M in cooperation with gemini")

# Available Ollama models
# These models must be available on your local Ollama server.
available_models = ["llama3", "gemma", "mistral"]

# Session state to store conversation history and model settings
if "history" not in st.session_state:
    st.session_state.history = []
if "model" not in st.session_state:
    st.session_state.model = "llama3"

# Sidebar for model selection and conversation reset
st.sidebar.title("Configuration")
st.sidebar.header("Model")
selected_model = st.sidebar.selectbox(
    "Choose a model:",
    options=available_models,
    key="model"
)

# Chat interface
user_prompt = st.chat_input("Enter your prompt:")

# Handle user input and model response
if user_prompt:
    # Append user's message to history
    st.session_state.history.append({"role": "user", "content": user_prompt})
    
    # Get response from the selected model
    with st.spinner("Generating response..."):
        try:
            # Call the get_response function from your model.py file
            response = get_response(user_prompt, st.session_state.model)
            st.session_state.history.append({"role": "assistant", "content": response})
        except Exception as e:
            st.error(f"An error occurred: {e}")
            st.session_state.history.append({"role": "assistant", "content": f"An error occurred: {e}"})

# Display conversation history
for message in st.session_state.history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])