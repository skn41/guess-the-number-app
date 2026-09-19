import unittest
from game_logic import NumberGuessGame


class NumberGuessGameTests(unittest.TestCase):
    def setUp(self):
        self.game = NumberGuessGame(1, 100)
        self.game.secret_number = 50
        self.game.attempts = 0

    def test_higher(self):
        self.assertEqual(self.game.guess(25), "higher")

    def test_lower(self):
        self.assertEqual(self.game.guess(75), "lower")

    def test_correct(self):
        self.assertEqual(self.game.guess(50), "correct")

    def test_attempts_increment(self):
        self.game.guess(10)
        self.game.guess(90)
        self.assertEqual(self.game.attempts, 2)

    def test_rejects_out_of_range_values(self):
        with self.assertRaises(ValueError):
            self.game.guess(0)
        with self.assertRaises(ValueError):
            self.game.guess(101)


if __name__ == "__main__":
    unittest.main()
