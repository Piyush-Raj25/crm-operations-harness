from llm.ollama_client import OllamaClient
from llm.prompts import PlannerPrompt
from llm.parser import LLMParser


class PlannerService:
    """
    Handles AI-powered planning.
    """

    def __init__(self):
        self.client = OllamaClient()

    def generate_plan(self, lead, priority):

        prompt = PlannerPrompt.build(
            lead,
            priority,
        )

        response = self.client.generate(prompt)

        return LLMParser.parse(response)