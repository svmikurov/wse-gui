"""Defines protocols for MVC model components interface."""

from typing import Protocol, TypeVar

from wse.config.layout import StyleConfig, ThemeConfig

from .icontainer import Containerizable, Localizable, Stylizable
from .icontent import GetContentProto
from .iobserver import AddObserverProto

T_contra = TypeVar('T_contra', contravariant=True)


# Model


class ModelProto(
    AddObserverProto,
    Protocol,
):
    """Protocol for page model interface."""


# View


class ViewProto(
    AddObserverProto,
    Containerizable,
    Localizable,
    Stylizable[StyleConfig, ThemeConfig],
    Protocol,
):
    """Protocol for page view interface."""


# Controller


class ControllerProto(
    GetContentProto,
    Protocol,
):
    """Protocol for controller interface."""


class PageControllerProto(
    ControllerProto,
    Protocol[T_contra],
):
    """Protocol for page controller interface."""

    def on_open(self, **kwargs: T_contra) -> None:
        """Call methods when page opens."""
