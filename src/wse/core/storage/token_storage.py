"""Token storage."""

import logging
from pathlib import Path

from cryptography.fernet import Fernet

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO,
)
logger = logging.getLogger(__name__)


class TokenStorage:
    """Token storage."""

    def __init__(self, filename: str, encryption_key: str) -> None:
        """Construct the storage."""
        self._file_path = Path(filename)
        self._cipher = Fernet(encryption_key.encode())

    def save_token(self, token: str) -> None:
        """Save token."""
        try:
            encrypted_data = self._cipher.encrypt(token.encode())
            self._file_path.write_bytes(encrypted_data)
            logger.info('Token saved successfully')
        except Exception as e:
            logger.error(f'Error saving token: {e}')
            raise
