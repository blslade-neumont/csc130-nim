from unittest import TestCase
from LearningAiPlayer import *
from RandomAiPlayer import *
from SilentUserInterface import *
from Game import *
from Board import *

class TestLearningAiPlayer(TestCase):
    def setUp(self):
        self.silentUi = SilentUserInterface()
        self.lp1 = LearningAiPlayer()
    
    def tearDown(self):
        self.silentUi = None
        self.lp1 = None
    
    def test_train_canBeatRandomPlayer(self):
        lp2 = LearningAiPlayer()
        self.lp1.train(lp2, iterations=1000, printProgress=False)
        
        rp = RandomAiPlayer()
        wins = 0
        for n in range(100):
            game = Game(self.silentUi)
            game.start(Board([3, 5, 7]), self.lp1, rp)
            if self.lp1.wonLastGame:
                wins += 1
        
        self.assertGreaterEqual(wins, 99)
