from models.lead import Lead
from models.workflow import WorkflowState, WorkflowStatus
from tools.email_validator import EmailValidator
from tools.logger import AuditLogger


class ValidatorAgent:
    """
    Validates incoming CRM leads.
    """

    def __init__(self, logger: AuditLogger):
        self.logger = logger

    def validate(self, lead: Lead, state: WorkflowState) -> WorkflowState:
        self.logger.log("Validation started.")

        state.status = WorkflowStatus.VALIDATING

        # Check required phone number
        if not lead.phone.strip():
            state.validation_errors.append("Phone number is missing.")

        # Validate email if provided
        if lead.email and not EmailValidator.is_valid(str(lead.email)):
            state.validation_errors.append("Invalid email address.")

        if state.validation_errors:
            state.status = WorkflowStatus.FAILED
            self.logger.log("Validation failed.")
        else:
            state.status = WorkflowStatus.VALIDATED
            self.logger.log("Validation passed.")

        return state