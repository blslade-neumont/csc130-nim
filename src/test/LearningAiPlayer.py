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
        self.lp2 = LearningAiPlayer()
        self.trainPlayers()
    
    def tearDown(self):
        self.silentUi = None
        self.lp1 = None
        self.lp2 = None
    
    def trainPlayers(self):
        print('Training Learning AIs')
        lp1 = self.lp1
        lp2 = self.lp2
        for q in range(2500):
            if q % 125 == 0:
                print(str(q / 25) + '% done')
            game = Game(self.silentUi)
            game.start(Board([3, 5, 7]), lp1, lp2)
            lp1, lp2 = lp2, lp1
    
    def test_canBeatRandomP(self):
        rp = RandomAiPlayer()
        wins = 0
        for n in range(100):
            game = Game(self.silentUi)
            game.start(Board([3, 5, 7]), self.lp1, rp)
            if self.lp1.wonLastGame:
                wins += 1
        
        self.assertGreaterEqual(wins, 99)
