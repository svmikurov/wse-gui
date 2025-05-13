"""Defines exercise provider switcher."""

import logging

from wse.features.shared.enums.exercises import Exercises
from wse.interfaces.iexercise import IExercise

logger = logging.getLogger(__name__)

DEFAULT_MATH_EXERCISE = Exercises.SUBTRACTION


class ExerciseSwitcher:
    """Controlling switching between exercise types."""

    def __init__(
        self,
        _exercises: dict[Exercises, IExercise],
    ) -> None:
        """Construct the switcher."""
        self._exercises = _exercises
        self._current_exercise_name = DEFAULT_MATH_EXERCISE

    def switch(self, exercise_name: Exercises) -> None:
        """Switch exercise."""
        try:
            if exercise_name not in self._exercises:
                raise ValueError(
                    f'Unknown exercise: {self._current_exercise_name}'
                )
        except ValueError as error:
            logger.exception(error)

        self._current_exercise_name = exercise_name
        logger.debug(
            f'Switched to the exercise "{self._current_exercise_name}"'
        )

    @property
    def current_exercise(self) -> IExercise:
        """Get current exercise dependency."""
        return self._exercises[self._current_exercise_name]

    @property
    def current_exercise_name(self) -> Exercises:
        """Get current exercise name."""
        return self._current_exercise_name

    @property
    def exercises(self) -> dict[Exercises, IExercise]:
        """Get available exercises mapping."""
        return self._exercises
