"""Test the widgets of glossary main page box.

Testing:
 * Text representation of widgets in the window content
   (text on widget, placeholder text).
 * Changing window contents when pressing move buttons.
 * Control the order of widgets at page.
"""

from unittest.mock import MagicMock, patch

import pytest
from _pytest.monkeypatch import MonkeyPatch

from tests.utils import run_until_complete
from wse.app import WSE
from wse.pages.widgets.table import TableApp


@pytest.fixture(autouse=True)
def goto_glossary_main_page(wse: WSE) -> None:
    """Assign the glossary main page box to main window content.

    The pytest fixture, ``autouse=True``.
    """
    wse.main_window.content = wse.box_glossary_main


def test_widget_order(wse: WSE) -> None:
    """Test the widget order at glossary main page box."""
    box = wse.box_glossary_main

    assert box.children == [
        box._label_title,
        box._btn_goto_params,
        box._btn_goto_create,
        box.btn_goto_list,
        box._btn_goto_back,
    ]


def test_label_title(wse: WSE) -> None:
    """Test the title of glossary term create page box."""
    title = wse.box_glossary_main._label_title
    assert title.text == 'Глоссарий'


def test_btn_goto_glossary_create_page(wse: WSE) -> None:
    """Test the button of go to create glossary term page box."""
    btn = wse.box_glossary_main._btn_goto_create

    btn._impl.simulate_press()

    # Run a fake main loop.
    run_until_complete(wse)

    assert btn.text == 'Добавить термин'
    assert wse.main_window.content == wse.box_glossary_create


@patch('httpx.Client')
def test_btn_goto_glossary_params_page(
    client: MagicMock,
    wse: WSE,
) -> None:
    """Test the button of go to glossary exercise params page box.

    Mock:
     * ``httpx.Client``, otherwise http request.
    """
    btn = wse.box_glossary_main._btn_goto_params

    btn._impl.simulate_press()

    # Run a fake main loop.
    run_until_complete(wse)

    assert btn.text == 'Упражнение'
    assert wse.main_window.content == wse.box_glossary_params


def request_entries(obj: object, url: str) -> list[tuple[str, ...]]:
    """Return entries to insert at table."""
    return [
        ('id', 'term', 'definition'),
    ]


def test_btn_goto_list(
    wse: WSE,
    monkeypatch: MonkeyPatch,
) -> None:
    """Test the button of go to glossary term list page box."""
    btn = wse.box_glossary_main.btn_goto_list
    assert btn.text == 'Словарь терминов'

    monkeypatch.setattr(TableApp, 'request_entries', request_entries)

    # No window switching.
    btn._impl.simulate_press()

    # Run a fake main loop.
    run_until_complete(wse)

    assert wse.main_window.content == wse.box_glossary_selected
