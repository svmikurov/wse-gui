"""Test a widgets specific to foreign exercise params."""

from unittest.mock import MagicMock, patch

from toga.handlers import simple_handler

from tests.utils import FixtureReader
from wse.app import WSE


@patch('httpx.Client.get')
def test_order(
    get: MagicMock,
    wse: WSE,
) -> None:
    """Test order in foreign exercise params."""
    get.return_value = FixtureReader('params_foreign.json')
    box = wse.box_foreign_params
    wse.main_window.content = box

    async def handler(*args: object, **kwargs: object) -> None:
        """Wrap the method to populate widgets."""
        await box.on_open(*args, **kwargs)

    wrapped = simple_handler(handler, 'obj')

    # Invoke the handler.
    wse.loop.run_until_complete(wrapped('button'))

    # Params widget has selections.
    expected = get.return_value.json()['exercise_choices']['orders']
    assert box.selection_order.get_items() == expected

    # Selection has value by default.
    assert box.selection_order.value.alias == 'TR'
