"""Test the Control container."""

from unittest.mock import Mock

import pytest

from wse.config import layout
from wse.ui.containers.control import Action, ControlNotifyT
from wse.ui.containers.control.container import ControlContainer
from wse.ui.content import Content

CONTAINER_NOTIFICATION: ControlNotifyT = 'handle'


@pytest.fixture
def control_container(
    style: layout.StyleConfig,
    theme: layout.ThemeConfig,
    content: Content,
    mock_subject: Mock,
) -> ControlContainer:
    """Get Control container fixture."""
    return ControlContainer(
        _style=style,
        _theme=theme,
        _content=content,
        _subject=mock_subject,
    )


class TestControlContainer:
    """Test the Control container."""

    @pytest.mark.parametrize(
        'btn_row_index, btn_col_index, action',
        (
            [1, 0, Action.DISPLAY],
            [1, 1, Action.NEXT],
            [1, 2, Action.PAUSE],
            [0, 0, Action.KNOWN],
            [0, 1, Action.UNKNOWN],
        ),
    )
    def test_notification_call(
        self,
        btn_row_index: int,
        btn_col_index: int,
        action: Action,
        mock_subject: Mock,
        control_container: ControlContainer,
    ) -> None:
        """Test that button press call notification."""
        # Reset mock to ensure clean state
        mock_subject.reset_mock()

        btn = control_container.content.children[btn_row_index].children[
            btn_col_index
        ]

        # Simulate button press
        btn._impl.interface.on_press()

        # Verify notification was called with correct parameters
        mock_subject.notify.assert_called_once_with(
            CONTAINER_NOTIFICATION, action=action
        )

    def test_add_observer(
        self,
        mock_subject: Mock,
        mock_observer: Mock,
        control_container: ControlContainer,
    ) -> None:
        """Test that `add_observer()` was called."""
        control_container.add_observer(mock_observer)
        mock_subject.add_observer.assert_called_once_with(mock_observer)

    def test_remove_observer(
        self,
        mock_subject: Mock,
        mock_observer: Mock,
        control_container: ControlContainer,
    ) -> None:
        """Test that `remove_observer()` was called."""
        control_container.remove_observer(mock_observer)
        mock_subject.remove_observer.assert_called_once_with(mock_observer)

    def test_container_has_correct_attributes(
        self,
        control_container: ControlContainer,
    ) -> None:
        """Test that container has all required attributes."""
        assert control_container._style is not None
        assert control_container._theme is not None
        assert control_container._content is not None
        assert control_container._subject is not None
