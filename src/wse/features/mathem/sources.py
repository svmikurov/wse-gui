"""Defines mathematical package source management."""

from typing import Callable

from toga.sources import Listener, Source

from wse.features.shared.enums.exercises import Exercises


class SourceHub(Source, Listener):
    """Hub to pass notifications from model to widget."""

    def __init__(self) -> None:
        """Construct the source."""
        super().__init__()
        self._collection: list = []

    def __len__(self) -> int:
        """Gen collection length."""
        return len(self._collection)

    def __getitem__(self, index: int) -> object:
        """Get item from collection by index."""
        return self._collection[index]

    def index(self, entry: object) -> int:
        """Return entry index in collection."""
        return self._collection.index(entry)

    def change(self, item: object) -> object:
        """Notify that change has occurred in an item."""

    def insert(self, index: int, item: object) -> None:
        """Notify that  item has been added to the data source."""
        self._collection.append(item)
        self.notify('insert', index=index, item=item)

    def remove(self, index: int, item: object) -> None:
        """Notify that item has been removed from the data source."""
        self.notify('remove', index=index, item=item)

    def clear(self) -> None:
        """All items have been removed from the data source."""
        self.notify('clear')

    @property
    def collection(self) -> list[object]:
        """Get source collection."""
        return self._collection


class Exercise:
    """Data-Transfer-Object representation of Exercise."""

    def __init__(
        self,
        name: Exercises,
        instance: Callable,
    ) -> None:
        """Construct the DTO."""
        self.name = name
        self.instance = instance


class ExerciseSource(Source):
    """Source representation of Exercises."""

    def __init__(self) -> None:
        """Construct the source."""
        super().__init__()
        self._exercises: list[Exercise] = []

    def __getitem__(self, index: int) -> object:
        """Get item from collection by index."""
        return self._exercises[index]

    def index(self, entry: Exercise) -> int:
        """Return entry index in collection."""
        return self._exercises.index(entry)

    def add(self, name: Exercises, instance: Callable) -> None:
        """Add coloros."""
        exercise = Exercise(name, instance)
        self._exercises.append(exercise)
        self.notify(
            'insert',
            index=self._exercises.index(exercise),
            item=exercise,
        )

    def clear(self) -> None:
        """All items have been removed from the data source."""
        self._exercises = []
        self.notify('clear')

    @property
    def has_exercises(self) -> bool:
        """Is exercise collections has Data-Transfer-Object."""
        return bool(self._exercises)

    def find(self, name: Exercises, accessor: str = 'name') -> Exercise | None:
        """Find a DTO of exercise by its name."""
        error = f'No exercise matching {name!r} in exercises'

        for exercise in self._exercises:
            if getattr(exercise, accessor) == name:
                return exercise

        raise ValueError(error)

    def add_listener(self, listener: Listener) -> None:
        """Add a new listener to this data source.

        If the listener is already registered on this data source, the
        request to add is ignored.

        :param listener: The listener to add
        """
        if listener not in self._listeners:
            self._listeners.append(listener)
