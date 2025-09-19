"""Abstract base classes for Home screen UI layer."""

from abc import ABC

from wse.ui.base.abc.navigate import CreateNavButtonABC, NavigateABC
from wse.ui.base.abc.utils import OnCloseABC
from wse.ui.base.abc.view import ViewABC

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
