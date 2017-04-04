from ConsoleUserInterface import *
from Game import *
from Board import *
from HumanPlayer import *

def main():
    print('Welcome to Nim!')
    ui = ConsoleUserInterface()
    game = Game(ui)
    game.start(Board([3, 5, 7]), HumanPlayer('Player 1'), HumanPlayer('Player 2'))

if __name__ == '__main__':
    main()
