"""Abstract base class for Info container."""

from abc import ABC
from typing import Any

from wse.feature import observer
from wse.ui.base import container, content


class InfoContainerABC(
    observer.AccessorABC,
    observer.ChangeObserverABC[Any],
    content.GetContentABC,
    container.ContainerABC,
    container.StyleABC,
    ABC,
):
    """ABC for Info container."""

    _content: content.ContentABC

    def __post_init__(self) -> None:
        """Construct the container."""
        self._create_ui()
        self._populate_content()
        self._apply_styles()
