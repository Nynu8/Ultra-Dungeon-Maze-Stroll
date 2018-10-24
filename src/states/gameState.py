from enum import Enum
from src.player import Player
from src.labyrinth import Labyrinth

class GameState:
    class State(Enum):
        NEW_GAME = 1
        CHOOSE_ROOM = 2
        ENTER_ROOM = 3
        ENTER_RANDOM_ROOM = 4
        EXIT = 5

    def __init__(self):
        self.state = GameState.State.NEW_GAME
        self.Player = Player()
        self.Labyrinth = Labyrinth()

    def Update(self):
        if(self.state == GameState.State.NEW_GAME):
            print("New game")
            self.Player.name=input("Prosze podac imie gracza: ")
            self.state = GameState.State.EXIT