"""Defines a mixin for async notification."""

from toga.sources import Listener


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
