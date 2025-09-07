"""Task data source."""

import uuid
from dataclasses import dataclass


@dataclass
class TaskData:
    """Task data."""

    uid: uuid.UUID | None = None
    question: str | None = None
