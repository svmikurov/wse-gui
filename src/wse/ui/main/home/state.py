"""Home screen state."""

from dataclasses import dataclass

from injector import inject
from typing_extensions import override

from wse.core.interfaces import Navigable

from ...base.mixin import NavigateMixin
from .abc import HomeViewModelABC


@inject
@dataclass
class HomeViewModel(
    NavigateMixin,
    HomeViewModelABC,
):
    """Home screen ViewModel."""

    _navigator: Navigable

    @override
    def on_close(self) -> None:
        """Call methods before close the screen."""
        pass
