"""Test app."""

from wse_gui.app import WSEGUI


def test_run_app(app: WSEGUI) -> None:
    """Test app un with formal name and app id."""
    assert app.formal_name == 'Test App'
    assert app.app_id == 'org.beeware.toga.test-app'
