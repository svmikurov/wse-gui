"""Word study Presentation parameters Screen test configuration."""

from __future__ import annotations

from typing import TYPE_CHECKING
from unittest.mock import Mock

import pytest

from tests.fixtures.foreign import parameters
from wse.ui.containers.params.container import ParamsContainer
from wse.ui.containers.top_bar.container import TopBarController
from wse.ui.foreign.params import state, view

if TYPE_CHECKING:
    from wse.api.foreign import requests
    from wse.config import layout
    from wse.feature.observer.subject import Subject
    from wse.ui.content import Content


# Data
# ~~~~


@pytest.fixture
def parameters_dto() -> requests.PresentationParamsDTO:
    """Provide Word study Presentation parameters DTO."""
    return parameters.PRESENTATION_PARAMETERS_DTO


# Dependencies
# ~~~~~~~~~~~~


@pytest.fixture
def state_data() -> state.PresentationParamsData:
    """Provide Word study Presentation parameters UIState data."""
    return state.PresentationParamsData()


@pytest.fixture
def top_bar_container(
    subject: Subject,
) -> TopBarController:
    """Provide the Top bar container."""
    return TopBarController(
        _subject=subject,
        _container=Mock(),
    )


@pytest.fixture
def parameters_container(
    style: layout.StyleConfig,
    theme: layout.ThemeConfig,
    content: Content,
    subject: Subject,
) -> ParamsContainer:
    """Provide the Parameters container."""
    return ParamsContainer(
        _style=style,
        _theme=theme,
        _content=content,
        _subject=subject,
    )


@pytest.fixture
def view_model(
    subject: Subject,
    state_data: state.PresentationParamsData,
) -> state.WordStudyParamsViewModel:
    """Provide Word study Presentation parameters ViewModel."""
    return state.WordStudyParamsViewModel(
        _subject=subject,
        _navigator=Mock(),
        _data=state_data,
        _repo=Mock(),
        _source_subscriber=Mock(),
    )


# Tested screen with dependencies
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


@pytest.fixture
def screen(
    style: layout.StyleConfig,
    theme: layout.ThemeConfig,
    content: Content,
    view_model: state.WordStudyParamsViewModel,
    top_bar_container: TopBarController,
    parameters_container: ParamsContainer,
) -> view.WordStudyParamsView:
    """Provide Word study Presentation parameters View as Screen."""
    return view.WordStudyParamsView(
        _style=style,
        _theme=theme,
        _content=content,
        _state=view_model,
        _top_bar=top_bar_container,
        _params=parameters_container,
    )
