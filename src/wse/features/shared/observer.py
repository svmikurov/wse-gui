"""Observer pattern module."""

from typing import Callable, Iterable

from toga.sources import Listener, Source

from wse.features.shared.enums import FieldID
from wse.features.shared.enums.notify_id import NotifyID


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


class NotifyByIDMixin:
    """Mixin for standardized notification by IDs."""

    notify: Callable

    def notify_with_id(
        self,
        notify_id: NotifyID,
        field_id: FieldID | None = None,
        items: Iterable | None = None,
        value: str = '',
    ) -> None:
        """Send structured notification with IDs and optional data."""
        self.notify(
            'match_notify',
            notify_id=notify_id,
            field_id=field_id,
            items=items,
            value=value,
        )


class Subject(AsyncNotifyMixin, Source):
    """An observable object in the Observer pattern."""


class IDSubject(NotifyByIDMixin, Subject):
    """Subject with notification by ID."""


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
