"""Application exceptions."""


class ContentError(Exception):
    """Raised when unable to get or process page content."""


class NavigateError(Exception):
    """Raised when navigation between pages fails."""
