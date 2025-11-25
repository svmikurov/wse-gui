"""Word study Presentation parameters data fixtures."""

import pytest

from tests import types
from tests.fixtures.foreign import parameters

# The Word study Presentation parameters consists from data:
# - parameter options
# - selected parameter
# - set parameter value


@pytest.fixture
def translation_order_options() -> list[types.CodeNameT]:
    """Provide translation order options.

    Default option is 'to_native'.
    """
    return parameters.TRANSLATE_ORDER_OPTIONS


@pytest.fixture
def word_presentation_options() -> types.ParamOptionsT:
    """Provide Word study Presentation parameter options."""
    return parameters.PRESENTATION_OPTIONS


@pytest.fixture
def word_presentation_selected(
    translation_order_options: list[types.CodeNameT],
    word_presentation_options: types.ParamOptionsT,
) -> types.InitialChoicesT:
    """Provide Word study Presentation selected parameters."""
    return {
        'category': word_presentation_options['categories'][0],  # type: ignore
        'mark': word_presentation_options['marks'][1],  # type: ignore
        'word_source': word_presentation_options['sources'][0],  # type: ignore
        'start_period': word_presentation_options['periods'][0],
        'end_period': word_presentation_options['periods'][1],
        'translation_order': translation_order_options[0],
    }


@pytest.fixture
def word_presentation_settings() -> types.PresentationSettingsT:
    """Provide Word study Presentation settings."""
    return parameters.PRESENTATION_SETTINGS


@pytest.fixture
def word_presentation_params(
    word_presentation_options: types.ParamOptionsT,
    word_presentation_selected: types.InitialChoicesT,
    word_presentation_settings: types.PresentationSettingsT,
) -> types.WordPresentationParamsT:
    """Provide Word study Presentation parameters valid data."""
    return {
        **word_presentation_options,
        **word_presentation_selected,
        **word_presentation_settings,
    }
