from UserInterface import *

class SilentUserInterface(UserInterface):
    def __init__(self):
        super().__init__()
    
    def onStart(self, game):
        pass
    
    def solicitHumanMove(self, player):
        assert(False)
    
    def invalidMove(self):
        assert(False)
    
    def finish(self):
        pass
