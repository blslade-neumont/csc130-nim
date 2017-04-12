

class Player(object):
    def __init__(self, name):
        self.name = name
        self.wonLastGame = False
    
    def makeMove(self, game):
        assert(False)
    
    def recordResult(self, game, win):
        self.wonLastGame = win
