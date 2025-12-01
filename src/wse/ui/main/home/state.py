"""Home screen state."""

from dataclasses import dataclass

from injector import inject
from typing_extensions import override

from wse.core.interfaces import Navigable
from wse.ui.base.navigate.mixin import NavigateStateMixin

from .abc import HomeViewModelABC


@inject
@dataclass
class HomeViewModel(
    NavigateStateMixin,
    HomeViewModelABC,
):
    """Home screen ViewModel."""

    _navigator: Navigable

    @override
    def on_close(self) -> None:
        """Call methods before close the screen."""
        pass
