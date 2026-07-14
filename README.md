# CRM Operations Harness

An Autonomous AI Worker that manages a CRM lead workflow from start to finish.

This project was built as part of the Eko Autonomous AI Worker assignment to demonstrate workflow ownership, multi-agent orchestration, tool invocation, AI-assisted decision making, workflow state management, failure recovery, retry mechanisms, memory persistence, and audit logging.

Instead of acting as a chatbot, this worker autonomously processes CRM leads by validating input, detecting duplicate records, assigning priorities, generating follow-up actions using a local LLM (Ollama), reviewing the workflow, storing processed records, and maintaining a complete audit trail.

---

## Key Features

- Multi-agent workflow architecture
- AI-powered planning using Ollama (Llama 3.2)
- Rule-based fallback when AI fails
- Retry mechanism for transient AI failures
- Workflow state management
- SQLite-based memory for processed leads
- Duplicate lead detection
- Audit logging for every workflow step
- Configurable application settings
- Modular and extensible architecture

---

## Project Structure

```text
crm-operations-harness/

├── src/
│   ├── agents/
│   ├── ai/
│   ├── config/
│   ├── llm/
│   ├── models/
│   ├── tools/
│   ├── worker/
│   └── main.py
│
├── database/
│
├── docs/
│
├── README.md
├── AGENTS.md
├── CLAW.md
├── SOUL.md
├── TOOLS.md
```
## Installation

Clone the repository:

```bash
git clone <repository-url>
cd crm-operations-harness
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate the virtual environment:

**Windows**

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Install and run Ollama:

```bash
ollama pull llama3.2:3b
ollama run llama3.2:3b
```

---

## Running the Worker

Run the CRM workflow:

```bash
python src/main.py
```

---

## Example Workflow

1. Receive CRM lead
2. Validate required information
3. Check for duplicate records
4. Analyze lead priority
5. Generate next action using AI
6. Retry AI request on transient failures
7. Fall back to rule-based planning if AI fails
8. Review workflow
9. Store processed lead
10. Produce audit log

---

## Technologies Used

- Python 3
- Ollama
- Llama 3.2 (3B)
- SQLite
- Requests
- Object-Oriented Programming
- Modular Agent Architecture


---

# Example Input

```json
{
  "name": "Rahul Sharma",
  "phone": "9876543210",
  "email": "rahul@gmail.com",
  "company": "ABC Pvt Ltd",
  "business_type": "Retail",
  "city": "Delhi",
  "notes": "Interested in payment solutions"
}
```

# Example Output

```text
========== CRM WORKFLOW RESULT ==========

Approved          : True
Escalation Needed : False
Review Notes      : Workflow approved.
Priority          : HIGH
Confidence        : 0.95

Next Action       : Assign to Payment Solutions Team

Assigned Team     : Payment Solutions Team

Reason            : Lead has shown interest in payment solutions.

Workflow Status   : completed

Duplicate Found   : False
```

# Failure Example

When the AI model is unavailable or returns an invalid response, the workflow automatically retries the request.

If all retry attempts fail, the worker activates the deterministic rule-based planner.

Example audit log:

```text
Planning next action...

LLM retry 1...

LLM retry 2...

LLM retry 3...

AI planner failed.

Using rule-based planner.

Workflow completed successfully.
```


# Future Improvements

- REST API interface
- Human approval queue
- Multi-model AI routing
- External CRM integrations
- Vector memory for historical context
- Asynchronous workflow execution
- Dashboard for workflow analytics
- Confidence-based escalation