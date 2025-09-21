"""Abstract base class for Source."""

from abc import ABC, abstractmethod
from typing import Generic

from .protocol import AccessorT_contra, ListenerT, NotifyT_contra


class NotifyABC(
    ABC,
    Generic[NotifyT_contra],
):
    """ABC for notifications.

    Implements by Toga `toga` dependency and custom widgets.
    """

    @abstractmethod
    def notify(self, notification: NotifyT_contra, **kwargs: object) -> None:
        """Notify all listeners an event has occurred.

        :param notification: The notification to emit.
        :param kwargs: The data associated with the notification.
        """


class NotifyAccessorABC(
    ABC,
    Generic[NotifyT_contra, AccessorT_contra],
):
    """ABC for notifications with spcific accessors.

    Implements only by custom widgets.
    """

    @abstractmethod
    def notify(
        self,
        notification: NotifyT_contra,
        accessor: AccessorT_contra,
        **kwargs: object,
    ) -> None:
        """Notify all listeners an event has occurred.

        :param notification: The notification to emit.
        :param kwargs: The data associated with the notification.
        """


class ListenerManagementABC(
    ABC,
    Generic[ListenerT],
):
    """ABC for source listener management."""

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


class SourceABC(
    ListenerManagementABC[ListenerT],
    NotifyABC[NotifyT_contra],
    ABC,
    Generic[ListenerT, NotifyT_contra],
):
    """ABC for source.

    Implements by Toga `toga` dependency and custom widgets.
    """


class AccessorSourceABC(
    ListenerManagementABC[ListenerT],
    NotifyAccessorABC[NotifyT_contra, AccessorT_contra],
    ABC,
    Generic[ListenerT, NotifyT_contra, AccessorT_contra],
):
    """ABC for source.

    Implements only by custom widgets.
    """
