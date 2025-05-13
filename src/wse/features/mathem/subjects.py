"""Defines the subjects of math pages."""

from wse.features.shared.observer import Subject


class CalculationSubject(Subject):
    """Subject for notifying calculation page model observers."""

    def notify_task_created(self, value: str) -> None:
        """Notify observers to show task text."""
        self.notify('display_task', value=value)

    def notify_answer_checked(self, value: str) -> None:
        """Notify observers that the answer has been checked."""
        self.notify('display_result', value=value)

    def notify_page_cleared(self) -> None:
        """Notify observers about full page reset."""
        self.notify('clear_page')


class MathematicalSubject(Subject):
    """Subject for notifying mathematical page model observers."""
