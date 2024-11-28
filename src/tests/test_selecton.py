"""Test custom selection."""

from tests.utils import FixtureReader
from wse.contrib.data import SelectionEntries


def test_set_items() -> None:
    """Test update items to set."""
    expected = [
        {'alias': 'S', 'humanly': 'Изучаю'},
        {'alias': 'R', 'humanly': 'Повторяю'},
        {'alias': 'E', 'humanly': 'Проверяю'},
        {'alias': 'K', 'humanly': 'Знаю'},
    ]

    # Get json data for selection items.
    response = FixtureReader('params_foreign.json')
    json_data = response.json()['exercise_choices']['progress']

    # Initialize selection items instance.
    entries = SelectionEntries(json_data)

    # Assert items as expected.
    assert entries.items == expected
