from Player import *
from random import *

class RandomAiPlayer(Player):
    def __init__(self):
        super().__init__('Random AI')
    
    def makeMove(self, game):
        board = game.board
        assert(board.rows != None and len(board.rows) > 0)
        return choice(board.possibleMoves())
