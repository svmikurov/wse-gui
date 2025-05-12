"""Defines protocol interfaces for DI container."""


# ruff: noqa: D101, D102, D204, E301, E302
# fmt: off


# class IExerciseSwitcher(Protocol):
#     """Exercise provider switcher."""
#     def switch(self, exercise_name: str) -> None:
#         """Set exercise type."""
#     @property
#     def current_exercise_name(self) -> Exercises:
#         """Get current exercise name."""
#     @property
#     def current_exercise(self) -> ITask:
#         """Return current exercise."""
#     @property
#     def exercises(self) -> dict[Exercises, Callable]: ...
