import unittest
from bowling import Game

class BowlingTest(unittest.TestCase):

    def setUp(self):
        self.game = Game()

    def test_all_gutters(self):
        self.helper_test_roll(20,0)
        self.assertEqual(0, self.game.score())

    def test_one_spare(self):
        self.game.roll(5)
        self.game.roll(5)
        self.game.roll(6)
        self.helper_test_roll(17,0)
        self.assertEqual(self.game.score(), 22)

    def test_one_strike(self):
        self.game.roll(10)
        self.game.roll(4)
        self.game.roll(4)
        self.helper_test_roll(17, 0)
        self.assertEqual(self.game.score(), 26)

    def test_perfect_game(self):
        self.helper_test_roll(12, 10)
        self.assertEqual(self.game.score(),300)

    def test_all_spares(self):
        self.helper_test_roll(21,5)
        self.assertEqual(self.game.score(), 150)


    def helper_test_roll(self, rolls, pins):
        for roll in range(rolls):
            self.game.roll(pins)

if __name__ == '__main__':
    unittest.main()
