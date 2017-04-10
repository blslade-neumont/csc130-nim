from UserInterface import UserInterface
from Util import *

class ConsoleUserInterface(UserInterface):
    def __init__(self):
        super().__init__()
    
    def onStart(self, game):
        super().onStart(game)
        print('Welcome to Nim!')
    
    def printBoard(self):
        assert(self.game is not None)
        print()
        for i, row in enumerate(self.game.board.rows):
            print(i + 1, '#', '-' * row)
    
    def solicitHumanMove(self, player):
        self.printBoard()
        print('\n' + player.name + ', make your move!')
        
        row, count = None, None
        while row == None or count == None:
            row = ignore_exception(ValueError, None)(int)(input('What row do you want to take from? '))
            if (row == None):
                self.invalidMove()
                continue
            row -= 1
            
            count = ignore_exception(ValueError, None)(int)(input('How many do you want to take? '))
            if (count == None):
                self.invalidMove()
                continue
        
        return (row, count)
    
    def invalidMove(self):
        print("\nThat was not a valid move!")
    
    def finish(self):
        print("\n" + self.game.currentPlayer.name + " is the winner!")
        playAgain = input("Do you want to play again? (y) ")
        print()
        return playAgain == '' or playAgain[0] in ['y', 'Y']
