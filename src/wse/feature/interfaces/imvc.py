"""Defines protocols for MVC model components interface."""

from typing import Protocol, TypeVar

from wse.config.layout import StyleConfig, ThemeConfig

from .icontainer import Containerizable, Localizable, Stylizable
from .icontent import ContentProto
from .iobserver import AddObserverProto

T_contra = TypeVar('T_contra', contravariant=True)


# Model


class ModelProto(
    AddObserverProto,
    Protocol,
):
    """Protocol for screen model interface."""


# View


class ViewProto(
    AddObserverProto,
    Containerizable,
    Localizable,
    Stylizable[StyleConfig, ThemeConfig],
    Protocol,
):
    """Protocol for screen view interface."""


class NavigableView(Protocol[T_contra]):
    """Protocol for navigable view interface."""

    @property
    def content(self) -> ContentProto:
        """Get screen content."""

    def on_open(self, **kwargs: T_contra) -> None:
        """Call methods when screen opens."""

    def on_close(self) -> None:
        """Call methods before close the screen."""
