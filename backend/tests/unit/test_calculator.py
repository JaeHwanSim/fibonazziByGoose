import pytest

from core.calculator import FibonacciCalculator


@pytest.fixture
def calculator():
    """Provides a FibonacciCalculator instance for tests."""
    return FibonacciCalculator()


class TestFibonacciCalculator:
    """Unit tests for the FibonacciCalculator class."""

    @pytest.mark.parametrize(
        "n, expected",
        [
            (0, 0),
            (1, 1),
            (2, 1),
            (5, 5),
            (10, 55),
            (20, 6765),
        ],
    )
    def test_calculate_valid_numbers(self, calculator, n, expected):
        """
        Tests if the calculate method returns correct Fibonacci numbers
        for a range of valid inputs.
        """
        # Act
        result = calculator.calculate(n)

        # Assert
        assert result == expected

    def test_calculate_negative_number_raises_error(self, calculator):
        """
        Tests if the calculate method raises a ValueError for negative input.
        """
        # Act & Assert
        with pytest.raises(ValueError):
            calculator.calculate(-1)

    def test_calculate_large_number_raises_error(self, calculator):
        """
        Tests if the calculate method raises a ValueError for input > 100.
        """
        # Act & Assert
        with pytest.raises(ValueError):
            calculator.calculate(101)

    @pytest.mark.parametrize(
        "n, expected_sequence",
        [
            (5, [0, 1, 1, 2, 3]),
            (10, [5, 8, 13, 21, 34]),
            (1, []),
            (0, []),
        ],
    )
    def test_get_sequence(self, calculator, n, expected_sequence):
        """
        Tests if get_sequence returns the correct preceding 5 numbers.
        """
        # Act
        sequence = calculator.get_sequence(n)

        # Assert
        assert sequence == expected_sequence
