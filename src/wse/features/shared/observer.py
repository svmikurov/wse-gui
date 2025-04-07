"""Observer pattern module."""

from toga.sources import Listener, Source

from wse.interface.ifeatures import ISubject


class AsyncNotifyMixin:
    """A mixin for async notification."""

    _listeners: list[Listener]

    async def notify_async(self, notification: str, **kwargs: object) -> None:
        """Notify all listeners an event has occurred."""
        for listener in self._listeners:
            try:
                method = getattr(listener, notification)
            except AttributeError:
                method = None

            if method:
                await method(**kwargs)


class Subject(AsyncNotifyMixin, Source):
    """An observable object in the Observer pattern.

    Notifies subscribed listeners (observers) when its state changes.
    """
