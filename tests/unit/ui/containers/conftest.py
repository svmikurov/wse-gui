"""Test configuration."""

from unittest.mock import Mock

import pytest

from wse.config import layout
from wse.ui.containers.info.container import InfoContainer


@pytest.fixture
def info_container(
    style: layout.StyleConfig,
    theme: layout.ThemeConfig,
    content: Mock,
) -> InfoContainer:
    """Provide the Info container."""
    return InfoContainer(
        _style=style,
        _theme=theme,
        _content=content,
    )
