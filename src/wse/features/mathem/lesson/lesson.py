"""Defines base implementation for exercise lesson flow."""

from wse.features.mathem.lesson.interfaces import IExercise
from wse.features.shared.observer import Subject
from wse.interface.ifeatures import IListener, ISubject


class BaseLesson:
    """Abstract base class for managing exercise lifecycle."""

    def __init__(
        self,
        exercise: IExercise,
        subject: ISubject | None = None,
    ) -> None:
        """Construct the lesson."""
        self._exercise = exercise
        self._subject = subject if subject is not None else Subject()

    def create_task(self) -> None:
        """Generate new exercise task using configured exercise."""
        self._exercise.create_task()

    def check_answer(self, answer: str) -> bool:
        """Validate user answer against exercise solution."""
        return self._exercise.check_answer(answer)

    def start_lesson(self, *, listener: IListener) -> None:
        """Subscribe a listener and start a lesson."""
        self.create_task()
        self.render_task()

    # Notifications
    @property
    def subject(self) -> ISubject:
        """Provides access to observer pattern subject."""
        return self._subject

    def render_task(self) -> None:
        """Notify observers with formatted task string."""
        self.subject.notify('render_task', value=self._exercise.task)
