from unittest import TestCase
from Board import *

class TestBoard(TestCase):
    def setUp(self):
        self.board = Board([3, 5, 7])
    
    def tearDown(self):
        self.board = None
    
    def test_makeMove_max(self):
        self.assertTrue(self.board.makeMove(0, 3))
    
    def test_makeMove_min(self):
        self.assertTrue(self.board.makeMove(0, 1))
    
    def test_makeMove_tooMuch(self):
        self.assertFalse(self.board.makeMove(0, 4))
    
    def test_makeMove_tooLittle(self):
        self.assertFalse(self.board.makeMove(0, 0))
    
    def test_isEmpty(self):
        self.assertFalse(self.board.isEmpty())
        self.board.rows = [0,0,0]
        self.assertTrue(self.board.isEmpty())
    
    def test_possibleMoves_initial(self):
        moves = sum(self.board.rows)
        self.assertTrue(len(self.board.possibleMoves()) == moves)
    
    def test_possibleMoves_empty(self):
        self.board.rows = [0,0,0]
        self.assertTrue(len(self.board.possibleMoves()) == 0)
