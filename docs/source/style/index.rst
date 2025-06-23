Project layout style
====================

Application style control includes configs for:

    * Widgets size
    * Widgets color theme

Configuration name enumeration is used to manage and load the configuration
---------------------------------------------------------------------------

.. code-block:: python
   :caption: config/settings.py

   RESOURCES_PATH = PROJECT_PATH / 'resources'
   STYLE_PATH = RESOURCES_PATH / 'style'
   ...
   # Layout style
   LAYOUT_THEME = LayoutTheme.DEFAULT
   LAYOUT_STYLE = LayoutStyle.DEFAULT

.. code-block:: python
   :caption: config/enums.py

    class LayoutTheme(BaseEnum):
        """Layout color theme enumerations."""

        DEFAULT = 'theme_default.json'
        GREEN = 'theme_green.json'


    class LayoutStyle(BaseEnum):
        """Layout style enumerations."""

        DEFAULT = 'style_default.json'

The `injector` library is used to load and inject the configuration
-------------------------------------------------------------------

.. code-block:: python
   :caption: config/di_module.py

   from injector import Module, provider, singleton

   LAYOUT_STYLE_PATH = STYLE_PATH / LAYOUT_STYLE
   LAYOUT_THEME_PATH = STYLE_PATH / LAYOUT_THEME


   class ConfigModule(Module):
       """Configuration injection modules container."""

       @provider
       @singleton
       def provide_style_config(self) -> StyleConfig:
           """Load and provide layout style configuration."""
           try:
               with open(LAYOUT_STYLE_PATH, 'r') as f:
                   data = json.load(f)
           except FileNotFoundError:
               data = {}

           return StyleConfig(**data)

       @provider
       @singleton
       def provide_theme_config(self) -> ThemeConfig:
           """Load and provide layout color theme configuration."""
           try:
               with open(LAYOUT_THEME_PATH, 'r') as f:
                   data = json.load(f)
           except FileNotFoundError:
               data = {}

           return ThemeConfig(**data)

The loaded configuration is wrapped in a class
----------------------------------------------

.. code-block:: python
   :caption: config/layout.py

   @dataclass
   class ThemeConfig:
       """Application layout theme configuration.

       For example, load from json config:

           {
             "content": {
               "background_color": "blue"
             },
             "title": {
               "background_color": "green",
               "color": "yellow"
             },
             ...
           }
       """

       content: dict[str, Any] = field(default_factory=dict)
       title: dict[str, str] = field(default_factory=dict)
       btn_nav: dict[str, str] = field(default_factory=dict)
       ...

   @dataclass
   class StyleConfig:
       """Application layout style configuration.

       For example, load from json config:

           {
             "window_size": [440, 700],
             "title": {
               "font_size": 20,
               "text_align": "center",
               ...
             },
             ...
           }
       """

       window_size: tuple[int, int] = field(default=(440, 700))
       title: dict[str, str | int] = field(default_factory=dict)
       btn_nav: dict[str, str | int] = field(default_factory=dict)
       ...

The configuration implementation is defined in the `BaseView` class
-------------------------------------------------------------------

.. code-block:: python
   :caption: features/base/mvc.py

   @dataclass
   class BaseView(..., ABC):
       """Abstract base class for page view."""

       ...
       _style_config: StyleConfig
       _theme_config: ThemeConfig

       def __post_init__(self) -> None:
           """Construct the view."""
           ...
           self.update_style(self._style_config)
           self.update_style(self._theme_config)

Decorate the created page view class with `@inject` and `@dataclass` and inherit from the base class
----------------------------------------------------------------------------------------------------

.. code-block:: python
   :caption: features/subapps/main/pages/home/view.py

   from injector import inject

   @inject
   @dataclass
   class HomeView(BaseView):
       """Home page view of main feature."""

       def __post_init__(self) -> None:
           """Construct the page."""
           super().__post_init__()

       ...
