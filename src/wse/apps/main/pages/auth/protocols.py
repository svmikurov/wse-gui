"""Defines Authentication page interfaces."""

from typing import Any, Protocol

from wse.feature.interfaces.imvc import (
    ModelProto,
    PageControllerProto,
    ViewProto,
)

# Model


class AuthModelFeatureProto(Protocol):
    """Protocol for Authentication page model feature interface."""

    def handle_success_authentication(self) -> None:
        """Handle the success authentication."""


class AuthModelProto(
    AuthModelFeatureProto,
    ModelProto,
    Protocol,
):
    """Protocol for Authentication page model interface."""


class AuthModelObserverProto(Protocol):
    """Protocol for Model page view notification observer interface."""

    def credential_clean(self) -> None:
        """Handle the credential clean."""


# View


class AuthViewProto(
    ViewProto,
    Protocol,
):
    """Protocol for Authentication page view interface."""


class AuthViewObserverProto(Protocol):
    """Protocol for Auth page view notification observer interface."""

    def success_authentication(self) -> None:
        """Handle the success authentication event."""


# Controller


class AuthControllerProto(
    PageControllerProto[Any],
    Protocol,
):
    """Protocol for Authentication page controller interface."""
