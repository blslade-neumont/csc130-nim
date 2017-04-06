from ConsoleUserInterface import *
from Game import *
from Board import *
from HumanPlayer import *
from PerfectAiPlayer import *
from RandomAiPlayer import *

def main():
    ui = ConsoleUserInterface()
    while True:
        game = Game(ui)
        p1 = HumanPlayer('Player 1')
        # p2 = HumanPlayer('Player 2')
        # p1 = PerfectAiPlayer()
        p2 = RandomAiPlayer()
        print()
        if not game.start(Board([3, 5, 7]), p1, p2):
            break

if __name__ == '__main__':    
    main()
