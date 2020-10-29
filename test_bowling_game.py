import unittest
from bowling_game import Game

class GameTest(unittest.TestCase):

    def setUp(self):
        self.game = Game()
    
    def test_gutter(self):
        self.rollMany(20,0)
        self.assertEqual(0, self.game.getScore())
        
    def test_1pin(self):
        self.rollMany(20,1)
        self.assertEqual(20, self.game.getScore())

    def test_spare(self):
        self.game.roll(5)
        self.game.roll(5)
        self.game.roll(3)
        self.game.roll(4)
        self.rollMany(16, 0)
        self.assertEqual(20, self.game.getScore())

    def test_strike(self):
        self.game.roll(10)
        self.game.roll(3)
        self.game.roll(4)
        self.rollMany(17, 0)
        self.assertEqual(24, self.game.getScore())

    def test_perfect(self):
        self.rollMany(12, 10)
        self.assertEqual(300, self.game.getScore())
        
    def rollMany(self, n, pins):
        for i in range(n):
            self.game.roll(pins)
