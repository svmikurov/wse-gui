"""Defines mixins for page components to control top bar containers."""

from typing import Generic, TypeVar

from wse.core import NavID
from wse.feature.interfaces.iobserver import SubjectABC
from wse.ui.base.abc import NavigateABC

from .itop_bar import (
    TopBarViewMixinProto,
)

TopBarViewT = TypeVar('TopBarViewT', bound=TopBarViewMixinProto)


class TopBarModelMixin:
    """Mixin providing top bar features for page model."""

    _subject: SubjectABC

    def _notify_balance_updated(self, value: str) -> None:
        """Notify than balance updated."""
        self._subject.notify('balance_update', value=value)


class TopBarControllerMixin(Generic[TopBarViewT]):
    """Mixin providing top bar features for page controller."""

    _view: TopBarViewT

    def balance_update(self, value: str) -> None:
        """Handle balance update event notification."""
        self._view.update_balance(value)


class TopBarNavigationViewMixin:
    """Mixin providing navigation notifications for View.

    Add View to observers of TopBar.
    """

    _state: NavigateABC

    def navigate(self, nav_id: NavID) -> None:
        """Navigate."""
        self._state.navigate(nav_id)
