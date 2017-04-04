

class Game(object):
    def __init__(self, ui):
        assert(ui != None)
        self.ui = ui

        self.board = None
        self.p1 = None
        self.p2 = None
        self.currentPlayer = None
    
    def start(self, board, p1, p2):
        assert(board != None and p1 != None and p2 != None)
        self.board = board
        self.p1 = p1
        self.p2 = p2
        self.currentPlayer = p1

        self.ui.onStart(self)
    
    def nextPlayer():
        assert(self.currentPlayer != None)
        self.currentPlayer = self.p2 if self.currentPlayer is self.p1 else self.p1
