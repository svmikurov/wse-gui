"""Abstract base class for Exercise control container."""

from abc import ABC

from wse.ui.base.container import ContainerABC, StyleABC
from wse.ui.base.content import ContentABC, GetContentABC


class ControlContainerABC(
    ContainerABC,
    GetContentABC,
    StyleABC,
    ABC,
):
    """ABC for Exercise control container."""

    _content: ContentABC

    def __post_init__(self) -> None:
        """Construct the container."""
        self._create_ui()
        self._populate_content()
        self._apply_styles()
