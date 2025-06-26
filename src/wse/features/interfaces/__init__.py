"""Features interfaces."""

__all__ = [
    'IAddObserver',
    'IContainer',
    'IContent',
    'IController',
    'IGetContent',
    'IModel',
    'IObserver',
    'IPageController',
    'ISubject',
    'IView',
]

from .icontainer import IContainer
from .icontent import IContent, IGetContent
from .imvc import IController, IModel, IPageController, IView
from .iobserver import IAddObserver, IObserver, ISubject
