from ConsoleUserInterface import *

from Game import *
from Board import *

from HumanPlayer import *
from PerfectAiPlayer import *
from RandomAiPlayer import *
from LearningAiPlayer import *

def main():
    # lp1 = LearningAiPlayer()
    # lp2 = LearningAiPlayer() 
    # lp1.train(lp2)
    
    ui = ConsoleUserInterface()
    while True:
        game = Game(ui)
        #p1 = HumanPlayer('Player 1')
        p1 = PerfectAiPlayer()
        p2 = PerfectAiPlayer()
        # p2 = HumanPlayer('Player 2')
        # p2 = lp1 #RandomAiPlayer()
        print()
        if not game.start(Board([3, 5, 7]), p1, p2):
            break

if __name__ == '__main__':    
    main()
