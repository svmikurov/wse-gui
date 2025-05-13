"""Mathematical feature model (MVC)."""

from dataclasses import dataclass

from wse.features.mathem.interfaces.iexercise import IExerciseSwitcher
from wse.features.mathem.interfaces.ipages import IMathematicalModel
from wse.features.mathem.interfaces.isubjects import IMathematicalSubject
from wse.features.mathem.sources import ExerciseSource
from wse.features.shared.enums import FieldID
from wse.features.shared.enums.exercises import Exercises
from wse.utils.contextmanagers import temporarily_disable_on_change_call


@dataclass
class MathematicalModel(IMathematicalModel):
    """Model for mathematical exercises page."""

    _subject: IMathematicalSubject
    _exercise_switcher: IExerciseSwitcher

    def __post_init__(self) -> None:
        """Initialise attributes."""
        self._exercises_source = ExerciseSource()

    def on_open(self) -> None:
        """Initialize model state when component is opened."""
        if not self.exercises_source.has_exercises:
            self._populate_selection_source()
            self._notify_set_default_exercise()

    # Listening to controller notifications

    def switch_exercise_type(self, exercise_type: Exercises) -> None:
        """Switch the current exercise type."""
        self._exercise_switcher.switch(exercise_type)

    # Properties

    @property
    def subject(self) -> IMathematicalSubject:
        """Get the model's subject instance."""
        return self._subject

    @property
    def exercises_source(self) -> ExerciseSource:
        """Get exercises source instance."""
        return self._exercises_source

    @property
    def _current_exercise_name(self) -> Exercises:
        """Get current exercise."""
        return self._exercise_switcher.current_exercise_name

    # Source methods

    def _populate_selection_source(self) -> None:
        """Populate selection source and notify listeners."""
        with temporarily_disable_on_change_call(
            self.subject, FieldID.EXERCISE_SELECTION
        ):
            self.exercises_source.clear()
            for args in self._exercise_switcher.exercises.items():
                self.exercises_source.add(*args)

    def _get_source_item(self, name: Exercises) -> object:
        """Get from source the exercise DTO by its name."""
        return self._exercises_source.find(name)

    # Notifications

    def _notify_set_default_exercise(self) -> None:
        """Notify the controller to set the default exercise."""
        with temporarily_disable_on_change_call(
            self.subject, FieldID.EXERCISE_SELECTION
        ):
            self.subject.notify(
                'set_default_selection',
                value=self._get_source_item(name=self._current_exercise_name),
            )
