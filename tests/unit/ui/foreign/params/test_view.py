"""Word study Presentation View tests."""

import pytest

from wse.di import create_injector
from wse.ui.foreign.params.view import WordStudyParamsView


# TODO: Create injector with specific modules?
@pytest.fixture
def view() -> WordStudyParamsView:
    """Provide dependency injector."""
    injector = create_injector()
    return injector.get(WordStudyParamsView)


class TestInstantiating:
    """Presentation params View instantiating tests."""

    def test_view_instantiating(
        self,
        view: WordStudyParamsView,
    ) -> None:
        """Test the View instantiating."""
        assert view
