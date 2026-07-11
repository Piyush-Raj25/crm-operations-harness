from models import workflow
from models.lead import Lead
from models.workflow import WorkflowState

from tools.logger import AuditLogger
from agents.validator import ValidatorAgent
from agents.analyzer import AnalyzerAgent


def main():

    lead = Lead(
        name="Rahul Sharma",
        phone="9876543210",
        email="rahul@gmail.com",
        company="ABC Pvt Ltd",
        business_type="Retail",
        city="Delhi",
        notes="Interested in payment solutions",
    )

    logger = AuditLogger()

    workflow = WorkflowState()

    validator = ValidatorAgent(logger)

    workflow = validator.validate(lead, workflow)
    if not workflow.validation_errors:
        analyzer = AnalyzerAgent(logger)
        workflow = analyzer.analyze(lead, workflow)

    print("\nPriority")
    print(workflow.priority)

    print("\nConfidence")
    print(workflow.confidence)    

    print("\nWorkflow Status")
    print(workflow.status)

    print("\nValidation Errors")
    print(workflow.validation_errors)

    print("\nAudit Log")

    for log in logger.get_logs():
        print(log)


if __name__ == "__main__":
    main()