"""Abstract base class for label listener container via accessors."""

from abc import ABC
from dataclasses import dataclass

from wse.feature.observer.abc import AccessorABC, AccessorNotifyChangeABC
from wse.ui.base.container.abc import ContainerABC


@dataclass
class LabelAccessorContainerABC(
    ContainerABC,
    AccessorABC,
    AccessorNotifyChangeABC,
    ABC,
):
    """ABC for label listener container via accessors."""

    def __post_init__(self) -> None:
        """Construct the accessor."""
        self._create_ui()
        self._populate_content()
        self._check_accessors()
