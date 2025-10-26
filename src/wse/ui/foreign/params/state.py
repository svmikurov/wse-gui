"""Word study params state."""

from dataclasses import dataclass
from typing import Any

from injector import inject

from wse.feature.observer.mixins import NotifyAccessorGen, ObserverManagerGen
from wse.ui.base.navigate.mixin import NavigateStateMixin

from . import WordStudyParamsViewModelABC


@inject
@dataclass
class WordStudyParamsViewModel(
    NavigateStateMixin,
    ObserverManagerGen[Any],
    NotifyAccessorGen[Any, Any],
    WordStudyParamsViewModelABC,
):
    """Word study params ViewModel."""
