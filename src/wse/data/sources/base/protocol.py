"""Defines protocol for source interface."""

from typing import Protocol, TypeVar

ListenerT = TypeVar('ListenerT')
NotifyT_contra = TypeVar('NotifyT_contra', contravariant=True)


class SourceProto(Protocol[ListenerT, NotifyT_contra]):
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

    def notify(self, notification: NotifyT_contra, **kwargs: object) -> None:
        """Notify all listeners an event has occurred.

        :param notification: The notification to emit.
        :param kwargs: The data associated with the notification.
        """
