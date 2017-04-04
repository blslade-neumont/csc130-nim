from Player import *

class HumanPlayer(Player):
    def __init__(self, name):
        self.name = name
    
    def makeMove(self, game):
        while True:
            if game.board.makeMove(*game.ui.solicitHumanMove(self)):
                return
