"""Defines the protocols for subjects of math pages."""

from typing import Protocol

from wse.interface.iobserver import ISubject

# ruff: noqa: D101, D102, D204, E301, E302
# fmt: off


class ICalculationSubject(ISubject, Protocol):
    """Subject for notifying calculation model observers."""

    def notify_task_created(self, value: str) -> None:
        """Notify observers to show task text."""
        self.notify('display_task', value=value)

    def notify_answer_checked(self, value: str) -> None:
        """Notify observers that the answer has been checked."""
        self.notify('display_result', value=value)

    def notify_page_cleared(self) -> None:
        """Notify observers about full page reset."""
        self.notify('clear_page')


class IMathematicalSubject(ISubject, Protocol):
    """Subject for notifying mathematical model observers."""
