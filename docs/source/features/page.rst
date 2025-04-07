=======================
Add Foreign params page
=======================

Add modules
===========

Add MVC model to `feature` package
  * Add model module (optional): `feature/params_model.py`
  * Add view module: `feature/params_view.py`
  * Add controller module: `feature/params_controller.py`

::

   src/
   ├── wse/
   │   └── features/
   │       ├── foreign/
   │       │   ├── di_container.py
   │       │   ├── params_controller.py
   │       │   ├── params_view.py
   │       │   └── ...
   │       └── ...
   └── ...

Add ParamsView class
====================

Inherit page view from BaseView.

.. code-block:: python
   :caption: src/wse/features/foreign/params_view.py

   class ParamsView(BaseView):
       """Foreign params view."""

       def __init__(self, content_box: BaseContent | None = None) -> None:
           """Construct the view."""
           super().__init__(content_box)

Add ID for page content

.. code-block:: python
   :caption: src/wse/features/foreign/params_view.py

   class ParamsView(BaseView):
       def __init__(self, content_box: BaseContent | None = None) -> None:
           ...
           self._content.id = ObjectID.FOREIGN_PARAMS

Add a call of methods:
  * to create UI elements
  * to assign text to UI elements
  * to add UI elements to content box

.. code-block:: python
   :caption: src/wse/features/foreign/params_view.py

   class ParamsView(BaseView):
       def __init__(self, content_box: BaseContent | None = None) -> None:
           ...
           self._create_ui()
           self._assign_ui_text()
           self._add_ui()

Add methods.

.. code-block:: python
   :caption: src/wse/features/foreign/params_view.py

   class ParamsView(BaseView):
       ...

       def _add_ui(self) -> None:
           self.content.add(
               self._label_title,
               self.info_panel,
               self._btn_goto_back,
           )

        def _create_ui(self) -> None:
            # Title
            self._label_title = TitleLabel('')

            # Info panel
            self.info_panel = MultilineInfoPanel()

            # NavigationID buttons
            self._btn_goto_back = self._create_nav_btn()

        def _assign_ui_text(self) -> None:
            self._label_title.text = _('Foreign params title')
            self._btn_goto_back.text = _(NavigationID.BACK)

Add page content ID to ObjectID class
=====================================

.. code-block:: python
   :caption: src/wse/features/object_id.py

   @unique
   class ObjectID(str, Enum):
       """Application object ID enumeration."""
       ...
       FOREIGN_PARAMS = 'Foreign params view'

Add page navigation ID to NavigationID class
============================================

.. code-block:: python
   :caption: src/wse/core/navigation/navigation_id.py

   @unique
   class NavigationID(BaseEnum):
       """Application navigation ID enumeration."""
       ...
       FOREIGN_PARAMS = 'Foreign params'

Add ParamsController class
==========================

Inherit page view from BaseController.

.. code-block:: python
   :caption: src/wse/features/foreign/params_controller.py

   @dataclass
   class ParamsController(BaseController):
       """Foreign params page controller."""

Add page to dependency-injector container
=========================================

.. code-block:: python
   :caption: src/wse/features/foreign/di_container.py

   class ForeignContainer(containers.DeclarativeContainer):
       """Foreign pages container."""

       content_box = providers.Dependency()
       ...

       # Foreign params page
       params_view = providers.Factory(ParamsView, content_box=content_box)
       params_controller = providers.Factory(ParamsController, view=params_view)

       # NavigationID routes
       routes = providers.Dict(
           {
               NavigationID.FOREIGN_PARAMS: params_controller,
               ...
           }
       )

Add navigation button to ForeignView class
==========================================

.. code-block:: python
   :caption: src/wse/features/foreign/home_view.py

   class ForeignView(BaseView):
       """Foreign home page view."""
       ...

       def _add_ui(self) -> None:
           self.content.add(
               ...
               self._btn_goto_params,
           )

       def _create_ui(self) -> None:
           ...
           self._btn_goto_params = self._create_nav_btn()

       def _assign_ui_text(self) -> None:
           ...
           self._btn_goto_params.text = _(NavigationID.FOREIGN_PARAMS)
