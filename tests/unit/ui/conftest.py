"""Test configuration."""

import pytest
from unittest.mock import Mock
from wse.feature import observer
from wse.config import layout
from wse.config.di_module import ConfigModule
from wse.ui.base.content.abc import ContentABC
from wse.ui.content import Content
from wse.ui.di_module import UIModule

from injector import Injector


@pytest.fixture
def ui_injector() -> Injector:
    """Get UI injector with config module."""
    return Injector(
        [
            ConfigModule(),
            UIModule(),
        ]
    )


@pytest.fixture
def style(
    ui_injector: Injector,
) -> layout.StyleConfig:
    """Get style config."""
    return ui_injector.get(layout.StyleConfig)


@pytest.fixture
def theme(
    ui_injector: Injector,
) -> layout.ThemeConfig:
    """Get theme config."""
    return ui_injector.get(layout.ThemeConfig)


@pytest.fixture
def content(
    ui_injector: Injector,
) -> Content:
    """Mock container content fixture."""
    return ui_injector.get(ContentABC)  # type: ignore


@pytest.fixture
def mock_subject() -> Mock:
    """Mock container content fixture."""
    return Mock(spec=observer.SubjectABC)


@pytest.fixture
def mock_observer() -> Mock:
    """Mock container content fixture."""
    return Mock()
