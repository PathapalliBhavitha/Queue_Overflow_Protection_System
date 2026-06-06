# Queue Overflow Protection System

## Objective

Protect backend services during heavy traffic spikes.

Features:

- Rate Limiting
- Queue Overflow Protection
- Burst Traffic Handling
- Request Rejection

---

## Project Structure

```text
queue_overflow_protection/
│
├── README.md
├── integration.py
├── overflow_handler.py
├── queue_manager.py
├── rate_limiter.py
└── test.py
```

## Requirements

Python 3.8+

## Installation

Check Python version:

```bash
python --version
```

or

```bash
python3 --version
```

## Run Project

```bash
python test.py
```

## Expected Output

```text
Task Added: Task 1
Task Added: Task 2
Task Added: Task 3

[OVERFLOW] Task rejected: Task 4

[RATE LIMITED] User spammer
```

## Acceptance Criteria

✔ Rate limiting implemented

✔ Queue overflow protection implemented

✔ Burst traffic handled

✔ Overflow protection layer implemented