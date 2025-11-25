"""Test configuration."""

import pytest
from injector import Injector

from wse.config import layout
from wse.config.di_module import ConfigModule
from wse.ui.base.content.abc import ContentABC
from wse.ui.content import Content
from wse.ui.di_module import UIModule

pytest_plugins = [
    'tests.fixtures.foreign.repos',
    'tests.fixtures.foreign.sources',
]


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
