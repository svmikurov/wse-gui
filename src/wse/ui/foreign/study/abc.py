"""Abstract base classes for Foreign words study screen."""

from abc import ABC

from wse.ui.base.navigate import NavigateABC, OnCloseABC
from wse.ui.base.view import ViewABC


class StudyForeignViewModelABC(
    NavigateABC,
    ABC,
):
    """ABC for Foreign words study ViewModel."""


class StudyForeignViewABC(
    OnCloseABC,
    ViewABC,
    ABC,
):
    """ABC for Foreign words study View."""
