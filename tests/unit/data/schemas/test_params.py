"""Word study parameters Schema tests."""

from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from tests.fixtures.foreign import params as fixtures

if TYPE_CHECKING:
    from wse.data.schemas import foreign as schemas


@pytest.fixture(scope='module')
def schema() -> schemas.PresentationParametersSchema:
    """Provide Word study presentation parameters schema."""
    return fixtures.PARAMETERS_SCHEMA


class TestPresentationParametersSchema:
    """Word study presentation parameters schema tests."""

    def test_convert_schema_to_dto(
        self,
        schema: schemas.PresentationParametersSchema,
    ) -> None:
        """Test that Schema was converted to DTO."""
        assert schema.to_dto() == fixtures.PARAMETERS_DTO
