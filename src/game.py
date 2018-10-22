from states.gameState import GameState

class Game:
    def __init__(self):
        self.is_running = True
        self.GameState = GameState()

    def run(self):
        while(self.GameState.state != GameState.State.EXIT):
            self.GameState.Update()
