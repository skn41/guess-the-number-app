import random


class NumberGuessGame:
    """Game logic for guessing an integer from 1 through 100."""

    def __init__(self, minimum: int = 1, maximum: int = 100) -> None:
        if minimum >= maximum:
            raise ValueError("minimum must be smaller than maximum")
        self.minimum = minimum
        self.maximum = maximum
        self.secret_number = 0
        self.attempts = 0
        self.reset()

    def reset(self) -> None:
        """Start a new game with a freshly chosen secret number."""
        self.secret_number = random.randint(self.minimum, self.maximum)
        self.attempts = 0

    def guess(self, value: int) -> str:
        """Compare a guess with the secret number.

        Returns one of: "higher", "lower", or "correct".
        """
        if not self.minimum <= value <= self.maximum:
            raise ValueError(
                f"Guess must be between {self.minimum} and {self.maximum}."
            )

        self.attempts += 1

        if value < self.secret_number:
            return "higher"
        if value > self.secret_number:
            return "lower"
        return "correct"
