from SilentUserInterface import *
from Game import *
from Board import *

def countWins(test, other, swap=True):
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
