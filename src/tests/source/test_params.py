"""Test params source."""
from wse.source.params import ParamSource

ACCESSORS = ['alias', 'name']


def test_create() -> None:
    """Test create source."""
    source = ParamSource()

