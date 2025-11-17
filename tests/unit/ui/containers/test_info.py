"""Test Info container."""

import pytest

from wse.di import create_injector
from wse.ui.containers.info import InfoContainer


def test_initialise_container() -> None:
    """Test that the Info container has been initialized."""
    injector = create_injector()
    assert injector.get(InfoContainer)


class TestDisplayInfo:
    """Test display info."""

    @pytest.mark.parametrize(
        'accessor, value',
        [
            ('progress', '2'),
        ],
    )
    def test_change_context(
        self,
        accessor: str,
        value: str,
        info_container: InfoContainer,
    ) -> None:
        """Test change Info container context."""
        # Action
        info_container.change(accessor=accessor, value=value)

        # Assert
        assert info_container._progress.text == value

    @pytest.mark.parametrize(
        'accessor',
        [
            ('progress'),
        ],
    )
    def test_content(
        self,
        accessor: str,
        info_container: InfoContainer,
    ) -> None:
        """Test change Info container context."""
        # Arrange
        accessor = getattr(info_container, f'_{accessor}')
        content = info_container.content.children

        # Assert
        assert accessor in content
