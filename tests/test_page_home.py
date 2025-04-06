"""Home page testing module."""

import unittest
from typing import cast

import pytest
import toga

from wse.application.app import WSE
from wse.features.main.home_view import HomeView
from wse.features.object_id import ObjectID
from wse.interface.ifeatures import IContent


@pytest.fixture
def content() -> IContent:
    """Return the main window content."""
    app = WSE(formal_name='Test App', app_id='org.example.test')
    return cast(IContent, app.main_window.content)


@pytest.fixture
def home_view() -> HomeView:
    """Return the Home view."""
    return HomeView()


def test_assign_home_page_to_main_window_content(content: IContent) -> None:
    """Test is assigned Home page to window content."""
    assert content.id == ObjectID.HOME_VIEW


def test_home_view_title_text(home_view: HomeView) -> None:
    """Test a Home view content."""
    # Test page title
    assert home_view.title == 'WSELFEDU'

    # Test page have text panel
    assert hasattr(home_view, 'info_panel')

    ...


@unittest.skip('Add buttons to page')
@pytest.mark.parametrize(
    'btn_inst, btn_text',
    [
        ('_btn_foreign', 'Иностранный'),
        ('_btn_glossary', 'Глоссарий'),
    ],
)
def test_buttons(
    content: HomeView,
    btn_inst: str,
    btn_text: str,
) -> None:
    """Test that page have buttons."""
    button: toga.Button = getattr(content, btn_inst)
    assert button.text == btn_text

    ...
