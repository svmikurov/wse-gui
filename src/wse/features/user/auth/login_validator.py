"""Defines the login validator."""

CYRILLIC_LOWER = ''.join(chr(i) for i in range(1072, 1104))
CYRILLIC_UPPER = ''.join(chr(i) for i in range(1040, 1072))
LATIN_UPPER = ''.join(chr(i) for i in range(65, 91))
LATIN_LOWER = ''.join(chr(i) for i in range(97, 123))
NUMBERS = '0123456789'
SYMBOLS = '@.+-_'

MIN_USERNAME_LENGTH = 3
MAX_USERNAME_LENGTH = 50
MIN_PASSWORD_LENGTH = 8

USERNAME_LENGTH_ERROR = 'Username length error'
USERNAME_SYMBOL_ERROR = 'Username symbol error'
PASSWORD_LENGTH_ERROR = 'Password length error'
PASSWORD_NUMBER_ERROR = 'Password only numbers error'
EMPTY_FIELD_ERROR = 'Empty field error'


def validate_username(username: str) -> list:
    """Validate the username.

    >>> validate_username('username')
    []
    >>> validate_username('u')
    [The name must be at least 2 and no more than 50 characters]
    >>> validate_username('wrong!')
    ['The name can only contain letters, numbers and symbols @/./+/-/_']
    >>> validate_username('@.+-_1иG')
    []
    """
    allowed = (
        CYRILLIC_LOWER
        + CYRILLIC_UPPER
        + LATIN_LOWER
        + LATIN_UPPER
        + NUMBERS
        + SYMBOLS
    )

    # Checking the filling
    if not username:
        return [EMPTY_FIELD_ERROR]

    errors = []

    # Checking the length
    if (
        len(username) < MIN_USERNAME_LENGTH
        or len(username) > MAX_USERNAME_LENGTH
    ):
        errors.append(USERNAME_LENGTH_ERROR)

    # Checking symbols
    for liter in username:
        if liter not in allowed:
            errors.append(USERNAME_SYMBOL_ERROR)
            break

    return errors


def validate_password(password: str) -> list:
    """Validate the user password.

    >>> validate_password('12345678')
    ['The password cannot consist only of numbers']
    >>> validate_password('xxx')
    ['Password must be at least 8 characters long']
    >>> validate_password('password')
    []
    """
    # Checking the filling
    if not password:
        return [EMPTY_FIELD_ERROR]

    errors = [PASSWORD_NUMBER_ERROR]
    for item in password:
        if item not in NUMBERS:
            errors.pop()
            break

    if len(password) < MIN_PASSWORD_LENGTH:
        errors.append(PASSWORD_LENGTH_ERROR)

    return errors


def validate_credentials(username: str, password: str) -> list:
    """Validate the user credentials."""
    errors = []
    errors.extend(validate_username(username))
    errors.extend(validate_password(password))
    return errors
