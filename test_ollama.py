# test_ollama.py
from ollama_model import OllamaModel

model = OllamaModel("granite4.1:3b")

instructions = "You are Sunny, a support assistant for Bayside Outfitters. Answer in one short sentence."
history = [{"role": "user", "content": "What are your store hours?"}]

reply = model.reply(instructions, history)
print("Model Reply:", reply)
