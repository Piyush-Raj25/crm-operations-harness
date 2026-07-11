from models.workflow import WorkflowStatus
from tools.priority_rules import PriorityRules
from tools.logger import AuditLogger


class AnalyzerAgent:
    """
    Determines lead priority.
    """

    def __init__(self, logger: AuditLogger):
        self.logger = logger

    def analyze(self, lead, state):

        self.logger.log("Priority analysis started.")

        state.status = WorkflowStatus.ANALYZING

        priority, confidence = PriorityRules.calculate_priority(lead)

        state.priority = priority
        state.confidence = confidence

        self.logger.log(
            f"Priority assigned: {priority} ({confidence:.2f})"
        )

        return state