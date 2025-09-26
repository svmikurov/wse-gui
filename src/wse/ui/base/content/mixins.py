"""Mixins providing Content feature."""

from dataclasses import dataclass

from .abc import ContentABC


@dataclass
class GetContentMixin:
    """Mixin to provide content."""

    _content: ContentABC

    @property
    def content(self) -> ContentABC:
        """Get page content."""
        return self._content
