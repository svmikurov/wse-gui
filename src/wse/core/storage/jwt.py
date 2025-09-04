"""Defines JWT storage."""

import json
import logging
from pathlib import Path

from typing_extensions import override

from wse.config.settings import RESOURCES_PATH
from wse.core.exceptions import StorageError
from wse.core.interfaces.istorage import JWTJsonStorageProto

logger = logging.getLogger(__name__)


class JWTJsonStorage(JWTJsonStorageProto):
    """JWT storage with JSON."""

    FALLBACK_PATH = RESOURCES_PATH / '.storage' / 'jwt.json'

    def __init__(self, json_path: Path | str | None = None) -> None:
        """Construct the storage."""
        if json_path is None:
            self._json_path = self.FALLBACK_PATH
            logger.warning('JSON path for tokens not passed, fallback  used')
        else:
            self._json_path = Path(json_path)

        self._access_token: str | None = None
        self._refresh_token: str | None = None

    @override
    def save_tokens(self, access: str, refresh: str) -> None:
        """Save JWT tokens."""
        try:
            self._json_path.parent.mkdir(parents=True, exist_ok=True)

            with open(self._json_path, 'w', encoding='utf-8') as f:
                tokens = {'access': access, 'refresh': refresh}
                json.dump(tokens, f, indent=4, ensure_ascii=False)

        except Exception as e:
            logger.exception('Error saving JWT tokens to json: %s', e)
            raise StorageError from e

        finally:
            self._access_token = access
            self._refresh_token = refresh

    @override
    @property
    def access_token(self) -> str:
        """Get access storage token."""
        if self._access_token is not None:
            return self._access_token

        try:
            with open(self._json_path, 'r', encoding='utf-8') as f:
                token: str = json.load(f).get('access')
                self._access_token = token
                return token

        except FileNotFoundError as e:
            logger.debug('JSON tokens file does not exist yet')
            raise e

        except Exception as e:
            logger.exception('Error loading access token: %s', e)
            raise StorageError from e

    @access_token.setter
    def access_token(self, token: str) -> None:
        """Get access storage token."""
        try:
            with open(self._json_path, 'r', encoding='utf-8') as f:
                tokens = json.load(f)

            tokens['access'] = token

            with open(self._json_path, 'w', encoding='utf-8') as f:
                json.dump(tokens, f, indent=4, ensure_ascii=False)

        except Exception as e:
            logger.exception('Error updating access token: %s', e)
            raise StorageError from e

        finally:
            self._access_token = token

    @override
    @property
    def refresh_token(self) -> str:
        """Get access storage token."""
        if self._refresh_token is not None:
            return self._refresh_token

        try:
            with open(self._json_path, 'r', encoding='utf-8') as f:
                token: str = json.load(f).get('refresh')
                self._refresh_token = token
                return token

        except Exception as e:
            logger.exception('Error loading refresh token: %s', e)
            raise StorageError from e

    @override
    def delete_tokens(self, missing_ok: bool = True) -> None:
        """Delete JWT tokens."""
        try:
            self._json_path.unlink(missing_ok=missing_ok)

        except Exception as e:
            logger.exception('Error deleting tokens: %s', e)
            raise StorageError from e

        finally:
            self._access_token = None
            self._refresh_token = None
