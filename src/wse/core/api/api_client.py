"""API client."""

from wse.interfaces.iapi import IApiClient


class ApiClient(IApiClient):
    """API client."""

    def __init__(self) -> None:
        """Construct the client."""
