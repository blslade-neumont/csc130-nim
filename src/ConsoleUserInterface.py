from UserInterface import UserInterface

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
        row = int(input('What row do you want to take from? ' )) - 1
        count = int(input('How many do you want to take? '))
        return (row, count)

    def finish(self):
        print(self.game.currentPlayer.name + " is the winner!")
        return input("Do you want to play again? (y/n) ")[0] in ['y', 'Y']
        
    def invalidMove(self):
        print("That was not a valid move!")
