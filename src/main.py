from ConsoleUserInterface import *

from Game import *
from Board import *

from HumanPlayer import *
from PerfectAiPlayer import *
from RandomAiPlayer import *
from LearningAiPlayer import *

def main():
    lp1 = LearningAiPlayer('training_data/learning-player.data')
    # lp2 = LearningAiPlayer()
    # lp1.train(lp2, iterations=2500)
    
    ui = ConsoleUserInterface()
    while True:
        game = Game(ui)
        p1 = HumanPlayer('Player 1')
        p2 = lp1
        if not game.start(Board([3, 5, 7]), p1, p2):
            break
    
    for p in [p1, p2]:
        getattr(p, "save", lambda:None)()

if __name__ == '__main__':
    main()
