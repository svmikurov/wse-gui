"""Defines subject of Observer pattern."""

from ..interfaces import IObserver


class Subject:
    """Subject of Observer patten."""

    def __init__(self) -> None:
        """Construct the subject."""
        self._observers: list[IObserver] = []

    def add_observer(self, observer: IObserver) -> None:
        """Add a new observer to this subject."""
        self._observers.append(observer)

    def notify(self, notification: str, **kwargs: object) -> None:
        """Notify all observers an event has occurred."""
        for observer in self._observers:
            try:
                method = getattr(observer, notification)
            except AttributeError:
                method = None

            if method:
                method(**kwargs)
