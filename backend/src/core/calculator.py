from functools import lru_cache


class FibonacciCalculator:
    """
    A class to calculate Fibonacci numbers, applying SOLID principles.
    - Single Responsibility: Its only job is to calculate Fibonacci numbers.
    - Open/Closed: Can be extended (e.g., with new calculation strategies)
      without modifying existing, tested code.
    """

    @lru_cache(maxsize=None)
    def calculate(self, n: int) -> int:
        """
        Calculates the n-th Fibonacci number using an iterative algorithm.
        Includes input validation and is cached for performance.

        Args:
            n: The index in the Fibonacci sequence (must be 0 <= n <= 100).

        Returns:
            The n-th Fibonacci number.

        Raises:
            ValueError: If n is negative or greater than 100.
        """
        if not (0 <= n <= 100):
            raise ValueError("Input must be an integer between 0 and 100.")

        if n < 2:
            return n

        a, b = 0, 1
        for _ in range(n - 1):
            a, b = b, a + b

        return b

    def get_sequence(self, n: int) -> list[int]:
        """
        Returns the 5 Fibonacci numbers preceding the n-th number.
        If n < 6, it returns all preceding numbers.
        """
        if n <= 1:
            return []

        start = max(0, n - 5)
        return [self.calculate(i) for i in range(start, n)]