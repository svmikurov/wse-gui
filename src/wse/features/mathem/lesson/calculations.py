"""Defines mathematical exercises."""

from wse.features.mathem.lesson.base import BaseCalcExercise


class TwoOperandMixin:
    """Mixin providing two-operand storage functionality."""

    def __init__(self, *args: object, **kwargs: object) -> None:
        """Initialize operand storage."""
        super().__init__(*args, **kwargs)
        self._operand_1: int | None = None
        self._operand_2: int | None = None

    @property
    def operand_1(self) -> int:
        """Get first operand value."""
        return self._operand_1

    @property
    def operand_2(self) -> int:
        """Get second operand value."""
        return self._operand_2


class MultiplicationTableExercise(TwoOperandMixin, BaseCalcExercise):
    """Multiplication table exercise."""

    def create_task(self) -> None:
        """Generate new multiplication task and calculate answer."""
        self._operand_1 = self._generate_operand()
        self._operand_2 = self._generate_operand()
        self._task = f'{self._operand_1} x {self._operand_2}'
        self._answer = str(self._operand_1 * self._operand_2)
