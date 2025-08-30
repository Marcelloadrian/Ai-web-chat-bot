from llama_index.llms.ollama import Ollama

def get_response(prompt: str, model_name: str = "llama3"):
    """
    Generates a response from the specified Ollama model.
        To use a different model, you must first pull it.
        For example, to use 'gemma', run:
        ollama pull gemma
    """
    try:
        # Initialize the Ollama LLM with the specified model name
        llm = Ollama(model=model_name)
        
        # Generate the response
        response = llm.complete(prompt)
        
        # Return the generated text
        return str(response)
    
    except Exception as e:
        # Return an informative error message if something goes wrong
        return f"An error occurred: {e}"