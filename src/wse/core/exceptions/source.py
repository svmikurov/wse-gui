"""Source as subject of Observer pattern exceptions."""


class NotEmplementedAccessorError(Exception):
    """Raised when not emplemented accessor by listener."""

    def __init__(
        self, accessor: str, obj: object, detail: bool = False
    ) -> None:
        """Construct the exception."""
        header = (
            'Not emplemented accessor for source listener of Observer pattern'
        )
        description = (
            f'Description: The {obj} listener have no '
            f"implementation for '{accessor}' accessor\n"
        )
        solution = (
            f"Solution: Add '{accessor}' accessor as attribute to {obj}\n"
        )
        example = (
            f'For example:\n\n'
            f'    def _create_ui(self) -> None:\n'
            f'        ...\n'
            f"        self._{accessor} = toga.Label('')\n"
            f'        ...\n\n'
            f'    def _populate_content(self) -> None:\n'
            f'        self._content.add(\n'
            f'            ...\n'
            f"            self._{accessor} = toga.Label('')\n"
            f'            ...\n'
            f'        )\n'
        )
        message = f'{header}\n\n{description}\n\n{solution}\n\n{example}\n'
        super().__init__(message)
