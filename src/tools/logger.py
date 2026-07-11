from datetime import datetime


class AuditLogger:
    """
    Maintains an audit trail of all worker actions.
    """

    def __init__(self):
        self.logs = []

    def log(self, message: str):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        entry = f"[{timestamp}] {message}"
        self.logs.append(entry)

    def get_logs(self):
        return self.logs