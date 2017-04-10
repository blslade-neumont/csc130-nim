

class UserInterface(object):
    def __init__(self):
        self.game = None
    
    def onStart(self, game):
        self.game = game
    
    def solicitHumanMove(self, player):
        assert(False)
    
    def invalidMove(self):
        assert(False)
    
    def finish(self):
        assert(False)
