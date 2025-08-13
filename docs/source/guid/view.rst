Create View
===========

Inherit view form `BaseView`

Optional class attributes:

=================== ===================
Class attribute     Base class
=================== ===================
`_style_config`     `UpdateStyleABC`
`_theme_config`     `UpdateStyleABC`
=================== ===================

Required methods:

=================== ===================
Abstractmethod      ABC
=================== ===================
`_create_ui`        `ContainerABC`
`_populate_content` `ContainerABC`
`update_style`      `UpdateStyleABC`
`localize_ui`       `LocalizeABC`
=================== ===================

Optional methods:

=================== ===================
Method              Base class
=================== ===================
`__post_init__`     `ContainerABC`
`_setup`            `ContainerABC`
=================== ===================
