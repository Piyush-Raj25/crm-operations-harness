from models.lead import Lead


class DuplicateChecker:
    """
    Simulates checking whether a lead already exists in the CRM.
    """

    existing_phone_numbers = {
        "9999999999",
        "8888888888",
        "7777777777",
    }

    @classmethod
    def check_duplicate(cls, lead: Lead) -> bool:
        return lead.phone in cls.existing_phone_numbers