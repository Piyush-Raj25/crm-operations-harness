# SOUL.md

# CRM Operations Harness - Design Philosophy

## Purpose

The CRM Operations Harness is designed as an Autonomous AI Worker rather than a chatbot.

Its objective is to own an entire CRM workflow from start to finish while maintaining reliability, transparency, and predictable business behavior.

The worker combines deterministic business logic with AI-assisted reasoning instead of relying entirely on an LLM.

---

# Core Principles

## 1. Workflow Ownership

The worker owns the complete CRM workflow.

It is responsible for:

- validating input
- analyzing priority
- planning next actions
- reviewing results
- storing workflow memory
- maintaining audit logs

The user provides a lead.

The worker decides what should happen next.

---

## 2. AI as an Assistant

Artificial Intelligence improves business decisions.

Artificial Intelligence does not control the workflow.

The workflow remains deterministic.

Whenever AI fails, the system continues using rule-based logic.

---

## 3. Reliability Over Intelligence

The worker is designed to complete business workflows reliably.

A successful workflow is more valuable than an intelligent but unreliable workflow.

Therefore:

- retries are performed automatically
- failures are logged
- fallback logic always exists

---

## 4. Explainable Decisions

Every important decision is recorded.

Examples include:

- validation result
- priority assignment
- planner output
- retry attempts
- fallback activation
- workflow approval

This provides complete traceability.

---

## 5. Separation of Responsibilities

Each component has a single responsibility.

Agents make business decisions.

Tools perform reusable operations.

Models generate suggestions.

The CRM Worker orchestrates the workflow.

---

# Memory Strategy

Processed leads are stored in SQLite.

The stored information includes:

- Lead information
- Priority
- Approval status
- Review notes
- Timestamp

This enables future workflow analysis and historical tracking.

---

# Failure Strategy

The worker expects failures.

Failures are treated as part of normal execution.

Possible failures include:

- missing lead information
- duplicate leads
- unavailable AI model
- malformed AI responses
- timeout errors

Every failure has a recovery strategy.

---

# Current Capabilities

The current version can:

- validate CRM leads
- detect duplicate records
- analyze business priority
- generate AI-assisted plans
- retry failed AI requests
- fall back to deterministic planning
- review workflow quality
- store workflow history
- maintain an audit trail

---

# Future Improvements

Future versions may include:

- multi-model routing
- confidence-based escalation
- human approval queues
- vector memory
- external CRM integration
- REST API support
- dashboard and analytics
- asynchronous workflow execution