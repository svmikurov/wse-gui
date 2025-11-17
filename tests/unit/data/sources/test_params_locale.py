"""Word study Presentation params Locale source tests."""

import pytest
from injector import Injector

from wse.data.sources.di_module import SourceModule
from wse.data.sources.foreign import params, schemas
from wse.feature.observer.subject import Subject


@pytest.fixture
def initial_params() -> schemas.ParamsSchema:
    """Provide Word study Presentation initial params."""
    return schemas.ParamsSchema(
        categories=[],
        labels=[],
        default_category=None,
        default_label=None,
    )


@pytest.fixture
def params_locale_source(
    subject: Subject,
) -> params.WordParamsLocaleSource:
    """Provide Word study Presentation params Locale source."""
    injector = Injector(SourceModule())
    return params.WordParamsLocaleSource(
        _subject=subject,
        _data=injector.get(params.WordParamsData),
    )


class TestLocale:
    """Word study Presentation params Locale source tests."""

    def test_set_and_get_presentation_params(
        self,
        initial_params: schemas.ParamsSchema,
        params_locale_source: params.WordParamsLocaleSource,
    ) -> None:
        """Test set and get Presentation params."""
        # Act
        params_locale_source.set_initial_params(initial_params)

        # Assert
        assert (
            params_locale_source._data.categories == initial_params.categories
        )
        assert params_locale_source._data.labels == initial_params.labels
        assert (
            params_locale_source._data.default_category
            == initial_params.default_category
        )
        assert (
            params_locale_source._data.default_label
            == initial_params.default_label
        )
