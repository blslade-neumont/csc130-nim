from unittest import TestCase
from PerfectAiPlayer import *
from test.util.countWins import *

class TestPerfectAiPlayer(TestCase):
    def setUp(self):
        self.p = PerfectAiPlayer()
    
    def tearDown(self):
        self.p = None
    
    def test_train_winsWhenFirst(self):
        self.assertEqual(countWins(self.p, PerfectAiPlayer(), swap=False), 100)
    
    def test_train_losesWhenLast(self):
        self.assertEqual(countWins(PerfectAiPlayer(), self.p, swap=False), 100)
