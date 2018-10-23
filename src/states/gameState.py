from enum import Enum
from player.player import Player
from map.labyrinth import Labyrinth

class GameState:
    class State(Enum):
        NEW_GAME = 1
        ENTER_ROOM = 2
        CHOOSE_ROOM = 3
        ENTER_RANDOM_ROOM = 4
        EXIT = 5

    def __init__(self):
        self.state = GameState.State.NEW_GAME
        self.Player = Player()
        self.Labyrinth = Labyrinth()

    def Update(self):
        if(self.state == GameState.State.NEW_GAME):
            print("Jakas bardzo fajna historyjka na wstępie")
            Player.name = input("Jak masz na imię? ")
            self.state = GameState.State.EXIT