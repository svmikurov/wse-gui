"""Abstract base class for Index Foreign View."""

from abc import ABC

from wse.ui.base.navigate import CreateNavButtonABC, NavigateABC, OnCloseABC
from wse.ui.base.view import ViewABC


class IndexForeignViewModelABC(
    NavigateABC,
    ABC,
):
    """ABC for Index Foreign ViewModel."""


class IndexForeignViewABC(
    CreateNavButtonABC,
    OnCloseABC,
    ViewABC,
    ABC,
):
    """ABC for Index Foreign View."""
