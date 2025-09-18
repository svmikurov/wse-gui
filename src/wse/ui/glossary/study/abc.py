"""Abstract Base Classes for Terms study screen."""

from abc import ABC

from wse.ui.base.abc import NavigateABC, ViewABC


class TermsStudyViewModelABC(
    NavigateABC,
):
    """ABC for Terms study ViewModel."""


class TermsStudyViewABC(
    ViewABC,
    ABC,
):
    """ABC for Terms study View."""
