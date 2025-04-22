"""Defines base classes of page context."""


class Context(dict):
    """Page model data to render into view."""


class HomeContext:
    """Home page context."""

    info_panel: str

    @property
    def info_panel(self) -> str:
        """Info panel context."""
        return 'Hello!'
