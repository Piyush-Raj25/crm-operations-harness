from enum import Enum

from pydantic import BaseModel, Field


class WorkflowStatus(str, Enum):
    RECEIVED = "received"
    VALIDATING = "validating"
    VALIDATED = "validated"
    ANALYZING = "analyzing"
    PLANNING = "planning"
    REVIEWING = "reviewing"
    COMPLETED = "completed"
    FAILED = "failed"
    ESCALATED = "escalated"


class WorkflowState(BaseModel):
    """
    Shared state of our CRM Worker.
    """

    status: WorkflowStatus = WorkflowStatus.RECEIVED

    confidence: float = 0.0

    validation_errors: list[str] = Field(default_factory=list)

    duplicate_found: bool = False

    priority: str | None = None

    next_action: str | None = None

    audit_log: list[str] = Field(default_factory=list)