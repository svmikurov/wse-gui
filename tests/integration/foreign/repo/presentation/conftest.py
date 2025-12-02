"""Word study presentation Repository test configuration."""

from __future__ import annotations

from http import HTTPStatus
from typing import TYPE_CHECKING, Any
from unittest.mock import Mock

import httpx
import pytest

from tests.fixtures.foreign import params as fixtures
from wse.api import foreign as api
from wse.data.repos import foreign as repos
from wse.data.schemas import foreign as schemas
from wse.data.sources import foreign as sources

if TYPE_CHECKING:
    from wse.data.dto import foreign as dto
    from wse.feature.observer import subject

# Data
# ~~~~


@pytest.fixture(scope='package')
def parameters_dto() -> dto.PresentationParameters:
    """Provide Word study parameters DTO."""
    return fixtures.PARAMETERS_DTO


# TODO: Apply typed dict
@pytest.fixture(scope='package')
def presentation_request_payload() -> dict[str, Any]:
    """Provide Word study presentation Request payload."""
    return fixtures.PRESENTATION_REQUEST_PAYLOAD


# TODO: Apply typed dict
@pytest.fixture(scope='package')
def presentation_response_json() -> dict[str, Any]:
    """Provide Word study Presentation Response json."""
    return fixtures.PRESENTATION_RESPONSE_PAYLOAD


# TODO: Apply typed dict
@pytest.fixture(scope='package')
def presentation_schema(
    presentation_response_json: dict[str, Any],
) -> schemas.Presentation:
    """Provide Word study Presentation data schema."""
    return schemas.Presentation(**presentation_response_json['data'])


# TODO: Apply typed dict
@pytest.fixture(scope='package')
def presentation_response(
    presentation_response_json: dict[str, Any],
) -> httpx.Response:
    """Provide Word study Presentation response."""
    return httpx.Response(
        status_code=HTTPStatus.OK,
        json=presentation_response_json,
    )


# Dependencies
# ~~~~~~~~~~~~


@pytest.fixture
def presentation_api_client(
    mock_http_client: Mock,
    presentation_response: httpx.Response,
) -> api.WordPresentationApi:
    """Provide Word study Presentation API client."""
    # The client must return a response
    # with the presentation case data.
    mock_http_client.post.return_value = presentation_response

    return api.WordPresentationApi(
        _http_client=mock_http_client,
        _auth_scheme=Mock(),
        _api_config=Mock(),
    )


@pytest.fixture
def locale_parameters_source(
    subject: subject.Subject,
) -> sources.WordParametersLocaleSource:
    """Provide Word study parameters Locale source."""
    return sources.WordParametersLocaleSource(
        _subject=subject,
        _data=sources.WordParametersData(),
    )


# Repository dependencies
# ~~~~~~~~~~~~~~~~~~~~~~~


@pytest.fixture
def locale_presentation_source() -> sources.WordPresentationLocaleSource:
    """Provide Word study presentation Locale source."""
    return sources.WordPresentationLocaleSource(
        _data=sources.WordPresentationData(),
    )


@pytest.fixture
def network_presentation_source(
    presentation_api_client: Mock,
) -> sources.WordPresentationNetworkSource:
    """Provide Word study presentation Network source."""
    return sources.WordPresentationNetworkSource(
        _presentation_api=presentation_api_client,
    )


@pytest.fixture
def word_params_repo(
    locale_parameters_source: sources.WordParametersLocaleSource,
) -> repos.WordParametersRepo:
    """Provide Word study Parameters repository."""
    return repos.WordParametersRepo(
        _network_source=Mock(),
        _local_source=locale_parameters_source,
    )


# Tested repository
# ~~~~~~~~~~~~~~~~~


@pytest.fixture
def presentation_repo(
    word_params_repo: repos.WordParametersRepo,
    locale_presentation_source: sources.WordPresentationLocaleSource,
    network_presentation_source: sources.WordPresentationNetworkSource,
) -> repos.WordPresentationRepo:
    """Provide Word study Presentation repository."""
    return repos.WordPresentationRepo(
        _locale_source=locale_presentation_source,
        _network_source=network_presentation_source,
        _params_repo=word_params_repo,
    )
