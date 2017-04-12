from SilentUserInterface import *
from Game import *
from Board import *

class Player(object):
    def __init__(self, name):
        self.name = name
        self.wonLastGame = False
    
    def train(self, other, iterations = 2500, swap = True, printProgress = True, initialBoardState = [3, 5, 7]):
        if printProgress:
            print('Training AIs')
        silentUi = SilentUserInterface()
        p1 = self
        p2 = other
        for q in range(iterations):
            if q % (iterations // 10) == 0 and printProgress:
                print(str((q / iterations) * 100) + '% done')
            game = Game(silentUi)
            game.start(Board(initialBoardState[:]), p1, p2)
            if swap:
                p1, p2 = p2, p1
    
    def makeMove(self, game):
        assert(False)
    
    def recordResult(self, game, win):
        self.wonLastGame = win
