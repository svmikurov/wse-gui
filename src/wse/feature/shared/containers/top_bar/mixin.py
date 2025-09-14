"""Defines mixins for page components to control top bar containers."""

from typing import Generic, TypeVar

from wse.feature.interfaces.iobserver import Observable

from .itop_bar import (
    TopBarViewMixinProto,
)

TopBarViewT = TypeVar('TopBarViewT', bound=TopBarViewMixinProto)


class TopBarModelMixin:
    """Mixin providing top bar features for page model."""

    _subject: Observable

    def _notify_balance_updated(self, value: str) -> None:
        """Notify than balance updated."""
        self._subject.notify('balance_update', value=value)


class TopBarControllerMixin(Generic[TopBarViewT]):
    """Mixin providing top bar features for page controller."""

    _view: TopBarViewT

    def balance_update(self, value: str) -> None:
        """Handle balance update event notification."""
        self._view.update_balance(value)
