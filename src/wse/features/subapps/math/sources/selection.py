"""Defines selection data sources."""

from wse_exercises.core.mathem.enums import Exercises

from wse.features.sources.selection import BaseSelectionSource, Entry
from wse.utils.i18n import exercise_


class ExerciseEntry(Entry[Exercises]):
    """Exercise DTO to entry to selection widget."""

    def __init__(self, entry: Exercises) -> None:
        """Construct the DTO."""
        super().__init__(entry)
        self.accessor = self._localize(entry.value)

    @staticmethod
    def _localize(text: str) -> str:
        """Localize exercise name for display."""
        return exercise_(text)


class ExerciseSelectionSource(BaseSelectionSource[Exercises]):
    """Exercise selection data source."""

    def _create_entry_dto(self, entry: Exercises) -> ExerciseEntry:
        """Create DTO of entry."""
        return ExerciseEntry(entry)
