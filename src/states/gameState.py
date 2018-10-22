from enum import Enum

class GameState:
    class State(Enum):
        NEW_GAME = 1
        CHOOSE_ROOM = 2
        ENTER_ROOM = 3
        ENTER_RANDOM_ROOM = 4
        EXIT = 5

    def __init__(self):
        self.state = GameState.State.NEW_GAME

    def Update(self):
        if(self.state == GameState.State.NEW_GAME):
            print("New game")
            self.state = GameState.State.EXIT