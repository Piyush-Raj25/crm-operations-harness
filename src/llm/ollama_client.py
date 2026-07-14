import requests

from llm.exceptions import (
    OllamaConnectionError,
    OllamaResponseError,
)

from config.settings import (
    OLLAMA_MODEL,
    OLLAMA_BASE_URL,
)

class OllamaClient:
    """
    Client for communicating with the local Ollama server.
    """

    BASE_URL = OLLAMA_BASE_URL

    def __init__(self, model: str = OLLAMA_MODEL):
       self.model = model

    def generate(self, prompt: str) -> str:
        """
        Sends a prompt to Ollama and returns the generated response.
        """

        payload = {
            "model": self.model,
            "prompt": prompt,
            "stream": False,
        }

        try:

            response = requests.post(
                self.BASE_URL,
                json=payload,
                timeout=60,
            )

            response.raise_for_status()

        except requests.exceptions.HTTPError as e:
         raise OllamaConnectionError(
        f"Ollama returned an HTTP error: {e}"
    ) from e

        except requests.exceptions.ConnectionError as e:
         raise OllamaConnectionError(
        "Unable to connect to Ollama. Is Ollama running?"
    ) from e

        except requests.exceptions.Timeout as e:
         raise OllamaConnectionError(
        "Ollama request timed out."
    ) from e

        try:

            data = response.json()

            return data["response"]

        except Exception as e:
            raise OllamaResponseError(
                "Invalid response received from Ollama."
            ) from e