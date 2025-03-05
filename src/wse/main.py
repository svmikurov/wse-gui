"""Start application endpoint."""

from wse.core.app import WSE
from wse.core.di_container import DIContainer


def main() -> WSE:
    """Return the app instance."""
    container = DIContainer()
    return container.app()
