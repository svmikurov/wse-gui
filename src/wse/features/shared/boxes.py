"""Defines styled toga Box widgets."""

import toga


class FlexColumn(toga.Box):  # type: ignore[misc]
    """Flex column box."""

    def __init__(self, *args: object, **kwargs: object) -> None:
        """Construct the box."""
        super().__init__(*args, direction='column', flex=1, **kwargs)


class FlexRow(toga.Box):  # type: ignore[misc]
    """Flex row box."""

    def __init__(self, *args: object, **kwargs: object) -> None:
        """Construct the box."""
        super().__init__(*args, flex=1, **kwargs)
