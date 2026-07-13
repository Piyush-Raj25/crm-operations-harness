class PlannerPrompt:

    @staticmethod
    def build(lead, priority):

        return f"""
You are an intelligent CRM Operations AI Worker.

Your task is to decide the next business action.

Return ONLY valid JSON.

Lead Details:

Name: {lead.name}
Company: {lead.company}
Business Type: {lead.business_type}
City: {lead.city}
Priority: {priority}
Notes: {lead.notes}

Return exactly:

{{
    "next_action": "...",
    "assigned_team": "...",
    "reason": "..."
}}

Do not explain anything.
Do not use markdown.
Return JSON only.
"""