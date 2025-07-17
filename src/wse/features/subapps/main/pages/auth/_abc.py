"""Defines abstract base class with Auth page model features."""

from abc import ABC, abstractmethod

from typing_extensions import override

from .interfaces import IAuthModel


class AuthModelABC(
    ABC,
    IAuthModel,
):
    """Abstract base class with Authentication page model features."""

    @abstractmethod
    @override
    def handle_success_authentication(self) -> None:
        """Handle the success authentication."""
