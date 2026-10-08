BLOCKED_PATTERNS = [
    "ignore previous instructions",
    "ignore all instructions",
    "delete all files",
    "api key",
    "secret",
    "system prompt",
    "reveal prompt",
    "drop database"
]


def validate_task(task: str):

    task_lower = task.lower()

    for pattern in BLOCKED_PATTERNS:
        if pattern in task_lower:
            raise ValueError(
                f"Blocked task detected: {pattern}"
            )

    return True