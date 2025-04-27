"""Observer pattern module."""

from toga.sources import Listener, Source


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


class ValueListenerMixin:
    """Listener methods mixin."""

    value: str

    def change(self, value: str) -> None:
        """Update text widget value."""
        self.value = value

    def clean(self) -> None:
        """Clear the value of the text widget."""
        self.value = ''


class TextListenerMixin:
    """Listener methods mixin."""

    text: str

    def change(self, value: str) -> None:
        """Update text widget value."""
        self.text = value

    def clean(self) -> None:
        """Clear the value of the text widget."""
        self.text = ''
