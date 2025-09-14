"""Defines load data utils."""

import json
import logging
from pathlib import Path
from typing import Generic, Type, TypeVar

from pydantic import BaseModel, ValidationError

logger = logging.getLogger(__name__)

T = TypeVar('T', bound=BaseModel)


class ApiConfigLoader(Generic[T]):
    """Api configuration loader."""

    def __init__(
        self,
        config: Type[T],
        config_path: Path,
    ) -> None:
        """Configure the loader."""
        self._config = config
        self._path = config_path

    def load_api_config(self) -> T | None:
        """Load configuration data from a file."""
        try:
            if not self._path.exists():
                logger.error(f'Error load {self._path} API config')

            with self._path.open('r', encoding='utf-8') as f:
                try:
                    data = json.load(f)
                except json.JSONDecodeError:
                    logger.exception(f'Parsing error {self._path}')

            try:
                return self._config(**data)
            except ValidationError:
                logger.exception(f'Validation error {self._path} config')

        except Exception:
            logger.exception(f'Error to open {self._path}')

        return None


def load_style_data(
    path: Path,
    klass: Type[T],
    container_alice: str | None = None,
) -> T:
    """Load config data from file."""
    data = {}
    try:
        with open(path, 'r') as f:
            json_data = json.load(f)
            data = (
                json_data
                if container_alice is None
                else json_data[container_alice]
            )
    except FileNotFoundError:
        logger.error(f"Config '{path.name}' not found")
        raise
    except KeyError:
        logger.error(
            f"Config '{path.name}' has no configuration "
            f"for '{container_alice}' container"
        )
        raise
    except json.JSONDecodeError:
        logger.error(f"Invalid JSON in config file '{path.name}'")
        raise

    return klass.parse_obj(data)
