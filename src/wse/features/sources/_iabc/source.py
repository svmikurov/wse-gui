"""Defines protocol for source interface."""

from abc import ABC, abstractmethod
from typing import Protocol

from typing_extensions import override

from wse.features import ListenerT


class ISource(Protocol[ListenerT]):
    """A base class for data sources.

    Provides an implementation of data notifications.
    """

    _listeners: list[ListenerT] = []

    @property
    def listeners(self) -> list[ListenerT]:
        """The listeners of this data source.

        :returns: A list of objects that are listening to this data
            source.
        """

    def add_listener(self, listener: ListenerT) -> None:
        """Add a new listener to this data source.

        If the listener is already registered on this data source,
        the request to add is ignored.

        :param listener: The listener to add
        """

    def remove_listener(self, listener: ListenerT) -> None:
        """Remove a listener from this data source.

        :param listener: The listener to remove.
        """

    def notify(self, notification: str, **kwargs: object) -> None:
        """Notify all listeners an event has occurred.

        :param notification: The notification to emit.
        :param kwargs: The data associated with the notification.
        """


class SourceABC(
    ABC,
    ISource[ListenerT],
):
    """A base class for data sources.

    Provides an implementation of data notifications.
    """

    _listeners: list[ListenerT] = []

    @property
    @abstractmethod
    @override
    def listeners(self) -> list[ListenerT]:
        """The listeners of this data source.

        :returns: A list of objects that are listening to this data
            source.
        """

    @abstractmethod
    @override
    def add_listener(self, listener: ListenerT) -> None:
        """Add a new listener to this data source.

        If the listener is already registered on this data source,
        the request to add is ignored.

        :param listener: The listener to add
        """

    @abstractmethod
    @override
    def remove_listener(self, listener: ListenerT) -> None:
        """Remove a listener from this data source.

        :param listener: The listener to remove.
        """

    @abstractmethod
    @override
    def notify(self, notification: str, **kwargs: object) -> None:
        """Notify all listeners an event has occurred.

        :param notification: The notification to emit.
        :param kwargs: The data associated with the notification.
        """


class BaseSource(
    SourceABC[ListenerT],
):
    """A base class for data sources.

    Provides an implementation of data notifications.
    """

    def __init__(self) -> None:
        """Construct the source."""
        self._listeners: list[ListenerT] = []

    @property
    @override
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

    @override
    def remove_listener(self, listener: ListenerT) -> None:
        """Remove a listener from this data source.

        :param listener: The listener to remove.
        """
        self._listeners.remove(listener)

    @override
    def notify(self, notification: str, **kwargs: object) -> None:
        """Notify all listeners an event has occurred.

        :param notification: The notification to emit.
        :param kwargs: The data associated with the notification.
        """
        for listener in self._listeners:
            try:
                method = getattr(listener, notification)
            except AttributeError:
                method = None

            if method:
                method(**kwargs)
