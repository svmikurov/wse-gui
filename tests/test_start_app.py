"""Testing the launch of the application."""

from unittest.mock import MagicMock, patch

from wse.container import ApplicationContainer
from wse.main import main


@patch('wse.main.ApplicationContainer')
def test_main_success(container: ApplicationContainer) -> None:
    """Testing the successful launch of the application."""
    # Mock the app instance
    mock_app = MagicMock()
    container.return_value.app.return_value = mock_app

    # Start app
    app = main()

    # Assert
    assert app is mock_app
    container.return_value.app.assert_called_once()
