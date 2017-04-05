from ConsoleUserInterface import *
from Game import *
from Board import *
from HumanPlayer import *
from AiPlayer import *

def main():
    ui = ConsoleUserInterface()
    while True:
        game = Game(ui)
        if not game.start(Board([3, 5, 7]), HumanPlayer('Player 1'), HumanPlayer('Player 2')):
            break

if __name__ == '__main__':    
    main()
