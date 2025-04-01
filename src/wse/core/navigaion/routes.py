"""Application page routes module."""

from dataclasses import dataclass

from wse.core.i18n import _


@dataclass
class Route:
    """Application page route representation."""

    btn_text: str


class Routes:
    """Application page routes."""

    FOREIGN_HOME = Route(_('foreign_home'))
    GLOSSARY_HOME = Route(_('glossary_home'))

    ...

assert Routes.foreign_home == Routes.FOREIGN_HOME.btn_text