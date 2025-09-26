"""Defines selection data sources."""

from wse_exercises.base.enums import ExerciseEnum

from wse.feature.source.selection import Entry, SelectSourceABC
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


class ExerciseSelectSourceWrap(SelectSourceABC[ExerciseEnum]):
    """Exercise selection data source wrap."""

    def _create_entry(self, value: ExerciseEnum) -> ExerciseEntry:
        """Create entry."""
        return ExerciseEntry(value)
