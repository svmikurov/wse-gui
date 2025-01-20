"""Test widgets of glossary term list page box."""

from unittest.mock import AsyncMock, patch

import pytest
from _pytest.monkeypatch import MonkeyPatch
from httpx import Client

from tests.utils import FixtureReader, run_until_complete
from wse.app import WSE


@pytest.fixture(autouse=True)
def goto_glossary_list_page(wse: WSE) -> None:
    """Assign the glossary list box to main window content, fixture."""
    wse.main_window.content = wse.box_glossary_selected


def mock_list_json(*args: object, **kwargs: object) -> FixtureReader:
    """Mock a json http response with a list of terms."""
    return FixtureReader('response_glossary_list.json')


@pytest.fixture(autouse=True)
def populate_table(wse: WSE, monkeypatch: MonkeyPatch) -> None:
    """Populate glossary table list table."""
    # Mock http request word list, populate table.
    monkeypatch.setattr(Client, 'get', mock_list_json)
    wse.box_glossary_selected.populate_table()


def test_widget_order(wse: WSE) -> None:
    """Test the widget and containers orger at glossary list page."""
    box = wse.box_glossary_selected

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


def test_label_title(wse: WSE) -> None:
    """Test page box title."""
    title = wse.box_glossary_selected._label_title
    assert title.text == 'Список терминов'


def test_table(wse: WSE) -> None:
    """Test table of glossary term list."""
    table = wse.box_glossary_selected._table
    assert table.table_headings == ['ID', 'Термин', 'Толкование']
    assert table.source_accessors == ['id', 'term', 'definition']


########################################################################
# Create, update, delete buttons


def test_btn_goto_glossary_create(wse: WSE) -> None:
    """Test the button go to create glossary term."""
    button = wse.box_glossary_selected._btn_create

    # Simulate a button press.
    button._impl.simulate_press()

    # Run a fake main loop.
    run_until_complete(wse)

    # Assert button text.
    assert button.text == 'Добавить'

    # The window content has been refreshed.
    assert wse.main_window.content == wse.box_glossary_create


def test_btn_goto_glossary_update(wse: WSE) -> None:
    """Test the button go to update glossary term."""
    button = wse.box_glossary_selected._btn_update

    # Select table entry to update.
    entry_index = 1
    table = wse.box_glossary_selected._table
    table._impl.simulate_selection(entry_index)

    # Simulate a button press.
    button._impl.simulate_press()

    # Run a fake main loop.
    run_until_complete(wse)

    # Assert button text.
    assert button.text == 'Изменить'

    # The window content has been refreshed.
    assert wse.main_window.content == wse.box_glossary_update

    # Assert fill input fields.
    assert wse.box_glossary_update._input_term.value == 'apple'
    assert wse.box_glossary_update._input_definition.value == 'яблоко'


@patch('httpx.AsyncClient.delete')
def test_btn_glossary_delete(
    delete: AsyncMock,
    wse: WSE,
) -> None:
    """Test the button of delete glossary term."""
    btn = wse.box_glossary_selected._btn_delete

    # Select table entry to delete.
    entry_index = 1
    table = wse.box_glossary_selected._table
    table._impl.simulate_selection(entry_index)

    # Simulate a button press.
    btn._impl.simulate_press()

    # Run a fake main loop.
    run_until_complete(wse)

    # Assert button text.
    assert btn.text == 'Удалить'

    # The window content has not been refreshed.
    assert wse.main_window.content == wse.box_glossary_selected

    # Assert http request called with arg.
    delete.assert_called_once_with('http://127.0.0.1/api/v1/glossary/2/')
