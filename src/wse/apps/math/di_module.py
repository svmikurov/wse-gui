"""Defines Mathematics application module."""

from typing import no_type_check

from injector import Binder, Module, provider, singleton

from wse.config.settings import CONFIGS_PATH
from wse.utils.loader import ApiConfigLoader

from .http import IMathAPI
from .http.api import MathAPI
from .http.config import MathAPIConfigV1
from .interfaces import IMathRoutes
from .routes import MathRoutes


class MathAppModule(Module):
    """Math app module."""

    @no_type_check
    def configure(self, binder: Binder) -> None:
        """Configure binders."""
        # Routes
        binder.bind(IMathRoutes, to=MathRoutes)

        # API
        binder.bind(IMathAPI, to=MathAPI)

    @singleton
    @provider
    def provide_api_config(self) -> MathAPIConfigV1:
        """Provide the math app API config."""
        loader = ApiConfigLoader(
            MathAPIConfigV1,
            CONFIGS_PATH / 'api_math.json',
        )
        return loader.load_api_config()
