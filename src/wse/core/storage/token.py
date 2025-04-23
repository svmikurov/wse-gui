"""Manages storage and retrieval of authentication tokens."""

import logging
from pathlib import Path

from cryptography.fernet import Fernet, InvalidToken
from pydantic import SecretStr

logger = logging.getLogger(__name__)


class TokenStorage:
    """Handles encryption and decryption of tokens."""

    def __init__(self, token_path: Path, encryption_key: SecretStr) -> None:
        """Construct the storage."""
        self._token_path = token_path
        self._cipher = Fernet(encryption_key.get_secret_value())

    def save_token(self, token: str) -> None:
        """Encrypt and save the token to a file."""
        try:
            encrypted_data = self._cipher.encrypt(token.encode())
            self._token_path.write_bytes(encrypted_data)
            logger.info('Token saved successfully')

        except Exception as e:
            logger.exception(f'Error saving token {self._token_path}: {e}')
            raise

    def load_token(self) -> str | None:
        """Load and decrypt the token from a file."""
        if not self._token_path.exists():
            logger.warning('Token file not found')
            return None

        try:
            encrypted_data = self._token_path.read_bytes()
            decrypted_data = self._cipher.decrypt(encrypted_data)
            return decrypted_data.decode()

        except InvalidToken:
            logger.exception('Invalid encryption key, could not decrypt token')
            self._token_path.unlink()
            return None

        except Exception as e:
            logger.exception(f'Error loading token: {e}')
            return None

    def delete_token(self) -> bool:
        """Delete the token file if it exists."""
        if not self._token_path.exists():
            logger.debug('Token file not found for deletion')
            return False

        try:
            self._token_path.unlink()
            logger.info('Token deleted successfully')
            return True

        except OSError as e:
            logger.exception(f'Error deleting token {self._token_path}: {e}')
            return False
