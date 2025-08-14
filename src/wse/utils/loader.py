"""Defines load data utils."""

import json
import logging
from pathlib import Path
from typing import Generic, Type, TypeVar

from pydantic import ValidationError

logger = logging.getLogger(__name__)

T = TypeVar('T')


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

    def load_api_config(self) -> T:
        """Load config to model."""
        try:
            if not self._path.exists():
                logger.error(f'Error load {self._path} API config')
                raise FileNotFoundError(f'Fail {self._path} not found')

            with self._path.open('r', encoding='utf-8') as f:
                try:
                    data = json.load(f)
                except json.JSONDecodeError as e:
                    logger.exception(f'Parsing error {self._path}')
                    raise ValueError(f'Json parsing error: {e}') from e

            try:
                return self._config(**data)
            except ValidationError as e:
                logger.exception(f'Validation error {self._path} config')
                raise ValueError(f'Validation error: {e}') from e

        except Exception as e:
            logger.exception(f'Error to open {self._path}')
            raise RuntimeError(f'Error to open {self._path}: {e}') from e
