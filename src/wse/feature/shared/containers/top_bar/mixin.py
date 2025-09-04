"""Defines mixins for page components to control top bar containers."""

from dataclasses import dataclass
from typing import Generic, TypeVar

from injector import inject

from wse.feature.base.mixins import NotifyNavigateMixin
from wse.feature.interfaces.iobserver import Observable

from .itop_bar import (
    TopBarControllerProto,
    TopBarViewMixinProto,
)

TopBarViewT = TypeVar('TopBarViewT', bound=TopBarViewMixinProto)


class TopBarModelMixin:
    """Mixin providing top bar features for page model."""

    _subject: Observable

    def _notify_balance_updated(self, value: str) -> None:
        """Notify than balance updated."""
        self._subject.notify('balance_update', value=value)


@inject
@dataclass
class TopBarViewMixin(
    NotifyNavigateMixin,
):
    """Mixin providing top bar features for page view.

    Add top bar content to view content.

    For example:

        def _populate_content(self) -> None:
            self.content.add(
                self._top_bar.content,
                ...,
            )
    """

    _top_bar: TopBarControllerProto

    def __post_init__(self) -> None:
        """Construct the view."""
        super().__post_init__()  # type: ignore[misc]
        self._top_bar.add_observer(self)


class TopBarControllerMixin(Generic[TopBarViewT]):
    """Mixin providing top bar features for page controller."""

    _view: TopBarViewT

    def balance_update(self, value: str) -> None:
        """Handle balance update event notification."""
        self._view.update_balance(value)
