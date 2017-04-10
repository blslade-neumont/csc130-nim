from unittest import TestCase
from Game import *
from test.FauxUi import *

class TestGame(TestCase):
    def setUp(self):
        self.game = Game(FauxUi())
    
    def tearDown(self):
        self.game = None
    
    def test_start(self):
        self.skipTest('Not implemented')
    
    def test_play(self):
        self.skipTest('Not implemented')
    
    def test_nextPlayer(self):
        self.skipTest('Not implemented')
    
    def test_finish(self):
        self.skipTest('Not implemented')
