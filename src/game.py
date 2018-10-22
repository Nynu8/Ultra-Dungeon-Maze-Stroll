from states.gameState import GameState

class Game:
    def __init__(self):
        self.GameState = GameState()
        
    def run(self):
        while(self.GameState.state != GameState.State.EXIT):
            self.GameState.Update()