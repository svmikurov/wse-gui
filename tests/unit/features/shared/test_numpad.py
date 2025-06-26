"""Test the NumPad."""

from unittest.mock import Mock

import pytest

from wse.features.interfaces import ISubject
from wse.features.shared.components.numpad import NumPadModel

MAX_CHAR_COUNT = 8
NO_TEXT = ''

# Numpad signs
BACKSPACE = '\u232b'
DOT = '\u002e'
MINUS = '\u002d'


@pytest.fixture
def mock_subject() -> Mock:
    """Fixture for creating a mock ISubject object."""
    return Mock(spec=ISubject)


@pytest.fixture
def numpad_model(mock_subject: Mock) -> NumPadModel:
    """Fixture for creating a NumPadModel instance."""
    return NumPadModel(mock_subject)


class TestNumPadModel:
    """Test the `NumPadModel`."""

    def test_initial_state(self, numpad_model: NumPadModel) -> None:
        """Test the initial model state."""
        assert numpad_model._input == NO_TEXT

    @pytest.mark.parametrize(
        'initial_input,char,expected_input',
        [
            ('', '1', '1'),
            ('1', '2', '12'),
            ('12.', '3', '12.3'),
            ('', '4', '4'),
            ('', '5', '5'),
            ('', '6', '6'),
            ('', '7', '7'),
            ('', '8', '8'),
            ('', '9', '9'),
            ('', '0', '0'),
            # Test with backspace
            ('', BACKSPACE, ''),
            ('1', BACKSPACE, ''),
            ('465', BACKSPACE, '46'),
            ('0', BACKSPACE, ''),
            ('0.', BACKSPACE, ''),
            # Test with dot
            ('', DOT, '0.'),
            ('5', DOT, '5.'),
            ('5.', DOT, '5.'),
            ('5.6', DOT, '5.6'),
            # Test with minus
            ('', MINUS, '-'),
            ('-', MINUS, ''),
            ('0.1', MINUS, '-0.1'),
            ('-9', MINUS, '9'),
            # Test with Wrong
            ('', '11', ''),
            ('', 'a', ''),
        ],
    )
    def test_chapter_input(
        self,
        initial_input: str,
        char: str,
        expected_input: str,
        mock_subject: Mock,
        numpad_model: NumPadModel,
    ) -> None:
        """Test update initial input."""
        numpad_model._input = initial_input
        numpad_model.update_input(char)
        assert numpad_model._input == expected_input

    def test_notification_update_with_allowed_char(
        self,
        mock_subject: Mock,
        numpad_model: NumPadModel,
    ) -> None:
        """Test model notification to update with allowed char."""
        numpad_model.update_input('4')
        mock_subject.notify.assert_called_once_with(
            'numpad_input_updated', value='4'
        )

    @pytest.mark.parametrize(
        'initial_input,char,expected_input',
        [
            ('', '1', '1'),
            ('1', '2', '12'),
            ('1', BACKSPACE, ''),
            ('1' * MAX_CHAR_COUNT, BACKSPACE, '1' * (MAX_CHAR_COUNT - 1)),
            ('', MINUS, '-'),
            ('-', MINUS, ''),
            ('5', DOT, '5.'),
        ],
    )
    def test_notification_occurred(
        self,
        initial_input: str,
        char: str,
        expected_input: str,
        mock_subject: Mock,
        numpad_model: NumPadModel,
    ) -> None:
        """Test that notification occurred."""
        numpad_model._input = initial_input
        numpad_model.update_input(char)
        mock_subject.notify.assert_called_once_with(
            'numpad_input_updated', value=expected_input
        )

    @pytest.mark.parametrize(
        'initial_input,char',
        [
            ('', BACKSPACE),
            ('1.', DOT),
            ('1.1', DOT),
            ('1' * MAX_CHAR_COUNT, MINUS),
        ],
    )
    def test_notification_not_occurred(
        self,
        initial_input: str,
        char: str,
        mock_subject: Mock,
        numpad_model: NumPadModel,
    ) -> None:
        """Test that notification not occurred."""
        numpad_model._input = initial_input
        numpad_model.update_input(char)
        mock_subject.notify.assert_not_called()
