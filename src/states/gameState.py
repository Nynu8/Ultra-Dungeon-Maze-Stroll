from enum import Enum

class GameState:
    class State(Enum):
        NEW_GAME = 1
        CHOOSE_ROOM = 2
        ENTER_ROOM = 3
        ENTER_RANDOM_ROOM = 4
        EXIT = 5

    class Player:
        def __init__(self, name):
            self.name=name

    def __init__(self, Player):
        self.state = GameState.State.NEW_GAME
        self.Player = Player()

    def Update(self, Player):
        if(self.state == GameState.State.NEW_GAME):
            print("New game")
            Player.name=input("Prosze podac imie gracza: ")
            self.state = GameState.State.EXIT