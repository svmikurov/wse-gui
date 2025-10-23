"""Foreign words study ViewModel."""

from dataclasses import dataclass

from injector import inject

from wse.ui.base.navigate.mixin import NavigateStateMixin

from . import StudyForeignViewModelABC


@inject
@dataclass
class StudyForeignViewModel(
    NavigateStateMixin,
    StudyForeignViewModelABC,
):
    """Foreign words study ViewModel."""
