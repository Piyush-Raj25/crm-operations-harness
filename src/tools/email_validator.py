import re


class EmailValidator:
    """
    Validates whether an email address follows a basic format.
    """

    @staticmethod
    def is_valid(email: str | None) -> bool:
        if email is None:
            return False

        pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
        return re.match(pattern, email) is not None