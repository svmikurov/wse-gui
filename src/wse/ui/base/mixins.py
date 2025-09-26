"""Mixins for UI layer."""

from typing import Callable

from wse.core.auth import AuthServiceProto


class SetAuthStatusMixin:
    """Mixin providing set user auth status."""

    _auth_service: AuthServiceProto

    notify: Callable[..., None]
    _update_data: Callable[..., None]

    def _set_auth_state(self) -> None:
        """Set user authenticated state."""
        if is_auth := self._auth_service.is_auth:
            self.notify('user_authenticated')
        else:
            self.notify('user_anonymous')

        self._update_data(is_auth=is_auth)
