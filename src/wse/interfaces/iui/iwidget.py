"""Widget Interface Protocols for Type-Safe UI Components."""

from typing import Iterable, Protocol

# fmt: off


class IValueWidget(Protocol):
    """Protocol defining a widget with a value property."""
    value: str

class IItemsWidget(Protocol):
    """Protocol defining a widget with an items collection."""
    items: Iterable

class IValueItemsWidget(IValueWidget, IItemsWidget, Protocol):
    """Protocol combining value and items capabilities."""
