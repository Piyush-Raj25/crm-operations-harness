from pydantic import BaseModel


class WorkflowResult(BaseModel):
    """
    Final output of CRM Worker.
    """

    success: bool

    priority: str

    next_action: str

    confidence: float

    message: str