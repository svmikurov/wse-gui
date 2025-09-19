"""Abstract Base Classes for Presentation container."""

from abc import ABC, abstractmethod
from typing import Literal

from wse.ui.base.abc.container import AddContentABC

PresentationNotifyT = Literal[
    'change_case',
    'change_text',
]


class PresentationListenerABC(ABC):
    """Abstract Base Class for Presentation listener."""

    @abstractmethod
    def change_case(self, value: str) -> None:
        """Change case."""

    @abstractmethod
    def change_text(self, value: str) -> None:
        """Change text."""


class PresentationContainerABC(
    PresentationListenerABC,
    AddContentABC,
    ABC,
):
    """ABC for Presentation container."""
