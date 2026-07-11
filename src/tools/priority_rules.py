class PriorityRules:
    """
    Rule-based priority assignment.
    """

    HIGH_PRIORITY_CITIES = {
        "Delhi",
        "Mumbai",
        "Bengaluru"
    }

    HIGH_PRIORITY_BUSINESSES = {
        "Retail",
        "Finance",
        "Healthcare"
    }

    @staticmethod
    def calculate_priority(lead):
        score = 0

        if lead.city in PriorityRules.HIGH_PRIORITY_CITIES:
            score += 40

        if lead.business_type in PriorityRules.HIGH_PRIORITY_BUSINESSES:
            score += 40

        if lead.notes and "urgent" in lead.notes.lower():
            score += 20

        if score >= 80:
            return "HIGH", 0.95

        elif score >= 50:
            return "MEDIUM", 0.80

        else:
            return "LOW", 0.60