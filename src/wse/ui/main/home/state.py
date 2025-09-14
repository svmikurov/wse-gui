"""Home screen state."""

from dataclasses import dataclass

from injector import inject

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
