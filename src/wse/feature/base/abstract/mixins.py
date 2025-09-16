"""Abstract base classes for mixins."""

from abc import ABC, abstractmethod

from wse.feature.interfaces.icontent import ContentProto


class GetContentABC(ABC):
    """ABC to provide content."""

    @property
    @abstractmethod
    def content(self) -> ContentProto:
        """Get page content."""
