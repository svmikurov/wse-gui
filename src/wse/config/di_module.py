"""Defines config injector modules container."""

import json

from injector import Module, provider, singleton

from wse.config.layout import LayoutConfig
from wse.config.settings import CONFIGS_PATH, LAYOUT_STYLE

LAYOUT_CONFIG_PATH = CONFIGS_PATH / LAYOUT_STYLE


class ConfigModule(Module):
    """Configuration injection modules container."""

    @provider
    @singleton
    def provide_layout_config(self) -> LayoutConfig:
        """Load and provide layout configuration."""
        try:
            with open(LAYOUT_CONFIG_PATH, 'r') as f:
                data = json.load(f)
        except FileNotFoundError:
            data = {}

        return LayoutConfig(**data)
