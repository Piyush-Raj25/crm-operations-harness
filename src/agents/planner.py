from models.workflow import WorkflowStatus
from tools.logger import AuditLogger


class PlannerAgent:
    """
    Decides the next action for the lead.
    """

    def __init__(self, logger: AuditLogger):
        self.logger = logger

    def plan(self, lead, state):

        self.logger.log("Planning next action.")

        state.status = WorkflowStatus.PLANNING

        if state.priority == "HIGH":
            state.next_action = "Call customer within 1 hour"
            state.assigned_team = "Enterprise Sales"
            state.reason = "High-priority lead with complete profile."

        elif state.priority == "MEDIUM":
            state.next_action = "Send follow-up email"
            state.assigned_team = "Sales Executive"
            state.reason = "Medium-priority lead."

        else:
            state.next_action = "Add to marketing campaign"
            state.assigned_team = "Marketing"
            state.reason = "Low-priority lead."

        self.logger.log(
            f"Planner assigned '{state.next_action}' to {state.assigned_team}."
        )

        return state