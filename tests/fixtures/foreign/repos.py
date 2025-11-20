"""Foreign discipline source fixtures."""

from unittest.mock import Mock

import pytest

from wse.data.repos.foreign import params


@pytest.fixture
def params_repo(
    mock_network_params_source: Mock,
    mock_locale_params_source: Mock,
) -> params.WordParamsRepo:
    """Provide Word study params repository."""
    return params.WordParamsRepo(
        _network_source=mock_network_params_source,
        _local_source=mock_locale_params_source,
    )
