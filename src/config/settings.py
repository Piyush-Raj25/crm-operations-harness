"""
Application configuration.
"""

# -----------------------------
# Ollama Configuration
# -----------------------------

OLLAMA_MODEL = "llama3.2:3b"

OLLAMA_BASE_URL = "http://localhost:11434/api/generate"


# -----------------------------
# Retry Configuration
# -----------------------------

MAX_RETRIES = 3

RETRY_DELAY = 1


# -----------------------------
# Database Configuration
# -----------------------------

DATABASE_PATH = "database/crm.db"