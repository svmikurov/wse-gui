"""Defines multiplication page model."""

from wse.features.base.mvc import BaseModel
from wse.features.mathem.lesson.calculations import MultiplicationTableExercise
from wse.features.mathem.lesson.lesson import BaseLesson


class MultiplicationModel(BaseModel):
    """Multiplication page model."""

    def __init__(self, *args: object, **kwargs: object) -> None:
        """Construct the model."""
        super().__init__(*args, **kwargs)

        self.lesson = BaseLesson(
            exercise=MultiplicationTableExercise(min_value=2, max_value=9),
        )
        self.lesson.subject.add_listener(self)

    # Listening to the `self.lesson`
    def render_task(self, value: object) -> None:
        """Display task."""
        self.subject.notify('display_task', value=value)
