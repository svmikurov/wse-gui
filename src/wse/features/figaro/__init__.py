"""Figaro pages package."""

from wse.features.figaro.figaro_controller import FigaroController
from wse.features.figaro.figaro_model import FigaroModel
from wse.features.figaro.figaro_view import FigaroView
from wse.features.figaro.practice_controller import PracticeController
from wse.features.figaro.practice_model import PracticeModel
from wse.features.figaro.practice_view import PracticeView
from wse.features.figaro.swarm_controller import SwarmController
from wse.features.figaro.swarm_model import SwarmModel
from wse.features.figaro.swarm_view import SwarmView

__all__ = [
    'FigaroController',
    'FigaroModel',
    'FigaroView',
    'SwarmController',
    'SwarmModel',
    'SwarmView',
    'PracticeController',
    'PracticeModel',
    'PracticeView',
]
