Local LLM Chatbot using Streamlit and Ollama
This is a simple chatbot application built with Python using Streamlit for the user interface and Ollama for running open-source large language models (LLMs) locally.

This project was created as a mini-assignment to demonstrate the basic setup and use of LLMs in a local environment.

Requirements
Before you can run this application, you need to have the following installed on your system:

Python 3.8+

Ollama: A local service for running open-source LLMs. You can download and install it from the official website: ollama.com.

Setup and Installation
Follow these steps to get the application up and running on your local machine.

Step 1: Install Python Libraries
You need to install the necessary Python libraries using pip. Open your terminal or command prompt and run the following command:

pip install streamlit llama-index-llms-ollama

Step 2: Set up Ollama
You must have the Ollama service running and the required models pulled to your local machine.

Start Ollama: Make sure Ollama is running in the background.

Pull Models: This application uses llama3, gemma, and mistral models. You can pull these models from the Ollama library by running the following commands in your terminal:

ollama pull llama3
ollama pull gemma
ollama pull mistral

Note: If the ollama command is not recognized, you need to add the Ollama installation directory to your system's PATH. On Windows, this is typically C:\Users\<YourUsername>\.ollama.

Step 3: Run the Application
Once the models are downloaded, you can run the Streamlit application. Open your terminal in the same directory as app.py and run:

streamlit run app.py

This command will start a local server and open the chatbot application in your web browser.

Project Structure
app.py: The main Streamlit application file. It contains the user interface, handles user input, and displays the conversation history.

model.py: This file contains the logic for interacting with the Ollama service. It includes a function get_response that sends a prompt to a specified LLM and returns the response.

Usage
After running streamlit run app.py, the application will open in your browser.

In the sidebar, you can select the LLM model you want to use (llama3, gemma, or mistral).

Type your message into the chat box at the bottom and press Enter to get a response from the selected model.

Created with assistance from Gemini.
