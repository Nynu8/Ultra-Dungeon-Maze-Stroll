from states.gameState import GameState
from player.player import Player


class Game:

    def __init__(self):
        self.is_running = True
        self.GameState = GameState()
        self.Player = Player

    def run(self):
        while(self.GameState.state != GameState.State.EXIT):
            self.GameState.Update()

        
