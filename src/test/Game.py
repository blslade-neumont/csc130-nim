from unittest import TestCase
from Game import *
from Board import *
from RandomAiPlayer import *
from test.InvalidMovePlayer import *
from test.FauxUi import *

class TestGame(TestCase):
    def setUp(self):
        self.ui = FauxUi()
        self.game = Game(self.ui)
    
    def tearDown(self):
        self.game = None
        self.ui = None
    
    def test_start_checkNone(self):
        board = Board([0, 0, 0])
        p1 = RandomAiPlayer()
        p2 = RandomAiPlayer()
        
        self.assertRaises(AssertionError, lambda: self.game.start(None, p1, p2))
        self.assertRaises(AssertionError, lambda: self.game.start(board, None, p2))
        self.assertRaises(AssertionError, lambda: self.game.start(board, p1, None))
    
    def test_start(self):
        board = Board([3, 5, 7])
        p1 = RandomAiPlayer()
        p2 = RandomAiPlayer()
        
        self.assertTrue(self.ui.expectNoMore())
        self.game.start(board, p1, p2)
        self.assertTrue(self.ui.expect(('onStart', self.game)));
        self.assertTrue(self.ui.expect(('finish')));
        self.assertTrue(self.ui.expectNoMore())
    
    def test_start_invalidMove(self):
        board = Board([3, 5, 7])
        p1 = InvalidMovePlayer()
        p2 = InvalidMovePlayer()
        
        self.assertTrue(self.ui.expectNoMore())
        self.game.start(board, p1, p2)
        self.assertTrue(self.ui.expect(('onStart', self.game)));
        self.assertTrue(self.ui.expectOneOrMore(('invalidMove')));
        self.assertTrue(self.ui.expect(('finish')));
        self.assertTrue(self.ui.expectNoMore())
    
    def test_nextPlayer(self):
        p1 = RandomAiPlayer()
        p2 = RandomAiPlayer()
        self.game.p1 = p1
        self.game.p2 = p2
        self.game.currentPlayer = p1
        
        self.game.nextPlayer()
        self.assertEqual(self.game.currentPlayer, p2)
        self.game.nextPlayer()
        self.assertEqual(self.game.currentPlayer, p1)
        self.game.nextPlayer()
        self.assertEqual(self.game.currentPlayer, p2)
    
    def test_nextPlayer_checkNone(self):
        self.assertRaises(AssertionError, lambda: self.game.nextPlayer())
    
    def test_finish(self):
        self.game.finish()
        self.assertTrue(self.ui.expect(('finish')));
        self.assertTrue(self.ui.expectNoMore())
