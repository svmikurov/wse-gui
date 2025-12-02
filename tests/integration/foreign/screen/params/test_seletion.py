"""Selection widget integration tests."""

from __future__ import annotations

from typing import TYPE_CHECKING

from wse.data.dto import foreign as dto

if TYPE_CHECKING:
    from unittest.mock import Mock

    from wse.data.schemas import foreign as schemas
    from wse.ui.containers.params import container
    from wse.ui.foreign.params import view


class TestSelection:
    """Selection widget tests."""

    def test_populate_no_initial_option_value(
        self,
        mock_params_api: Mock,
        screen: view.WordStudyParamsView,
        parameters_container: container.ParamsContainer,
        parameters_schema: schemas.PresentationParameters,
        parameters_dto: dto.PresentationParameters,
    ) -> None:
        """Test that selection populated with stub."""
        # Arrange
        expected_options = [dto.NOT_SELECTED, *parameters_dto.categories]

        # - Mock api options data return
        mock_params_api.fetch.return_value = parameters_schema

        # - Populate screen with data
        screen.on_open()

        # Act
        parameters_container._category.value = dto.NOT_SELECTED

        # Assert
        # - That selection items have 'not selected' item
        assert expected_options == parameters_container._category.items._items  # type: ignore[union-attr]

        # - That UIState was updated with 'not selected'
        assert screen._state._data.category != parameters_dto.category  # type: ignore[attr-defined]
        assert screen._state._data.category is None  # type: ignore[attr-defined]

        # - Other UIState field was not updated
        assert screen._state._data.mark == parameters_dto.mark  # type: ignore[attr-defined]
