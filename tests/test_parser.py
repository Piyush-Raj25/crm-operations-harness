import sys

sys.path.append("src")

from llm.parser import LLMParser

response = """
Hello!

{
    "next_action":"Call customer",
    "assigned_team":"Sales",
    "reason":"High priority"
}
"""

print(LLMParser.parse(response))