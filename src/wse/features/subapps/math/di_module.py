"""Defines Mathematics application module."""

import json
import logging
from typing import no_type_check

from injector import Binder, Module, provider, singleton
from pydantic import ValidationError

from wse.config.settings import CONFIGS_PATH

from .http import IMathAPI
from .http.api import MathAPI
from .http.config import MathAPIConfigV1
from .interfaces import IMathRoutes
from .routes import MathRoutes

API_CONFIG_PATH = CONFIGS_PATH / 'api_math.json'

logger = logging.getLogger(__name__)


def load_api_config() -> MathAPIConfigV1:
    """Load config to model."""
    try:
        if not API_CONFIG_PATH.exists():
            logger.error(f'Error load {API_CONFIG_PATH} API config')
            raise FileNotFoundError(f'Fail {API_CONFIG_PATH} not found')

        with API_CONFIG_PATH.open('r', encoding='utf-8') as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError as e:
                logger.exception(f'Parsing error {API_CONFIG_PATH}')
                raise ValueError(f'Json parsing error: {e}') from e

        try:
            return MathAPIConfigV1(**data)
        except ValidationError as e:
            logger.exception(f'Validation error {API_CONFIG_PATH} config')
            raise ValueError(f'Validation error: {e}') from e

    except Exception as e:
        logger.exception(f'Error to open {API_CONFIG_PATH}')
        raise RuntimeError(f'Error to open {API_CONFIG_PATH}: {e}') from e


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
        return load_api_config()
