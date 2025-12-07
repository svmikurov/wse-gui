"""Word study presentation Parameters test configuration."""

from __future__ import annotations

from http import HTTPStatus
from typing import TYPE_CHECKING, Any
from unittest.mock import Mock

import httpx
import pytest

from tests.fixtures.foreign import parameters as fixtures
from wse.api import foreign as api
from wse.data.repos import foreign as repos
from wse.data.sources import foreign as sources

if TYPE_CHECKING:
    from wse.feature.observer import subject

# Data
# ~~~~


# TODO: Apply typed dict
@pytest.fixture(scope='package')
def params_response_json() -> dict[str, Any]:
    """Provide Word study Parameters Response json."""
    return fixtures.PARAMETERS_RESPONSE_PAYLOAD


# TODO: Apply typed dict
@pytest.fixture(scope='package')
def params_response(
    params_response_json: dict[str, Any],
) -> httpx.Response:
    """Provide Word study Parameters response."""
    return httpx.Response(
        status_code=HTTPStatus.OK,
        json=params_response_json,
        request=httpx.Request(method='GET', url='https://...'),
    )


# Mock dependencies
# ~~~~~~~~~~~~~~~~~


# Dependencies
# ~~~~~~~~~~~~


@pytest.fixture
def word_params_api_client(
    mock_http_client: Mock,
    params_response: httpx.Response,
) -> api.WordParametersApi:
    """Provide Word study Parameters API client."""
    # The client returns a response with
    # the presentation Parameters data.
    mock_http_client.get.return_value = params_response

    return api.WordParametersApi(
        _http_client=mock_http_client,
        _auth_scheme=Mock(),
        _api_config=Mock(),
    )


# Repository dependencies
# ~~~~~~~~~~~~~~~~~~~~~~~


@pytest.fixture
def locale_parameters_source(
    subject: subject.Subject,
) -> sources.WordParametersLocaleSource:
    """Provide Word study parameters Locale source."""
    return sources.WordParametersLocaleSource(
        _subject=subject,
        _data=sources.WordParametersData(),
    )


@pytest.fixture
def network_parameters_source(
    word_params_api_client: api.WordParametersApi,
) -> sources.WordParametersNetworkSource:
    """Provide Word study parameters Locale source."""
    return sources.WordParametersNetworkSource(
        _api_client=word_params_api_client,
    )


# Tested repository
# ~~~~~~~~~~~~~~~~~


@pytest.fixture
def word_params_repo(
    locale_parameters_source: sources.WordParametersLocaleSource,
    network_parameters_source: sources.WordParametersNetworkSourceABC,
) -> repos.WordParametersRepo:
    """Provide Word study Parameters repository."""
    return repos.WordParametersRepo(
        _network_source=network_parameters_source,
        _local_source=locale_parameters_source,
    )
