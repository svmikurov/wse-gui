"""Word study params state."""

from dataclasses import dataclass, replace
from typing import Any

from injector import inject

from wse.feature.observer.mixins import NotifyAccessorGen, ObserverManagerGen
from wse.ui.base.navigate.mixin import NavigateStateMixin
from wse.ui.containers.params.entity import NamedEntity

from . import WordStudyParamsViewModelABC


@dataclass
class WordStudyData:
    """Word study data."""

    mark_select: NamedEntity | None = None
    category_select: NamedEntity | None = None


@inject
@dataclass
class WordStudyParamsViewModel(
    NavigateStateMixin,
    ObserverManagerGen[Any],
    NotifyAccessorGen[Any, Any],
    WordStudyParamsViewModelABC,
):
    """Word study params ViewModel."""

    _data: WordStudyData

    def update(self, accessor: str, value: object) -> None:
        """Update state."""
        self._update_data({accessor: value})

    # TODO: Fix type ignore
    def _update_data(self, data: dict[str, object]) -> None:
        self._data = replace(self._data, **data)  # type: ignore[arg-type]
