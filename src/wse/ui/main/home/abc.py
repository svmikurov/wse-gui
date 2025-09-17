"""Abstract base classes for Home screen UI layer."""

from abc import ABC

from wse.feature.base.container import CreateNavButtonABC
from wse.ui.base.abc import CloseScreenABC, NavigateABC, ViewABC

# ViewModel


class HomeViewModelABC(
    NavigateABC,
    CloseScreenABC,
    ABC,
):
    """ABC for Home screen ViewModel."""


# View


class HomeViewABC(
    CreateNavButtonABC,
    CloseScreenABC,
    ViewABC,
    ABC,
):
    """ABC for Home screen View."""
