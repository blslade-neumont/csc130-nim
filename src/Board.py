class Board(object):
    def __init__(self, rows):
        self.rows = rows

    def makeMove(self, rowIndex, amount):
        if 0 <= rowIndex < len(self.rows) and 0 < amount <= self.rows[rowIndex]:
            self.rows[rowIndex] -= amount
            return True
        return False
    
    def isEmpty(self):
        return not any(self.rows)
