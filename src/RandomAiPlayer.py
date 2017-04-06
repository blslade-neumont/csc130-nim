from Player import *
from random import *

class RandomAiPlayer(Player):
    def __init__(self):
        super().__init__('Random AI')
    
    def makeMove(self, game):
        board = game.board
        return choice([
            (r, c)
            for r in range(len(board.rows))
            for c in range(1, board.rows[r] + 1)
        ])
