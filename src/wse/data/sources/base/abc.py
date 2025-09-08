"""Abstract base class for Source."""

from abc import ABC, abstractmethod
from typing import Generic

from .protocol import ListenerT, NotifyT_contra


class BaseSource(
    ABC,
    Generic[ListenerT, NotifyT_contra],
):
    """A base class for data sources.

    Provides an implementation of data notifications.
    """

    _listeners: list[ListenerT] = []

    @property
    @abstractmethod
    def listeners(self) -> list[ListenerT]:
        """The listeners of this data source.

        :returns: A list of objects that are listening to this data
            source.
        """

    @abstractmethod
    def add_listener(self, listener: ListenerT) -> None:
        """Add a new listener to this data source.

        If the listener is already registered on this data source,
        the request to add is ignored.

        :param listener: The listener to add
        """

    @abstractmethod
    def remove_listener(self, listener: ListenerT) -> None:
        """Remove a listener from this data source.

        :param listener: The listener to remove.
        """

    @abstractmethod
    def notify(self, notification: NotifyT_contra, **kwargs: object) -> None:
        """Notify all listeners an event has occurred.

        :param notification: The notification to emit.
        :param kwargs: The data associated with the notification.
        """
