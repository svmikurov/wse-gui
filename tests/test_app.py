"""Test app."""

from wse_gui.app import WSEGUI

from .conftest import APP_ID, FORMAL_NAME


def test_run_app(app: WSEGUI) -> None:
    """Test run app."""
    # The app has formal name and app id.
    assert app.formal_name == FORMAL_NAME
    assert app.app_id == APP_ID

    # The main window will exist, and has content.
    assert app.main_window.content == app.main_box
