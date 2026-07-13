class OllamaConnectionError(Exception):
    """
    Raised when Ollama cannot be reached.
    """
    pass


class OllamaResponseError(Exception):
    """
    Raised when Ollama returns an invalid response.
    """
    pass