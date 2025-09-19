"""Defines data source."""

from typing import Generic

from toga.sources import Listener
from typing_extensions import override

from wse.feature import ListenerT
from wse.feature.interfaces.types import EntryNotifyT, EntryT, NotifyT

from .abc import BaseSource


# TODO: Fix type ignore
class SourceGen(
    BaseSource[ListenerT, NotifyT],
):
    """Data sources.

    Provides an implementation of data notifications.
    """

    def __init__(self) -> None:
        """Construct the source."""
        super().__init__()
        self._listeners: list[ListenerT] = []

    @property
    def listeners(self) -> list[ListenerT]:
        """The listeners of this data source.

        :returns: A list of objects that are listening to this data
            source.
        """
        return self._listeners

    @override
    def add_listener(self, listener: ListenerT) -> None:
        """Add a new listener to this data source.

        If the listener is already registered on this data source,
        the request to add is ignored.

        :param listener: The listener to add
        """
        if listener not in self._listeners:
            self._listeners.append(listener)

    def remove_listener(self, listener: ListenerT) -> None:
        """Remove a listener from this data source.

        :param listener: The listener to remove.
        """
        self._listeners.remove(listener)

    def notify(self, notification: NotifyT, **kwargs: object) -> None:
        """Notify all listeners an event has occurred.

        :param notification: The notification to emit.
        :param kwargs: The data associated with the notification.
        """
        for listener in self._listeners:
            try:
                method = getattr(listener, str(notification))
            except AttributeError:
                method = None

            if method:
                method(**kwargs)


class EntrySourceGen(
    SourceGen[Listener, EntryNotifyT],
    Generic[EntryT],
):
    """Entry source with typed notifications."""

    def __init__(self) -> None:
        """Construct the source."""
        super().__init__()
        self._entries: list[EntryT] = []

    def add(self, entry: EntryT) -> None:
        """Add entry."""
        self._entries.append(entry)
        self.notify('insert', index=self._entries.index(entry), item=entry)

    def remove(self, entry: EntryT) -> None:
        """Remove entry."""
        index = self.index(entry)
        self.notify('remove', index=index, item=entry)

    def clear(self) -> None:
        """Clear all entries."""
        self._entries = []
        self.notify('clear')

    def index(self, entry: EntryT) -> int:
        """Get index of term."""
        return self._entries.index(entry)

    def __len__(self) -> int:
        """Get entries length."""
        return len(self._entries)

    def __getitem__(self, index: int) -> EntryT:
        """Get entry via index."""
        return self._entries[index]
