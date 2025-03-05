"""Token storage."""

import logging
from pathlib import Path
from typing import Optional

from cryptography.fernet import Fernet, InvalidToken

from wse.interfaces.icore import ITokenStorage

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO,
)
logger = logging.getLogger(__name__)


class TokenStorage(ITokenStorage):
    """Token storage."""

    def __init__(self, token_path: str | Path, encryption_key: str) -> None:
        """Construct the storage."""
        self._token_path = Path(token_path)
        self._cipher = Fernet(encryption_key.encode())

    def save_token(self, token: str) -> None:
        """Save token."""
        try:
            encrypted_data = self._cipher.encrypt(token.encode())
            self._token_path.write_bytes(encrypted_data)
            logger.info('Token saved successfully')

        except Exception as e:
            logger.error(f'Error saving token: {e}')
            raise

    def load_token(self) -> Optional[str]:
        """Load token."""
        if not self._token_path.exists():
            logger.warning('Token file not found')
            return None

        try:
            encrypted_data = self._token_path.read_bytes()
            return self._cipher.decrypt(encrypted_data).decode()

        except InvalidToken:
            logger.error('Invalid encryption key, could not decrypt token')
            self._token_path.unlink()
            return None

        except Exception as e:
            logger.error(f'Error loading token: {e}')
            return None
