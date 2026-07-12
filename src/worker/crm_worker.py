from models.workflow import WorkflowState

from tools.logger import AuditLogger
from tools.duplicate_checker import DuplicateChecker

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

    def run(self, lead):

        workflow = WorkflowState()

        # ==========================
        # Step 1: Validate Lead
        # ==========================
        validator = ValidatorAgent(self.logger)
        workflow = validator.validate(lead, workflow)

        if workflow.validation_errors:
            return workflow

        # ==========================
        # Step 2: Duplicate Check
        # ==========================
        workflow.duplicate_found = DuplicateChecker.check_duplicate(lead)

        if workflow.duplicate_found:
            self.logger.log("Duplicate lead found.")
            return workflow

        # ==========================
        # Step 3: Analyze Lead
        # ==========================
        analyzer = AnalyzerAgent(self.logger)
        workflow = analyzer.analyze(lead, workflow)

        # ==========================
        # Step 4: Plan Next Action
        # ==========================
        planner = PlannerAgent(self.logger)
        workflow = planner.plan(lead, workflow)

        # ==========================
        # Step 5: Review Workflow
        # ==========================
        reviewer = ReviewerAgent(self.logger)
        workflow = reviewer.review(workflow)

        return workflow