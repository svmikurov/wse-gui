"""Generate secret key."""

from cryptography.fernet import Fernet


def generate_key() -> None:
    """Generate secret key."""
    key = Fernet.generate_key()
    print(key)


if __name__ == '__main__':
    generate_key()
