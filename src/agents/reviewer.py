from models.workflow import WorkflowStatus
from tools.logger import AuditLogger


class ReviewerAgent:
    """
    Reviews the workflow before completion.
    """

    def __init__(self, logger: AuditLogger):
        self.logger = logger

    def review(self, state):

        self.logger.log("Review started.")

        state.status = WorkflowStatus.REVIEWING

        # Validation failed
        if state.validation_errors:
            state.approved = False
            state.escalation_required = True
            state.review_notes = "Validation failed."

        # Duplicate lead
        elif state.duplicate_found:
            state.approved = False
            state.escalation_required = True
            state.review_notes = "Duplicate lead detected."

        # Low confidence
        elif state.confidence < 0.80:
            state.approved = False
            state.escalation_required = True
            state.review_notes = "Low confidence prediction."

        else:
            state.approved = True
            state.escalation_required = False
            state.review_notes = "Workflow approved."

            state.status = WorkflowStatus.COMPLETED

        self.logger.log(state.review_notes)

        return state