"""Exercise task."""

import uuid
from dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=True)
class Task:
    """Exercise task."""

    uid: uuid.UUID | None
    question: str | None

    correct_answer: str | None = None
    user_answer: str | None = None
    is_correct: bool | None = None
    solution: str | None = None
    completed: bool = False
    created_at: datetime = datetime.now()
    updated_at: datetime | None = None
