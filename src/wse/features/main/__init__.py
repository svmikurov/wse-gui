"""Main pages package."""

from wse.features.main.account_controller import AccountController
from wse.features.main.account_model import AccountModel
from wse.features.main.account_view import AccountView
from wse.features.main.home_controller import HomeController
from wse.features.main.home_model import HomeModel
from wse.features.main.home_view import HomeView
from wse.features.main.login_controller import LoginController
from wse.features.main.login_model import LoginModel
from wse.features.main.login_view import LoginView
from wse.features.main.practice_controller import PracticeController
from wse.features.main.practice_model import PracticeModel
from wse.features.main.practice_view import PracticeView

__all__ = [
    'AccountController',
    'AccountModel',
    'AccountView',
    'HomeController',
    'HomeModel',
    'HomeView',
    'LoginController',
    'LoginModel',
    'LoginView',
    'PracticeController',
    'PracticeModel',
    'PracticeView',
]
