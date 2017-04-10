from unittest import TestCase
from HumanPlayer import *

class FauxUi(object):
    def __init__(self):
        super().__init__()
    
    def solicitHumanMove(self, p):
        return True

class FauxGame(object):
    def __init__(self):
        super().__init__()
        self.ui = FauxUi()

class TestHumanPlayer(TestCase):
    def setUp(self):
        self.p = HumanPlayer('Player 1', inputName = False)
    
    def tearDown(self):
        self.p = None
    
    def test_makeMove_callsSolicitHumanMove(self):
        self.assertTrue(self.p.makeMove(FauxGame()))
