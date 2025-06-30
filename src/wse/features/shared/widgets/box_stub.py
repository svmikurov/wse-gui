"""Defines flexible box to stub in content."""

import toga
from toga.style import Pack


class FlexColumnStub(toga.Box):  # type: ignore[misc]
    """Flexible column direction box.

    For example:

        class SomeView(...):

            _flex_stub: Callable[[], IFlexColumnStub]

            def _populate_content(self) -> None:
                self.content.add(
                    ...,
                    self._flex_stub(),
                    ...,
                )

    """

    def __init__(self) -> None:
        """Construct the box."""
        style = Pack(
            flex=1,
        )
        super().__init__(style=style)
