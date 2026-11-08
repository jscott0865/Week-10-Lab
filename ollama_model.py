# ollama_model.py
# Author: Jackson Scott

from ollama import chat


class OllamaModel:
    """A model that talks to a local Ollama server."""

    def __init__(self, model_name="granite4.1:3b"):
        """Store the name of the Ollama model to use."""
        self.model_name = model_name

    def reply(self, instructions, history):
        """Send instructions and conversation history to Ollama and return its reply."""
        # Combine system instructions and history into the messages list
        messages = [{"role": "system", "content": instructions}] + history

        # Send the messages list to Ollama and return the text content
        response = chat(model=self.model_name, messages=messages)
        return response.message.content
