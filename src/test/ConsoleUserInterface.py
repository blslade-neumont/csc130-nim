from unittest import TestCase
from ConsoleUserInterface import *

class TestConsoleUserInterface(TestCase):
    def setUp(self):
        self.ui = ConsoleUserInterface()
    
    def tearDown(self):
        self.ui = None
    
    def test_printBoard(self):
        self.skipTest('Not implemented')
    
    def test_solicitHumanMove(self):
        self.skipTest('Not implemented')
    
    def test_finish(self):
        self.skipTest('Not implemented')
    
    def test_invalidMove(self):
        self.skipTest('Not implemented')
