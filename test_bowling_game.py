import unittest
from bowling_game import Game

class GameTest(unittest.TestCase):

    def setUp(self):
        self.game = Game()
    
    def test_gutter(self):
        for i in range(10):
            self.game.roll(0)
        self.assertEqual(0, self.game.getScore())
        
    def test_1pin(self):
        for i in range(20):
            self.game.roll(1)
        self.assertEqual(20, self.game.getScore())
        
