from models.lead import Lead

from tools.logger import AuditLogger

from worker.crm_worker import CRMWorker


def main():

    lead = Lead(
        name="Rahul Sharma",
        phone="9999999999",
        email="rahul@gmail.com",
        company="ABC Pvt Ltd",
        business_type="Retail",
        city="Delhi",
        notes="Interested in payment solutions",
    )

    logger = AuditLogger()

    worker = CRMWorker(logger)

    workflow = worker.run(lead)

    print("\n========== CRM WORKFLOW RESULT ==========\n")

    print(f"Approved          : {workflow.approved}")
    print(f"Escalation Needed : {workflow.escalation_required}")
    print(f"Review Notes      : {workflow.review_notes}")
    print(f"Priority          : {workflow.priority}")
    print(f"Confidence        : {workflow.confidence:.2f}")
    print(f"Next Action       : {workflow.next_action}")
    print(f"Assigned Team     : {workflow.assigned_team}")
    print(f"Reason            : {workflow.reason}")
    print(f"Workflow Status   : {workflow.status.value}")
    print(f"Duplicate Found   : {workflow.duplicate_found}")
    print(f"Validation Errors : {workflow.validation_errors}")

    print("\n========== AUDIT LOG ==========")

    for log in logger.get_logs():
        print(log)


if __name__ == "__main__":
    main()