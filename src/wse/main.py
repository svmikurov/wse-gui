"""Entry point for starting the application."""

from wse.core.app import WSE
from wse.core.di_container import DIContainer


def main() -> WSE:
    """Create and return the application instance."""
    container = DIContainer()
    return container.app()
