from unittest import TestCase
from LearningAiPlayer import *
from RandomAiPlayer import *
from PerfectAiPlayer import *

class TestLearningAiPlayer(TestCase):
    def setUp(self):
        self.lp = LearningAiPlayer()
    
    def tearDown(self):
        self.lp = None
    
    def test_train_canBeatRandomPlayer(self):
        lp2 = LearningAiPlayer()
        self.lp.train(lp2, iterations=1000, printProgress=False)
        self.assertGreaterEqual(self.lp.train(RandomAiPlayer(), iterations=100, printProgress=False), 99)
    
    def test_train_beatsPerfectPlayerWhenFirst(self):
        perfect = PerfectAiPlayer()
        self.lp.train(perfect, iterations=1000, printProgress=False)
        self.assertEqual(self.lp.train(perfect, iterations=100, swap=False, printProgress=False), 100)
    
    def test_train_losesToPerfectPlayerWhenLast(self):
        perfect = PerfectAiPlayer()
        self.lp.train(perfect, iterations=1000, printProgress=False)
        self.assertEqual(perfect.train(self.lp, iterations=100, swap=False, printProgress=False), 100)
