from Player import *

class LearningAiPlayer(Player):
    def __init__(self):
        super().__init__('Learning AI')
        self.weights = { (0,0,0): -10000 }
        self.states = []
    
    def makeMove(self, game):
        selectedMove = None
        selectedState = None
        selectedWeight = None
        for move in game.board.possibleMoves():
            state = self.fakeState(game.board, move)
            
            if not selectedMove:
                selectedMove = move
                selectedState = state
                selectedWeight = self.weights[state] if state in self.weights else 0
                continue
            
            weight = self.weights[state] if state in self.weights else 0
            if weight > selectedWeight:
                selectedMove = move
                selectedState = state
                selectedWeight = weight
        
        self.states.append(selectedState)
        return selectedMove
    
    def fakeState(self, board, move):
        fakeRows = [row for row in board.rows]
        fakeRows[move[0]] -= move[1]
        return tuple(fakeRows)
    
    def recordResult(self, game, win):
        value = 1 if win else -1
        for i, state in enumerate(reversed(self.states)):
            weight = self.weights[state] if state in self.weights else 0
            weight += value / (i + 1)
            self.weights[state] = weight

    def save(self, filename):
        with open(filename, 'w') as file:
            for key in self.weights:
                file.write(",".join(map(str, key)) + ":" + str(self.weights[key]) + "\n")
    
    def load(self, filename):
        self.weights = {}
        with open(filename) as file:
            for line in file:
                key_str, score = line.split(":")
                key = tuple(map(int, key_str.split(",")))
                self.weights[key] = int(score)
