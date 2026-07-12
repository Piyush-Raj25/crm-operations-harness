from models.lead import Lead
from models.workflow import WorkflowState

from tools.logger import AuditLogger
from tools.duplicate_checker import DuplicateChecker

from agents.validator import ValidatorAgent
from agents.analyzer import AnalyzerAgent
from agents.planner import PlannerAgent


def main():
    # Sample lead (replace with API/UI input later)
    lead = Lead(
        name="Rahul Sharma",
        phone="9876543210",
        email="rahul@gmail.com",
        company="ABC Pvt Ltd",
        business_type="Retail",
        city="Delhi",
        notes="Interested in payment solutions",
    )

    # Initialize logger and workflow state
    logger = AuditLogger()
    workflow = WorkflowState()

    # ==========================
    # Step 1: Validate Lead
    # ==========================
    validator = ValidatorAgent(logger)
    workflow = validator.validate(lead, workflow)

    if workflow.validation_errors:
        print("\nValidation Failed!")
        print(workflow.validation_errors)

        print("\n========== AUDIT LOG ==========")
        for log in logger.get_logs():
            print(log)

        return

    # ==========================
    # Step 2: Duplicate Check
    # ==========================
    workflow.duplicate_found = DuplicateChecker.check_duplicate(lead)

    if workflow.duplicate_found:
        logger.log("Duplicate lead found.")

        print("\nDuplicate Lead Detected!")

        print("\n========== AUDIT LOG ==========")
        for log in logger.get_logs():
            print(log)

        return

    # ==========================
    # Step 3: Analyze Lead
    # ==========================
    analyzer = AnalyzerAgent(logger)
    workflow = analyzer.analyze(lead, workflow)

    # ==========================
    # Step 4: Plan Next Action
    # ==========================
    planner = PlannerAgent(logger)
    workflow = planner.plan(lead, workflow)

    # ==========================
    # Final Output
    # ==========================
    print("\n========== CRM WORKFLOW RESULT ==========\n")

    print(f"Priority           : {workflow.priority}")
    print(f"Confidence         : {workflow.confidence:.2f}")
    print(f"Next Action        : {workflow.next_action}")
    print(f"Assigned Team      : {workflow.assigned_team}")
    print(f"Reason             : {workflow.reason}")
    print(f"Workflow Status    : {workflow.status.value}")
    print(f"Duplicate Found    : {workflow.duplicate_found}")
    print(f"Validation Errors  : {workflow.validation_errors}")

    print("\n========== AUDIT LOG ==========")

    for log in logger.get_logs():
        print(log)


if __name__ == "__main__":
    main()