from tools.duplicate_checker import DuplicateChecker
from tools.logger import AuditLogger


class ToolRegistry:
    """
    Central registry for all tools used by the CRM Worker.
    """

    def __init__(self, logger: AuditLogger):
        self.tools = {
            "duplicate_checker": DuplicateChecker,
            "logger": logger,
        }

    def get_tool(self, name):
        return self.tools.get(name)