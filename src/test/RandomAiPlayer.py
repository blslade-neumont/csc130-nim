from unittest import TestCase
from RandomAiPlayer import *

class TestRandomAiPlayer(TestCase):
    def setUp(self):
        self.p = RandomAiPlayer()
    
    def tearDown(self):
        self.p = None
    
    def test_makeMove(self):
        self.skipTest('Not implemented')
