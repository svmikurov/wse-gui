"""Test configuration."""

# Note: Multiple fixtures are used here to maintain consistency
# across the test suite. Revisit if maintenance becomes costly.
pytest_plugins = [
    'tests.fixtures.foreign.repos',
    'tests.fixtures.foreign.sources',
]
