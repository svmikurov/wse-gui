"""Word study Presentation parameters Locale source tests."""

from __future__ import annotations

from typing import TYPE_CHECKING
from unittest.mock import Mock

import pytest

from tests.fixtures.foreign import params as fixtures
from wse.data.sources.foreign import params as sources

if TYPE_CHECKING:
    from wse.data.dto import foreign


@pytest.fixture(scope='module')
def parameters_dto() -> foreign.PresentationParameters:
    """Provide Word study Presentation parameters DTO."""
    return fixtures.PARAMETERS_DTO


@pytest.fixture(scope='module')
def initial_parameters_dto() -> foreign.InitialParameters:
    """Provide Word study Presentation initial parameters DTO."""
    return fixtures.INITIAL_PARAMETERS_DTO


@pytest.fixture
def source_data() -> sources.WordParametersData:
    """Provide Word study parameters Locale source data."""
    return sources.WordParametersData()


@pytest.fixture
def locale_source(
    mock_subject: Mock,
    source_data: sources.WordParametersData,
) -> sources.WordParametersLocaleSource:
    """Provide Word study Presentation params Locale source."""
    return sources.WordParametersLocaleSource(
        _subject=mock_subject,
        _data=source_data,
    )


class TestLocaleSource:
    """Word study parameters Locale source tests."""

    def test_update(
        self,
        locale_source: sources.WordParametersLocaleSource,
        parameters_dto: foreign.PresentationParameters,
    ) -> None:
        """Test update Word study parameters of Locale source."""
        # Act
        locale_source.update(parameters_dto)

        # Assert
        assert locale_source._data.__dict__ == parameters_dto.__dict__

    def test_set_initial(
        self,
        locale_source: sources.WordParametersLocaleSource,
        initial_parameters_dto: foreign.InitialParameters,
    ) -> None:
        """Test set initial Word study parameters of Locale source."""
        # Act
        locale_source.set_initial(initial_parameters_dto)

        # Assert
        assert (
            initial_parameters_dto.__dict__.items()
            <= locale_source._data.__dict__.items()
        )

    def test_get_initial(
        self,
        locale_source: sources.WordParametersLocaleSource,
        parameters_dto: foreign.PresentationParameters,
        initial_parameters_dto: foreign.InitialParameters,
    ) -> None:
        """Test get initial Word study parameters of Locale source."""
        # Arrange
        locale_source.update(parameters_dto)

        # Act & Assert
        assert locale_source.get_initial() == initial_parameters_dto

    def test_refresh_initial(
        self,
        mock_subject: Mock,
        locale_source: sources.WordParametersLocaleSource,
        parameters_dto: foreign.PresentationParameters,
        initial_parameters_dto: foreign.InitialParameters,
    ) -> None:
        """Test refresh initial Word study parameters of source."""
        # Arrange
        locale_source.update(parameters_dto)
        mock_subject.reset_mock()

        # Act
        locale_source.refresh_initial()

        # Assert
        mock_subject.notify.assert_called_once_with(
            'initial_updated',
            params=initial_parameters_dto,
        )
