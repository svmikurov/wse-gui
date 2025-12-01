"""Word study Presentation parameters Screen test configuration."""

from __future__ import annotations

from typing import TYPE_CHECKING
from unittest.mock import Mock

import pytest

from tests.fixtures.foreign import params as fixtures
from wse.api.foreign import WordParametersApiABC
from wse.data.dto import foreign as dto
from wse.data.repos.foreign.params import (
    WordParametersRepo,
    WordParametersSubscriber,
)
from wse.data.sources.foreign import params as sources
from wse.ui.containers.params.container import ParamsContainer
from wse.ui.containers.top_bar.container import TopBarController
from wse.ui.foreign.params import state, view

if TYPE_CHECKING:
    from wse.config import layout
    from wse.data.schemas import foreign as schemas
    from wse.feature.observer.subject import Subject
    from wse.ui.content import Content


# Data
# ~~~~


@pytest.fixture(scope='package')
def parameters_dto() -> dto.PresentationParameters:
    """Provide Word study parameters DTO."""
    return fixtures.PARAMETERS_DTO


@pytest.fixture(scope='package')
def initial_parameters_dto() -> dto.InitialParameters:
    """Provide Word study initial parameters DTO."""
    return fixtures.INITIAL_PARAMETERS_DTO


@pytest.fixture(scope='package')
def changed_parameters_dto() -> dto.InitialParameters:
    """Provide Word study changed parameters DTO."""
    return fixtures.CHANGED_PARAMETERS_DTO


@pytest.fixture(scope='package')
def initial_parameters_schema() -> schemas.InitialParameters:
    """Provide Word study parameters schema."""
    return fixtures.INITIAL_PARAMETERS_SCHEMA


@pytest.fixture(scope='package')
def parameters_schema() -> schemas.PresentationParameters:
    """Provide Word study parameters schema."""
    return fixtures.PARAMETERS_SCHEMA


# Mocked dependencies
# ~~~~~~~~~~~~~~~~~~~


@pytest.fixture
def mock_params_api() -> Mock:
    """Mock the Word study parameters api client."""
    return Mock(spec=WordParametersApiABC)


# Dependencies
# ~~~~~~~~~~~~


@pytest.fixture
def source_data() -> sources.WordParametersData:
    """Provide Word study parameters source data."""
    return sources.WordParametersData()


@pytest.fixture
def locale_params_source(
    subject: Subject,
    source_data: sources.WordParametersData,
) -> sources.WordParametersLocaleSource:
    """Provide Word study parameters Locale source."""
    return sources.WordParametersLocaleSource(
        _subject=subject,
        _data=source_data,
    )


@pytest.fixture
def network_params_source(
    mock_params_api: Mock,
) -> sources.WordParametersNetworkSource:
    """Provide Word study parameters Network source."""
    return sources.WordParametersNetworkSource(
        _api_client=mock_params_api,
    )


@pytest.fixture
def parameters_repo(
    locale_params_source: sources.WordParametersLocaleSource,
    network_params_source: sources.WordParametersNetworkSource,
) -> WordParametersRepo:
    """Provide parameters repository."""
    return WordParametersRepo(
        _local_source=locale_params_source,
        _network_source=network_params_source,
    )


@pytest.fixture
def state_data() -> state.WordParametersUIState:
    """Provide Word study Presentation parameters UIState data."""
    return state.WordParametersUIState()


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
def source_subscriber(
    locale_params_source: sources.WordParametersLocaleSource,
) -> WordParametersSubscriber:
    """Provide the Top bar container."""
    return WordParametersSubscriber(
        _local_params_source=locale_params_source,
    )


@pytest.fixture
def view_model(
    subject: Subject,
    mock_navigator: Mock,
    state_data: state.WordParametersUIState,
    parameters_repo: WordParametersRepo,
    source_subscriber: WordParametersSubscriber,
) -> state.WordStudyParamsViewModel:
    """Provide Word study Presentation parameters ViewModel."""
    return state.WordStudyParamsViewModel(
        _subject=subject,
        _navigator=mock_navigator,
        _data=state_data,
        _repo=parameters_repo,
        _source_subscriber=source_subscriber,
    )


# Tested screen
# ~~~~~~~~~~~~~


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


# Configured Parameters container
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


@pytest.fixture
def populate_parameters_container(
    parameters_container: ParamsContainer,
    parameters_dto: dto.PresentationParameters,
) -> ParamsContainer:
    """Populate parameters container with test data."""
    # Arrange
    con = parameters_container
    dto = parameters_dto

    # - Set options
    con._category.items.update(dto.categories)  # type: ignore[union-attr]
    con._mark.items.update(dto.marks)  # type: ignore[union-attr]
    con._word_source.items.update(dto.sources)  # type: ignore[union-attr]
    con._translation_order.items.update(dto.translation_orders)  # type: ignore[union-attr]
    con._start_period.items.update(dto.periods)  # type: ignore[union-attr]
    con._end_period.items.update(dto.periods)  # type: ignore[union-attr]

    # - Set selected value
    con._category.value = dto.category
    con._mark.value = dto.mark
    con._word_source.value = dto.word_source
    con._translation_order.value = dto.translation_order
    con._start_period.value = dto.start_period
    con._end_period.value = dto.end_period

    # - Set number input
    con._word_count.value = dto.word_count
    con._question_timeout.value = dto.question_timeout
    con._answer_timeout.value = dto.answer_timeout

    return con
