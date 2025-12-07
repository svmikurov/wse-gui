"""API exceptions."""


class ServerNotAvailableError(Exception):
    """Raised when the server is unavailable."""


class NoResponseDataError(Exception):
    """Raised when the server was not return data."""
