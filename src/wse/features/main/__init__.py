"""Main pages package."""

from wse.features.main.account_controller import AccountController
from wse.features.main.account_model import AccountModel
from wse.features.main.account_view import AccountView
from wse.features.main.education_controller import EducationController
from wse.features.main.education_model import EducationModel
from wse.features.main.education_view import EducationView
from wse.features.main.home_controller import HomeController
from wse.features.main.home_model import HomeModel
from wse.features.main.home_view import HomeView
from wse.features.main.login_controller import LoginController
from wse.features.main.login_model import LoginModel
from wse.features.main.login_view import LoginView

__all__ = [
    'AccountController',
    'AccountModel',
    'AccountView',
    'EducationController',
    'EducationModel',
    'EducationView',
    'HomeController',
    'HomeModel',
    'HomeView',
    'LoginController',
    'LoginModel',
    'LoginView',
]
