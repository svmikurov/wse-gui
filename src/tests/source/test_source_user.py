"""Unit tests of user source."""

import pytest

from wse.app import WSE
from wse.source.user import UserSource


@pytest.fixture
def source() -> UserSource:
    """Return the source instance, fixture."""
    return UserSource()


def test_create_instance(wse: WSE) -> None:
    """Test create the source instance."""
    assert hasattr(wse, 'user')
    assert wse.user.username is None
    assert wse.user.is_auth is False


def test_source_main_box(wse: WSE) -> None:
    """Test add source to main box."""
    assert hasattr(wse.box_main, 'user')


def test_set_auth_data(source: UserSource) -> None:
    """Test set auth data method of source."""
    # Set for auth user.
    source._username = None
    source._is_auth = False

    source.set_userdata(dict(username='name'))

    assert source.username == 'name'
    assert source.is_auth is True

    # Set for not auth user.
    source._username = 'name'
    source._is_auth = True
