"""Abstract base classes for Home screen UI layer."""

from abc import ABC

from wse.feature.base import ViewABC
from wse.feature.base.container import CreateNavButtonABC
from wse.ui.base.abc import NavigateABC

# ViewModel


class HomeViewModelABC(
    NavigateABC,
    ABC,
):
    """ABC for Home screen ViewModel."""


# View


class HomeViewABC(
    CreateNavButtonABC,
    ViewABC,
    ABC,
):
    """ABC for Home screen View."""
