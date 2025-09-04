"""Defines selection data sources."""

from wse_exercises.base.enums import ExerciseEnum

from wse.feature.sources.selection import BaseSelectSource, Entry
from wse.utils.i18n import exercise_


class ExerciseEntry(Entry[ExerciseEnum]):
    """Exercise entry of selection widget."""

    def __init__(self, entry: ExerciseEnum) -> None:
        """Construct the entry."""
        super().__init__(entry)
        self.accessor = self._localize(entry.value)

    @staticmethod
    def _localize(text: str) -> str:
        """Localize exercise name for display."""
        return exercise_(text)


class ExerciseSelectSource(BaseSelectSource[ExerciseEnum]):
    """Exercise selection data source."""

    def _create_entry(self, value: ExerciseEnum) -> ExerciseEntry:
        """Create entry."""
        return ExerciseEntry(value)
