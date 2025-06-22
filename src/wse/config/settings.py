"""Defines application settings."""

from pathlib import Path

from wse.config.styles import LayoutStyles

# General paths
PROJECT_PATH = Path(__file__).parents[1]
CONFIGS_PATH = PROJECT_PATH / 'resources' / 'config'

# Layout style configuration
LAYOUT_STYLE = LayoutStyles.GREEN
