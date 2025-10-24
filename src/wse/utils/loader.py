"""Defines load data utils."""

import json
import logging
from pathlib import Path
from typing import Any, Generic, Type, TypeVar

from pydantic import BaseModel, ValidationError

log = logging.getLogger(__name__)

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
                log.error(f'Error load {self._path} API config')

            with self._path.open('r', encoding='utf-8') as f:
                try:
                    data = json.load(f)

                except json.JSONDecodeError:
                    log.exception(f'Parsing error {self._path}')

                else:
                    try:
                        return self._config(**data)
                    except ValidationError:
                        log.exception(f'Validation error {self._path} config')

        except Exception:
            log.exception(f'Error load {self._path} API config')

        return None


def load_style_data(path: Path, style_scheme: Type[T]) -> T:
    """Load config data from file."""
    try:
        with open(path, 'r') as f:
            json_data = json.load(f)

    except FileNotFoundError:
        log.error(f"Config '{path.name}' not found")
        raise

    except json.JSONDecodeError:
        log.error(f"Invalid JSON in config file '{path.name}'")
        raise

    return style_scheme.parse_obj(json_data)


def load_fixture(path: Path) -> dict[str, Any]:
    """Load json fixture."""
    with path.open('r', encoding='utf-8') as file:
        json_data: dict[str, Any] = json.load(file)
    return json_data
