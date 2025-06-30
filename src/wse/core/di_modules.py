"""Defines Core injector module."""

from typing import no_type_check

import httpx
from injector import Binder, Module, provider, singleton

from .api.exercise import ExerciseApi
from .api.interfaces import IExerciseApi
from .auth.service import AuthService
from .interfaces import INavigator
from .interfaces.iauth import IAuthService
from .navigation.navigator import Navigator


class CoreModule(Module):
    """Core injector module."""

    @no_type_check
    def configure(self, binder: Binder) -> None:
        """Configure dependencies."""
        binder.bind(INavigator, to=Navigator, scope=singleton)
        binder.bind(IAuthService, to=AuthService)

        # Api
        binder.bind(IExerciseApi, to=ExerciseApi)

    # Api
    @provider
    @singleton
    def provide_http_client(self) -> httpx.Client:
        """Provide the http client."""
        return httpx.Client()
