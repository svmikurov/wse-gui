"""Word study Presentation parameters tests.

Additional testing of the API client is required since it mock it.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from wse.core.navigation import NavID
from wse.data.dto import foreign as dto
from wse.ui.foreign.parameters import state

if TYPE_CHECKING:
    from unittest.mock import Mock

    from wse.data.schemas import foreign as schemas
    from wse.data.sources.foreign.params import WordParametersLocaleSource
    from wse.ui.containers.params.container import ParamsContainer
    from wse.ui.foreign.parameters import view

EMPTY = dto.NOT_SELECTED


class TestActions:
    """Word study Presentation parameters user action test."""

    def test_start(
        self,
        mock_navigator: Mock,
        locale_params_source: WordParametersLocaleSource,
        screen: view.WordStudyParamsView,
        view_model: state.WordStudyParamsViewModel,
        parameters_dto: dto.PresentationParameters,
        changed_parameters_dto: dto.InitialParameters,
    ) -> None:
        """Test that Presentation started via 'Start' button."""
        # Arrange
        # - Populate Locale source with parameters
        locale_params_source.update(parameters_dto)

        # - Populate UI State with changed parameters
        view_model._update_state(changed_parameters_dto)

        # Act
        screen._btn_start._impl.interface.on_press()

        # Assert
        # - Navigator was called
        mock_navigator.navigate.assert_called_once_with(
            nav_id=NavID.FOREIGN_STUDY
        )
        # - Parameters Local source was updated with changed parameters
        assert (
            vars(changed_parameters_dto).items()
            <= vars(locale_params_source._data).items()
        )

    def test_reset(
        self,
        screen: view.WordStudyParamsView,
        locale_params_source: WordParametersLocaleSource,
        parameters_container: ParamsContainer,
        parameters_dto: dto.PresentationParameters,
    ) -> None:
        """Test that the parameters was reset via 'Reset' button."""
        # Arrange
        con = parameters_container

        # - Set source and widget initial data
        locale_params_source.update(parameters_dto)

        # - Change widget value
        con._category.value = parameters_dto.categories[0]

        # Act
        # - Simulate the 'Reset' button press
        screen._btn_reset._impl.interface.on_press()

        # Assert
        assert con._category.value == parameters_dto.categories[1]

    @pytest.mark.skip("Change the 'mark' field to a multi-select")
    def test_save(
        self,
        mock_params_api: Mock,
        screen: view.WordStudyParamsView,
        locale_params_source: WordParametersLocaleSource,
        parameters_dto: dto.PresentationParameters,
        parameters_schema: schemas.PresentationParameters,
        initial_parameters_schema: schemas.InitialParameters,
        populate_parameters_container: ParamsContainer,
    ) -> None:
        """Test that the parameters was saved via 'Save' button."""
        # Arrange
        mock_params_api.save.return_value = parameters_schema

        # Act
        # - Simulate the 'Save' button press
        screen._btn_save._impl.interface.on_press()

        # Assert
        # - api client was called
        mock_params_api.save.assert_called_once_with(initial_parameters_schema)

        # - locale source data was updated
        assert vars(locale_params_source._data) == vars(parameters_dto)


class TestScreenInitialization:
    """Word study Presentation parameters Screen initialize tests."""

    def test_success(
        self,
        mock_params_api: Mock,
        screen: view.WordStudyParamsView,
        parameters_container: ParamsContainer,
        parameters_schema: schemas.PresentationParameters,
        parameters_dto: dto.PresentationParameters,
    ) -> None:
        """Test that screen is initialized successfully."""
        # Arrange
        con = parameters_container
        dto = parameters_dto

        mock_params_api.fetch.return_value = parameters_schema

        # Act
        # Populate screen with data
        screen.on_open()

        # Assert
        # - parameters was requested
        mock_params_api.fetch.assert_called_once_with()

        # - selection has options
        assert con._category.items._items == [EMPTY] + dto.categories  # type: ignore[union-attr]
        assert con._mark.items._items == [EMPTY] + dto.marks  # type: ignore[union-attr]
        assert con._word_source.items._items == [EMPTY] + dto.sources  # type: ignore[union-attr]
        assert con._translation_order.items._items == dto.translation_orders  # type: ignore[union-attr]
        assert con._start_period.items._items == [EMPTY] + dto.periods  # type: ignore[union-attr]
        assert con._end_period.items._items == [EMPTY] + dto.periods  # type: ignore[union-attr]

        # - selection has option value
        assert con._category.value == dto.category
        # HACK: Change the 'mark' field to a multi-select
        assert con._mark.value == dto.mark[0]  # type: ignore[index]
        assert con._word_source.value == dto.word_source
        assert con._translation_order.value == dto.translation_order
        assert con._start_period.value == dto.start_period
        assert con._end_period.value == dto.end_period

        # - number input has value
        assert int(con._word_count.value) == dto.word_count  # type: ignore[arg-type]
        assert int(con._question_timeout.value) == dto.question_timeout  # type: ignore[arg-type]
        assert int(con._answer_timeout.value) == dto.answer_timeout  # type: ignore[arg-type]

        # - progress switch has default state
        assert con._is_study.value is True
        assert con._is_repeat.value is False
        assert con._is_examine.value is True
        assert con._is_know.value is False
