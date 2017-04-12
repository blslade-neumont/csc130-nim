from unittest import TestCase
from PerfectAiPlayer import *

class TestPerfectAiPlayer(TestCase):
    def setUp(self):
        self.p = PerfectAiPlayer()
    
    def tearDown(self):
        self.p = None
    
    def test_train_winsWhenFirst(self):
        self.assertEqual(self.p.train(PerfectAiPlayer(), iterations=100, swap=False, printProgress=False), 100)
    
    def test_train_losesWhenLast(self):
        self.assertEqual(PerfectAiPlayer().train(self.p, iterations=100, swap=False, printProgress=False), 100)
