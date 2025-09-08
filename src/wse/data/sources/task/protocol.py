"""Protocol for Task source interface."""

import uuid
from typing import Protocol

from wse.feature.shared.schemas.task import Result


class TaskSourceProto(Protocol):
    """Task data."""

    def set_task(self, uid: uuid.UUID, question: str) -> None:
        """Set task data."""

    def set_result(self, result: Result) -> None:
        """Set task result."""

    @property
    def uid(self) -> uuid.UUID | None:
        """Get task identifier (read-only)."""

    @property
    def correct_expression(self) -> str | None:
        """Get correct task expression (read-only)."""
