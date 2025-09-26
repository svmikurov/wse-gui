"""Abstract base classes for Home screen UI layer."""

from abc import ABC

from wse.ui.base.navigate import CreateNavButtonABC, NavigateABC, OnCloseABC
from wse.ui.base.view.abc import ViewABC

# ViewModel


class HomeViewModelABC(
    NavigateABC,
    OnCloseABC,
    ABC,
):
    """ABC for Home screen ViewModel."""


# View


class HomeViewABC(
    CreateNavButtonABC,
    OnCloseABC,
    ViewABC,
    ABC,
):
    """ABC for Home screen View."""
