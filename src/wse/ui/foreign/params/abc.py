"""Abstract base classes for Word study params screen."""

from abc import ABC
from typing import Any

from wse.feature.observer.generic import ObserverManagerGenABC
from wse.ui.base.navigate import (
    CreateNavButtonABC,
    NavigateABC,
    OnCloseABC,
)
from wse.ui.base.view import ViewABC


class WordStudyParamsViewModelABC(
    ObserverManagerGenABC[Any],
    NavigateABC,
    ABC,
):
    """ABC for Word study params ViewModel."""


class WordStudyParamsViewABC(
    CreateNavButtonABC,
    OnCloseABC,
    ViewABC,
    ABC,
):
    """ABC for Word study params View."""
