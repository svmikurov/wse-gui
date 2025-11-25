"""Word study Presentation parameters Screen test configuration."""

from unittest.mock import Mock

import pytest

from wse.config.layout import StyleConfig, ThemeConfig
from wse.ui.foreign.params import state, view


@pytest.fixture
def view_model() -> state.WordStudyParamsViewModel:
    """Provide Word study Presentation parameters ViewModel."""
    return state.WordStudyParamsViewModel(
        _subject=Mock(),
        _navigator=Mock(),
        _data=Mock(),
        _repo=Mock(),
        _source_subscriber=Mock(),
    )


@pytest.fixture
def screen(
    style: StyleConfig,
    theme: ThemeConfig,
    view_model: state.WordStudyParamsViewModel,
) -> view.WordStudyParamsView:
    """Provide Word study Presentation parameters screen as view."""
    return view.WordStudyParamsView(
        _style=style,
        _theme=theme,
        _content=Mock(),
        _state=view_model,
        _top_bar=Mock(),
        _params=Mock(),
    )
