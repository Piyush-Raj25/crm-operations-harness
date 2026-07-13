import json


class LLMParser:

    REQUIRED_FIELDS = (
        "next_action",
        "assigned_team",
        "reason",
    )

    @staticmethod
    def parse(response: str):

        start = response.find("{")
        end = response.rfind("}")

        if start == -1 or end == -1:
            raise ValueError("No JSON found.")

        data = json.loads(response[start:end + 1])

        for field in LLMParser.REQUIRED_FIELDS:

            if field not in data:
                raise ValueError(f"Missing field: {field}")

        return data