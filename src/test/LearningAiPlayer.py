from unittest import TestCase
from LearningAiPlayer import *
from RandomAiPlayer import *
from PerfectAiPlayer import *
from SilentUserInterface import *
from Game import *
from Board import *

class TestLearningAiPlayer(TestCase):
    def setUp(self):
        self.lp = LearningAiPlayer()
    
    def tearDown(self):
        self.lp = None
    
    def test_train_canBeatRandomPlayer(self):
        lp2 = LearningAiPlayer()
        self.lp.train(lp2, iterations=1000, printProgress=False)
        self.assertGreaterEqual(self.countWins(self.lp, RandomAiPlayer()), 99)
    
    def test_train_beatsPerfectPlayerWhenFirst(self):
        perfect = PerfectAiPlayer()
        self.lp.train(perfect, iterations=1000, printProgress=False)
        self.assertEqual(self.countWins(self.lp, perfect, swap=False), 100)
    
    def test_train_losesToPerfectPlayerWhenLast(self):
        perfect = PerfectAiPlayer()
        self.lp.train(perfect, iterations=1000, printProgress=False)
        self.assertEqual(self.countWins(perfect, self.lp, swap=False), 100)
    
    def countWins(self, test, other, swap=True):
        silentUi = SilentUserInterface()
        wins = 0
        
        p1 = test
        p2 = other
        for n in range(100):
            game = Game(silentUi)
            game.start(Board([3, 5, 7]), p1, p2)
            if test.wonLastGame:
                wins += 1
            if swap:
                p1, p2 = p2, p1
        
        return wins
