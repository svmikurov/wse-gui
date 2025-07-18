"""Defines account state inspector."""

from typing import Any

from ._iabc.inspector import BaseAccountStateInspector


class AccountStateInspector(BaseAccountStateInspector):
    """Account state inspector."""

    def inspect(self, data: dict[str, Any]) -> None:
        """Inspect the response data."""
        print(f"{data.get('meta') = }")
