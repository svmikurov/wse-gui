"""Defines Core injector module."""

from typing import no_type_check

import httpx
import toga
from injector import Binder, Module, provider, singleton

from wse.core.http.auth import AuthSchema
from wse.core.http.client import HttpClient

from .api.auth_jwt import AuthAPIjwt
from .api.exercise import ExerciseApiClient
from .auth.service import AuthService
from .http import IHttpClient
from .http._iabc.inspector import IAccountStateInspector
from .http.inspector import AccountStateInspector
from .interfaces import INavigator
from .interfaces.iapi import (
    IAuthAPIjwt,
    IAuthScheme,
    IExerciseApiClient,
)
from .interfaces.iauth import IAuthService
from .interfaces.istorage import IJWTJsonStorage
from .navigation.navigator import Navigator
from .storage import JWTJsonStorage


class CoreModule(Module):
    """Core injector module."""

    # TODO: Check the singleton scopes
    @no_type_check
    def configure(self, binder: Binder) -> None:
        """Configure dependencies."""
        # Navigation service
        binder.bind(INavigator, to=Navigator, scope=singleton)

        # Authentication service
        binder.bind(IAuthService, to=AuthService, scope=singleton)

        # HTTP services
        binder.bind(IHttpClient, to=HttpClient)
        binder.bind(IAuthScheme, to=AuthSchema, scope=singleton)
        binder.bind(IAccountStateInspector, to=AccountStateInspector)

        # API services
        binder.bind(IAuthAPIjwt, to=AuthAPIjwt)
        binder.bind(IExerciseApiClient, to=ExerciseApiClient)

        # Storage service
        binder.bind(IJWTJsonStorage, JWTJsonStorage)

    @provider
    @singleton
    def provide_http_client(self) -> httpx.Client:
        """Provide the http client."""
        return httpx.Client()

    @provider
    @singleton
    def provide_main_window(self) -> toga.MainWindow:
        """Provide the Main window."""
        return toga.MainWindow()
