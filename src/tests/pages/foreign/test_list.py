"""Test widgets of foreign word list page box."""

from unittest.mock import AsyncMock, patch

import pytest
from _pytest.monkeypatch import MonkeyPatch
from httpx import Client

from tests.utils import FixtureReader, run_until_complete
from wse.app import WSE

FIXTURE_FOREIGN_LIST = 'response_foreign_list.json'
"""The fixture file name of json http response with a list of word
(`str`).
"""
FIXTURE_PAGINATION_FIRST = 'pagination_foreign_first.json'
"""The fixture file name to test the first pagination page (`str`)."""
FIXTURE_PAGINATION_LAST = 'pagination_foreign_last.json'
"""The fixture file name to test the last pagination page (`str`)."""


@pytest.fixture(autouse=True)
def goto_foreign_list_page(wse: WSE) -> None:
    """Assign the foreign list box to main window content, fixture."""
    wse.main_window.content = wse.box_foreign_selected


def mock_list_json(*args: object, **kwargs: object) -> FixtureReader:
    """Mock a json http response with a list of terms."""
    return FixtureReader(FIXTURE_FOREIGN_LIST)


@pytest.fixture(autouse=True)
def populate_table(wse: WSE, monkeypatch: MonkeyPatch) -> None:
    """Populate foreign word list table."""
    # Mock http request word list, populate table.
    monkeypatch.setattr(Client, 'get', mock_list_json)
    wse.box_foreign_selected.populate_table()


def mock_pagination_first(*args: object, **kwargs: object) -> FixtureReader:
    """Mock a json http response to test the first pagination page."""
    return FixtureReader(FIXTURE_PAGINATION_FIRST)


def mock_pagination_last(*args: object, **kwargs: object) -> FixtureReader:
    """Mock a json http response to test the last pagination page."""
    return FixtureReader(FIXTURE_PAGINATION_LAST)


def test_widget_order(wse: WSE) -> None:
    """Test the widget and containers orger at foreign list page."""
    box = wse.box_foreign_selected

    assert box.children == [
        box._label_title,
        box._box_btns_manage,
        box._table,
        box.box_btns_paginate,
        box._btn_goto_back,
    ]

    assert box._box_btns_manage.children == [
        box._btn_create,
        box._btn_update,
        box._btn_delete,
    ]

    assert box.box_btns_paginate.children == [
        box._btn_previous,
        box._btn_table_reload,
        box._btn_next,
    ]


def test_table(wse: WSE) -> None:
    """Test table of foreign word list."""
    table = wse.box_foreign_selected._table
    assert table.table_headings == ['Иностранный', 'Русский']
    assert table.source_accessors == ['foreign_word', 'native_word']


def test_populate_table(wse: WSE, monkeypatch: MonkeyPatch) -> None:
    """Test the populate foreign word list table."""
    entry_index = 0
    entry = wse.box_foreign_selected._table.data._words[entry_index]
    assert entry.foreign_word == 'hello'
    assert entry.native_word == 'привет'


def test_label_title(wse: WSE) -> None:
    """Test page box title."""
    title = wse.box_foreign_selected._label_title
    assert title.text == 'Словарь иностранных слов'


def test_btn_goto_foreign_create(wse: WSE) -> None:
    """Test the button go to create foreign word."""
    btn = wse.box_foreign_selected._btn_create

    # Simulate a button press.
    btn._impl.simulate_press()

    # Run a fake main loop.
    run_until_complete(wse)

    # Assert button text.
    assert btn.text == 'Добавить'

    # The window content has been refreshed.
    assert wse.main_window.content == wse.box_foreign_create


def test_btn_goto_foreign_update(wse: WSE, monkeypatch: MonkeyPatch) -> None:
    """Test the button go to update foreign word page box."""
    btn = wse.box_foreign_selected._btn_update

    # Select table entry to update.
    entry_index = 1
    table = wse.box_foreign_selected._table
    table._impl.simulate_selection(entry_index)

    # Simulate a button press.
    btn._impl.simulate_press()

    # Run a fake main loop.
    run_until_complete(wse)

    # Assert button text.
    assert btn.text == 'Изменить'

    # The window content has been refreshed.
    assert wse.main_window.content == wse.box_foreign_update

    # Assert fill input fields.
    assert wse.box_foreign_update.input_foreign.value == 'apple'
    assert wse.box_foreign_update.input_native.value == 'яблоко'


########################################################################
# Create, update, delete buttons


@patch('httpx.AsyncClient.delete')
def test_btn_foreign_delete(delete: AsyncMock, wse: WSE) -> None:
    """Test the button of delete foreign word."""
    btn = wse.box_foreign_selected._btn_delete

    # Select table entry to delete.
    entry_index = 1
    table = wse.box_foreign_selected._table
    table._impl.simulate_selection(entry_index)

    # Simulate a button press.
    btn._impl.simulate_press()

    # Run a fake main loop.
    run_until_complete(wse)

    # Assert button text.
    assert btn.text == 'Удалить'

    # The window content has not been refreshed.
    assert wse.main_window.content == wse.box_foreign_selected

    # Assert http request called with arg.
    delete.assert_called_once_with('http://127.0.0.1/api/v1/foreign/2/')
