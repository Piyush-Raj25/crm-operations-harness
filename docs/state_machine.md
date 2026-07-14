# Workflow State Machine

```mermaid
stateDiagram-v2

[*] --> Validation

Validation --> Analysis

Validation --> Failed

Analysis --> Planning

Planning --> Review

Planning --> Retry

Retry --> Planning

Retry --> RuleBasedPlanner

RuleBasedPlanner --> Review

Review --> Completed

Review --> Escalated

Completed --> [*]

Escalated --> [*]

Failed --> [*]

```