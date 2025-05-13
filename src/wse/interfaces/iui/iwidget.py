"""Widget Interface Protocols for Type-Safe UI Components."""

from typing import Iterable, Protocol

# ruff: noqa: D101, D102, D204, E301, E302
# fmt: off


class IValueWidget(Protocol):
    """Protocol defining a widget with a value property."""
    value: str

class IItemsWidget(Protocol):
    """Protocol defining a widget with an items collection."""
    items: Iterable

class IValueItemsWidget(IValueWidget, IItemsWidget, Protocol):
    """Protocol combining value and items capabilities."""
