"""Test the widgets of glossary main page box.

Testing:
 * Text representation of widgets in the window content
   (text on widget, placeholder text).
 * Changing window contents when pressing move buttons.
 * Control the order of widgets at page.
"""

import pytest
from _pytest.monkeypatch import MonkeyPatch

from wse.app import WSE
from wse.general.table import TableApp


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
        box.label_title,
        box.btn_goto_main,
        box.btn_goto_params,
        box.btn_goto_create,
        box.btn_goto_list,
    ]


def test_label_title(wse: WSE) -> None:
    """Test the title of glossary term create page box."""
    title = wse.box_glossary_main.label_title
    assert title.text == 'Глоссарий'


def test_btn_goto_main_page(wse: WSE) -> None:
    """Test the button of go to main page box."""
    btn = wse.box_glossary_main.btn_goto_main
    assert btn.text == 'На главную'
    btn._impl.simulate_press()
    assert wse.main_window.content == wse.box_main


def test_btn_goto_glossary_create_page(wse: WSE) -> None:
    """Test the button of go to create glossary term page box."""
    btn = wse.box_glossary_main.btn_goto_create
    assert btn.text == 'Добавить термин'
    btn._impl.simulate_press()
    assert wse.main_window.content == wse.box_glossary_create


def test_btn_goto_glossary_params_page(wse: WSE) -> None:
    """Test the button of go to glossary exercise params page box."""
    btn = wse.box_glossary_main.btn_goto_params
    assert btn.text == 'Упражнение'
    btn._impl.simulate_press()
    assert wse.main_window.content == wse.box_glossary_params


def request_entries(obj: object, url: str) -> list[tuple[str, str]]:
    """Return entries to insert at table."""
    return [
        ('term', 'definition'),
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
    assert wse.main_window.content == wse.box_glossary_list
