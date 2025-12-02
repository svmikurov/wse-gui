"""Word study Presentation screen test configuration."""

from __future__ import annotations

from typing import TYPE_CHECKING
from unittest.mock import Mock

import pytest

from wse.data.repos import foreign as repos
from wse.domain.foreign import presentation as domain
from wse.ui.foreign.presentation import state, view

if TYPE_CHECKING:
    from wse.config import layout
    from wse.feature.observer.subject import Subject
    from wse.ui.content import Content

# Repositories
# ~~~~~~~~~~~~


@pytest.fixture
def parameters_repo() -> repos.WordParametersRepo:
    """Provide parameters repository."""
    return repos.WordParametersRepo(
        _local_source=Mock(),
        _network_source=Mock(),
    )


@pytest.fixture
def presentation_repo(
    parameters_repo: repos.WordParametersRepo,
) -> repos.WordPresentationRepo:
    """Provide Word study Presentation repository."""
    return repos.WordPresentationRepo(
        _locale_source=Mock(),
        _network_source=Mock(),
        _params_repo=parameters_repo,
    )


# Domain
# ~~~~~~


@pytest.fixture
def study_case(
    subject: Subject,
    presentation_repo: repos.WordPresentationRepo,
) -> domain.WordStudyUseCase:
    """Provide Word study Presentation domain."""
    return domain.WordStudyUseCase(
        _subject=subject,
        _get_word_repo=presentation_repo,
        _progress_repo=Mock(),
        _settings_repo=Mock(),
        _domain=Mock(),
    )


# Screen dependencies
# ~~~~~~~~~~~~~~~~~~~


@pytest.fixture
def view_model(
    subject: Subject,
    mock_navigator: Mock,
    study_case: domain.WordStudyUseCase,
) -> state.WordPresentationViewModel:
    """Provide Word study Presentation ViewModel."""
    return state.WordPresentationViewModel(
        _subject=subject,
        _navigator=mock_navigator,
        _study_case=study_case,
        _normalize_case=Mock(),
    )


# Tested screen
# ~~~~~~~~~~~~~


@pytest.fixture
def screen(
    style: layout.StyleConfig,
    theme: layout.ThemeConfig,
    content: Content,
    subject: Subject,
    view_model: state.WordPresentationViewModel,
) -> view.WordPresentationView:
    """Provide Word study Presentation view as screen."""
    return view.WordPresentationView(
        _style=style,
        _theme=theme,
        _content=content,
        _subject=subject,
        _state=view_model,
        _top_bar=Mock(),
        _presentation_container=Mock(),
        _control_container=Mock(),
        _info_container=Mock(),
    )
