from llm.ollama_client import OllamaClient
from llm.prompts import PlannerPrompt
from llm.parser import LLMParser

from tools.retry import Retry
from tools.logger import AuditLogger


class PlannerService:
    """
    Handles AI-powered planning.
    """

    def __init__(self, logger: AuditLogger):
        self.client = OllamaClient()
        self.logger = logger

    def generate_plan(self, lead, priority):

        prompt = PlannerPrompt.build(
            lead,
            priority,
        )

        response = Retry.run(
            lambda: self.client.generate(prompt),
            retries=3,
            delay=1,
            on_retry=lambda attempt, error: self.logger.log(
                f"LLM retry {attempt}: {error}"
            ),
        )

        return LLMParser.parse(response)