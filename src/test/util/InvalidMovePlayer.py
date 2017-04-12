from RandomAiPlayer import *

class InvalidMovePlayer(RandomAiPlayer):
    def __init__(self):
        super().__init__()
        self.invalid = False
    
    def makeMove(self, game):
        self.invalid = not self.invalid
        if self.invalid:
            return (0, 999)
        
        return super().makeMove(game)
