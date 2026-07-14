import sys

sys.path.append("src")

from llm.ollama_client import OllamaClient


client = OllamaClient()

response = client.generate("Say hello in one sentence.")

print(response)