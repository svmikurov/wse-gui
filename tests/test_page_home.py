"""Home page testing module."""

import unittest

import pytest
import toga

from wse.app import WSE
from wse.pages import HomePage


@pytest.fixture
def page() -> toga.Widget:
    """Return the main window content."""
    app = WSE(formal_name='Test App', app_id='org.example.test')
    return app.main_window.content


def test_assign_home_page_to_main_window_content(page: toga.Widget) -> None:
    """Test is assigned Home page to window content."""
    assert isinstance(page, HomePage)


def test_home_page_widgets(page: HomePage) -> None:
    """Test that page have widgets."""
    # Test page title
    assert page.title == 'WSELFEDU'
    # Test page have text panel
    assert hasattr(page, 'info_panel')


@unittest.skip('Add buttons to page')
@pytest.mark.parametrize(
    'btn_inst, btn_text',
    [
        ('_btn_foreign', 'Иностранный'),
        ('_btn_glossary', 'Глоссарий'),
    ],
)
def test_buttons(
    page: HomePage,
    btn_inst: str,
    btn_text: str,
) -> None:
    """Test that page have buttons."""
    button: toga.Button = getattr(page, btn_inst)
    assert button.text == btn_text
