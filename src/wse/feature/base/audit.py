"""Defines mixins for audite."""

import logging

audit_logger = logging.getLogger('audit')


class AuditMixin:
    """Mixin for audite."""

    def __del__(self) -> None:
        """Call on delete instance."""
        audit_logger.info(f'Deleted {self.__class__}')
