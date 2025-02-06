"""Unit tests of user source."""

import pytest

from wse.app import WSE
from wse.models.user import User


@pytest.fixture
def source() -> User:
    """Return the source instance, fixture."""
    return User()


def test_create_instance(wse: WSE) -> None:
    """Test create the source instance."""
    assert hasattr(wse, 'user')

    # By default user instance has not private data.
    assert wse.user.username is None
    assert wse.user.is_auth is False


def test_set_auth_data(source: User) -> None:
    """Test set auth data method of source."""
    # Set for auth user.
    source._username = None
    source._is_auth = False

    source.set_userdata(dict(username='name'))

    assert source.username == 'name'
    assert source.is_auth is True

    source._username = 'name'
    source._is_auth = True
