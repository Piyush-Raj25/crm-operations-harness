# CLAW.md

# CRM Operations Harness Workflow Specification

## Purpose

The CRM Operations Harness autonomously manages a CRM lead from the moment it is received until the workflow is completed or escalated.

Instead of acting as a chatbot, the worker owns the complete business workflow by coordinating multiple agents, invoking tools, maintaining workflow state, recovering from failures, and recording every important decision.

---

# Overall Workflow

```
Receive Lead
      │
      ▼
Validate Lead
      │
      ▼
Duplicate Check
      │
      ▼
Priority Analysis
      │
      ▼
AI Planning
      │
      ├──────────────┐
      │              │
      ▼              │
AI Success           │
      │              │
      ▼              │
Review               │
      │              │
      ▼              │
Store Lead           │
      │              │
      ▼              │
Completed            │
                     │
                     ▼
             AI Failure
                     │
                     ▼
             Retry (3 Attempts)
                     │
                     ▼
          Rule-Based Planner
                     │
                     ▼
                 Review
                     │
                     ▼
                Store Lead
                     │
                     ▼
                 Completed
```

---

# Workflow States

The worker progresses through the following states:

- Validation
- Duplicate Check
- Analysis
- Planning
- Review
- Completed

If a duplicate lead is detected, the workflow is escalated immediately.

---

# Decision Flow

## Validation

Checks mandatory fields.

If validation fails:

- Workflow stops
- Validation errors are returned
- Audit log is updated

---

## Duplicate Detection

Checks whether the lead already exists.

If duplicate:

- Workflow is escalated
- Processing stops
- Duplicate event is logged

---

## Priority Analysis

Assigns one of:

- HIGH
- MEDIUM
- LOW

Also calculates a confidence score.

---

## AI Planning

The planner attempts to generate the next business action using the local Ollama model.

Expected output:

- Next Action
- Assigned Team
- Business Reason

---

## Failure Recovery

If AI planning fails:

1. Retry automatically.
2. Retry up to three times.
3. Log every retry attempt.
4. If all retries fail, activate the deterministic rule-based planner.

The workflow never terminates because of an AI failure.

---

## Review

The Reviewer Agent performs the final workflow validation.

It decides whether the workflow should:

- be approved
- be escalated

---

## Memory

Every successfully processed lead is stored in SQLite.

The stored information includes:

- Lead name
- Phone number
- Priority
- Approval status
- Review notes
- Timestamp

---

## Audit Trail

Every important workflow event is recorded.

Examples:

- Validation started
- Priority assigned
- Retry attempt
- AI planner success
- AI planner failure
- Rule-based fallback
- Workflow approved

This provides complete traceability of the workflow execution.