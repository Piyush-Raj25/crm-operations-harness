# AGENTS.md

# CRM Operations Harness - Agent Specification

## Overview

The CRM Operations Harness is built as a multi-agent workflow.

Each agent owns one specific business responsibility and passes the workflow state to the next agent.

This separation of responsibilities keeps the system modular, testable, and extensible.

---

# Workflow

Lead Input
    ↓
Validator Agent
    ↓
Analyzer Agent
    ↓
Planner Agent
    ↓
Reviewer Agent
    ↓
Memory Tool
    ↓
Completed

---

# 1. Validator Agent

## Responsibility

Checks whether the incoming lead contains all mandatory information.

## Inputs

- Lead

## Outputs

- Updated WorkflowState
- Validation errors (if any)

## Decisions

- Continue workflow
- Stop workflow if required fields are missing

---

# 2. Analyzer Agent

## Responsibility

Determines business priority for the lead.

## Inputs

- Lead
- WorkflowState

## Outputs

- Priority
- Confidence score

## Decisions

- HIGH
- MEDIUM
- LOW

---

# 3. Planner Agent

## Responsibility

Determines the best next action.

The planner first attempts AI planning using Ollama.

If AI is unavailable or returns an invalid response, the planner automatically falls back to deterministic business rules.

## Inputs

- Lead
- WorkflowState

## Outputs

- Next action
- Assigned team
- Business reason

---

# 4. Reviewer Agent

## Responsibility

Performs the final review before workflow completion.

## Inputs

- WorkflowState

## Outputs

- Approval status
- Escalation flag
- Review notes

---

# Agent Communication

Each agent receives the current WorkflowState.

The agent updates only the fields it owns.

The updated WorkflowState is passed to the next agent.

This ensures that no agent directly modifies another agent's responsibilities.