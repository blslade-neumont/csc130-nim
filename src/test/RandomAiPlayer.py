from unittest import TestCase
from RandomAiPlayer import *
from Game import *
from Board import *
from test.FauxUi import *

class TestRandomAiPlayer(TestCase):
    def setUp(self):
        self.p = RandomAiPlayer()
        self.game = Game(FauxUi())
    
    def tearDown(self):
        self.p = None
        self.game = None
    
    def test_makeMove_validMoves(self):
        for n in range(1000):
            board = self.game.board = Board([3, 5, 7])
            self.assertTrue(
                board.makeMove(*self.p.makeMove(self.game))
            )
