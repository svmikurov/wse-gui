Create container
================

Use a container as a reusable UI element that contains one or more widgets
and inject it on a page or in other containers.

Often, a container contains its own controller and provides its API.

Also, a container can have observers of the "Observer" pattern.

.. rubric:: Define container

Inherit container from
:class:`~wse.features.base.container.InteractiveContainerABC` or
:class:`~wse.features.base.container.NavigableContainerABC`
(adding :class:`~wse.features.base.mixins.CreateNavButtonMixin` methods)
abstract base class and override methods:

- :meth:`~wse.features.base.container.ContainerABC._create_ui`
- :meth:`~wse.features.base.container.ContainerABC._populate_content`
- :meth:`~wse.features.base._abc.mvc.UpdateStyleABC.update_style`
- :meth:`~wse.features.base._abc.mvc.LocalizeABC.localize_ui`

.. rubric:: Define style and thema

.. rubric:: Code example:

.. code-block::

    @inject
    @dataclass
    class BarContainer(
        NavigableContainerABC[StyleT, ThemeT],
    ):
        """Container for Bar."""

        @override
        def _create_ui(self) -> None:
            """Create UI."""

        @override
        def _populate_content(self) -> None:
            """Populate widget container content with UI."""

        @override
        def update_style(self, config: StyleT | ThemeT) -> None:
            """Update widgets style."""

        @override
        def localize_ui(self) -> None:
            """Localize the UI text."""
