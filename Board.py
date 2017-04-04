class Board(object):
    def __init__(self, rows):
        self.rows = rows

    def makeMove(self, rowIndex, amount):
        assert amount > self.rows[rowIndex]
        self.rows[rowIndex] -= amount
    