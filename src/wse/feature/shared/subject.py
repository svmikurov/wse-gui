"""Defines subject of Observer pattern."""

from ..interfaces.iobserver import ObserverProto, SubjectABC


class Subject(SubjectABC):
    """Subject of Observer patten."""

    def __init__(self) -> None:
        """Construct the subject."""
        self._observers: list[ObserverProto] = []

    @property
    def observers(self) -> list[ObserverProto]:
        """Get observers."""
        return self._observers

    def add_observer(self, observer: ObserverProto) -> None:
        """Add a new observer to this subject."""
        self._observers.append(observer)

    def remove_observer(self, observer: ObserverProto) -> None:
        """Remove an observer from this subject."""
        self._observers.remove(observer)

    def notify(self, notification: str, **kwargs: object) -> None:
        """Notify all observers an event has occurred."""
        for observer in self._observers:
            try:
                method = getattr(observer, notification)
            except AttributeError:
                method = None

            if method:
                method(**kwargs)
