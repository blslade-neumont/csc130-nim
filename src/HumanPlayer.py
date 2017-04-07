from Player import *

class HumanPlayer(Player):
    def __init__(self, name, inputName = True):
        super().__init__(
            input(name + ", enter your name: ") or name if inputName else name
        )
    
    def makeMove(self, game):
        return game.ui.solicitHumanMove(self)
