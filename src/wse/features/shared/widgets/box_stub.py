"""Defines flexible box to stub in content."""

import toga
from toga.style import Pack


class FlexColumnStub(toga.Box):  # type: ignore[misc]
    """Flexible column direction box."""

    def __init__(self) -> None:
        """Construct the box."""
        style = Pack(
            flex=1,
        )
        super().__init__(style=style)
