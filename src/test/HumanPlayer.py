from unittest import TestCase
from HumanPlayer import *
from Game import *
from test.util.FauxUi import *

class TestHumanPlayer(TestCase):
    def setUp(self):
        self.p = HumanPlayer('Player 1', inputName = False)
        self.game = Game(FauxUi())
    
    def tearDown(self):
        self.p = None
        self.game = None
    
    def test_makeMove_callsSolicitHumanMove(self):
        self.assertTrue(self.p.makeMove(self.game))
