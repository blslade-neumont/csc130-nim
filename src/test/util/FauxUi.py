from UserInterface import *

class FauxUi(UserInterface):
    def __init__(self):
        super().__init__()
        self.expectIdx = 0
        self.expectVals = []
    
    def onStart(self, game):
        self.expectVals.append(('onStart', game))
    
    def solicitHumanMove(self, player):
        self.expectVals.append(('solicitHumanMove', player))
        return True
    
    def invalidMove(self):
        self.expectVals.append(('invalidMove'))
    
    def finish(self):
        self.expectVals.append(('finish'))
    
    def expect(self, expected):
        vals = self.expectVals[self.expectIdx]
        if vals == expected:
            self.expectIdx += 1
            return True
        
        return False
    
    def expectOneOrMore(self, expected):
        if not self.expect(expected):
            return False
        
        while self.expect(expected):
            pass
        
        return True
    
    def expectNoMore(self):
        return self.expectIdx == len(self.expectVals)
