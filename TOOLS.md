# TOOLS.md

# CRM Operations Harness - Tool Definitions

## Overview

The CRM Operations Harness uses reusable tools to perform specific operations.

Unlike agents, tools do not make business decisions.

They provide capabilities that agents invoke while executing the workflow.

---

# Tool Architecture

Validator Agent
        │
        ▼
Duplicate Checker

Analyzer Agent
        │
        ▼
Priority Rules

Planner Agent
        │
        ▼
Ollama Client
        │
        ▼
Retry Utility

Reviewer Agent

        │
        ▼
Audit Logger

CRM Worker
        │
        ▼
Memory Tool

---

# 1. Duplicate Checker

## Purpose

Detects whether the incoming lead already exists.

## Input

Lead

## Output

Boolean

## Used By

Validator / CRM Worker

---

# 2. Audit Logger

## Purpose

Maintains a chronological audit trail of every workflow action.

## Input

Log message

## Output

Timestamped log entry

Example

[2026-07-14 10:20:11]
Validation started.

---

# 3. Memory Tool

## Purpose

Stores processed leads inside SQLite.

## Input

Lead

WorkflowState

## Output

Persistent database record

---

# 4. Retry Utility

## Purpose

Retries transient AI failures before giving up.

## Features

- Configurable retry count
- Configurable retry delay
- Retry callback support
- Raises last exception after retries are exhausted

---

# 5. Ollama Client

## Purpose

Communicates with the local Ollama server.

## Input

Prompt

## Output

LLM response

## Handles

- Connection failures
- Timeout failures
- HTTP failures

---

# Tool Contracts

Every tool follows these principles:

- Single responsibility
- Reusable
- Independent of business logic
- Testable
- Stateless whenever possible

Business decisions remain inside agents.