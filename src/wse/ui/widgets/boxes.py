"""Defines styled toga Box widgets."""

import toga


# TODO: Fix type ignore
class FlexColumn(toga.Box):
    """Flex column box."""

    def __init__(self, *args: object, **kwargs: object) -> None:
        """Construct the box."""
        super().__init__(*args, direction='column', flex=1, **kwargs)  # type: ignore[arg-type]


# TODO: Fix type ignore
class FlexRow(toga.Box):
    """Flex row box."""

    def __init__(self, *args: object, **kwargs: object) -> None:
        """Construct the box."""
        super().__init__(*args, flex=1, **kwargs)  # type: ignore[arg-type]
