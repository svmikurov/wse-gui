"""Defines mixins for page components to control top bar containers."""

from typing import Generic, TypeVar, no_type_check

from wse.feature.observer import SubjectABC

from .itop_bar import (
    TopBarViewMixinABC,
)

TopBarViewT = TypeVar('TopBarViewT', bound=TopBarViewMixinABC)


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


class BalanceUpdatedMixin:
    """Mixin providing observer method on update balance event."""

    @no_type_check
    def balance_updated(self, balance: str) -> None:
        """Handle the 'balance updated' event of User source."""
        self._update_data(balance=balance)
        self.notify('balance_updated', balance=balance)
