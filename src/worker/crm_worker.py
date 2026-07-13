from models.lead import Lead
from models.workflow import WorkflowState, WorkflowStatus

from tools.logger import AuditLogger
from tools.tool_registry import ToolRegistry
from tools.memory import MemoryTool

from agents.validator import ValidatorAgent
from agents.analyzer import AnalyzerAgent
from agents.planner import PlannerAgent
from agents.reviewer import ReviewerAgent


class CRMWorker:
    """
    Orchestrates the complete CRM workflow from start to finish.
    """

    def __init__(self, logger: AuditLogger):
        self.logger = logger
        self.tool_registry = ToolRegistry(logger)

    def run(self, lead: Lead) -> WorkflowState:

        workflow = WorkflowState()

        # Step 1: Validate
        validator = ValidatorAgent(self.logger)
        workflow = validator.validate(lead, workflow)

        if workflow.validation_errors:
            return workflow

        # Step 2: Duplicate Check
        duplicate_checker = self.tool_registry.get_tool("duplicate_checker")

        workflow.duplicate_found = duplicate_checker.check_duplicate(lead)

        if workflow.duplicate_found:
            self.logger.log("Duplicate lead found.")

            workflow.status = WorkflowStatus.ESCALATED
            workflow.approved = False
            workflow.escalation_required = True
            workflow.review_notes = "Duplicate lead detected. Workflow stopped."

            return workflow

        # Step 3: Analyze
        analyzer = AnalyzerAgent(self.logger)
        workflow = analyzer.analyze(lead, workflow)

        # Step 4: Plan
        planner = PlannerAgent(self.logger)
        workflow = planner.plan(lead, workflow)

        # Step 5: Review
        reviewer = ReviewerAgent(self.logger)
        workflow = reviewer.review(workflow)

        # Step 6: Save to Memory
        MemoryTool.save_lead(lead, workflow)

        return workflow