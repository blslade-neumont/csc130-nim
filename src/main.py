from ConsoleUserInterface import *

from Game import *
from Board import *

from HumanPlayer import *
from PerfectAiPlayer import *
from RandomAiPlayer import *
from LearningAiPlayer import *

def main():
    lp1 = LearningAiPlayer()
    lp2 = LearningAiPlayer()
    
    lp1.train(lp2)
    # silentUi = SilentUserInterface()
    # print('Training AIs')
    # for q in range(2500):
    #     if q % 250 == 0:
    #         print(str(q / 25) + '% done')
    #     game = Game(silentUi)
    #     game.start(Board([3, 5, 7]), lp1, lp2)
    #     lp1, lp2 = lp2, lp1
    
    ui = ConsoleUserInterface()
    while True:
        game = Game(ui)
        p1 = HumanPlayer('Player 1')
        # p2 = HumanPlayer('Player 2')
        # p1 = PerfectAiPlayer()
        p2 = lp1 #RandomAiPlayer()
        print()
        if not game.start(Board([3, 5, 7]), p1, p2):
            break
    
    

if __name__ == '__main__':    
    main()
