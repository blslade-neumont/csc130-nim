from Player import *

class AiPlayer(Player):
    def __init__(self):
        super().__init__()
    
    def xorCombined(self, board):
        result = 0
        for row in board.rows:
            result ^= row
        return result
    
    def makeMove(self, game):
        x = self.xorCombined(game.board)
        
        move = None
        if x == 0:
            for i, row in enumerate(game.board.rows):
                if row > 0:
                    move = (i, 1)
        
        for i, row in enumerate(game.board.rows):
            if row ^ x < row:
                count = row - (row ^ x)
                move = (i, count)
        
        rowsGreaterThanOne = 0
        for row in game.board.rows:
            nextRow = row - move[1] if row == move[0] else row
            rowsGreaterThanOne += (nextRow > 1)
        
        if rowsGreaterThanOne == 0:
            one_count = sum(row > 0 for row in game.board.rows)
            
            count = game.board.rows[move[0]] - one_count % 2
            move = (i, count)
        
        game.board.makeMove(*move)
