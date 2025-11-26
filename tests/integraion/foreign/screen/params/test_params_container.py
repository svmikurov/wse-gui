"""Word study Presentation parameters container tests."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from wse.api.foreign import requests
    from wse.ui.containers.params.container import ParamsContainer
    from wse.ui.foreign.params import state, view


class TestUpdateParameterWidget:
    """Word study Presentation parameter widgets update test."""

    def test_updated_successfully(
        self,
        screen: view.WordStudyParamsView,  # Builds screen
        view_model: state.WordStudyParamsViewModel,
        parameters_dto: requests.PresentationParamsDTO,
        parameters_container: ParamsContainer,
    ) -> None:
        """Test that the selection updated successfully."""
        # Arrange
        con = parameters_container
        dto = parameters_dto

        # Act
        view_model.initial_params_updated(parameters_dto)

        # TODO: Fix type ignore
        # Updated source typing?

        # Assert
        # - selection has options
        assert con._category.items._items == dto.categories  # type: ignore[union-attr]
        assert con._mark.items._items == dto.marks  # type: ignore[union-attr]
        assert con._word_source.items._items == dto.sources  # type: ignore[union-attr]
        assert con._translation_order.items._items == dto.translation_orders  # type: ignore[union-attr]
        assert con._start_period.items._items == dto.periods  # type: ignore[union-attr]
        assert con._end_period.items._items == dto.periods  # type: ignore[union-attr]

        # - selection has option value
        assert con._category.value == dto.category
        assert con._mark.value == dto.mark
        assert con._word_source.value == dto.word_source
        assert con._translation_order.value == dto.translation_order
        assert con._start_period.value == dto.start_period
        assert con._end_period.value == dto.end_period

        # - number input has value
        assert int(con._word_count.value) == dto.word_count  # type: ignore[arg-type]
        assert int(con._question_timeout.value) == dto.question_timeout  # type: ignore[arg-type]
        assert int(con._answer_timeout.value) == dto.answer_timeout  # type: ignore[arg-type]
