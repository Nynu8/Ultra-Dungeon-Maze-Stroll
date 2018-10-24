from enum import Enum
from player.player import Player
from map.labyrinth import Labyrinth
from map.room import Direction
from map.room import Type

class GameState:
    class State(Enum):
        NEW_GAME = 1
        ENTER_ROOM = 2
        CHOOSE_ROOM = 3
        EXIT = 4

    def __init__(self):
        self.state = GameState.State.NEW_GAME
        self.Player = Player()
        self.Labyrinth = Labyrinth()
        self.Player.current_location = self.Labyrinth.find_start_room().id
        print(self.Player.current_location)

    def Update(self):
        if(self.state == GameState.State.NEW_GAME):
            print("New game")
            self.Player.name = input("Prosze podac imie gracza: ")
            self.state = GameState.State.ENTER_ROOM

        if(self.state == GameState.State.ENTER_ROOM):
            current_room = Labyrinth.get_room_by_id(self.Labyrinth, self.Player.current_location)
            if(current_room.type == Type.ENTRANCE):
                print("wejscie")
            elif(current_room.type == Type.WITH_KEY):
                print("z kluczem")
            elif(current_room.type == Type.EXIT):
                print("wyjscie")
            elif(current_room.type == Type.PORTAL):
                print("portal")
            else:
                print("zwykly")
            self.state = GameState.State.CHOOSE_ROOM

        if(self.state == GameState.State.CHOOSE_ROOM):
            current_room = Labyrinth.get_room_by_id(self.Labyrinth, self.Player.current_location)
            while True:
                direction = input("Gdzie chciałbyś pójść? ").lower()
                if(direction == "n"):
                    if(current_room.route.get(Direction.NORTH) != None):
                        self.Player.current_location = current_room.route.get(Direction.NORTH)
                        self.state = GameState.State.ENTER_ROOM
                        break
                if(direction == "s"):
                    if(current_room.route.get(Direction.SOUTH) != None):
                        self.Player.current_location = current_room.route.get(Direction.SOUTH)
                        self.state = GameState.State.ENTER_ROOM
                        break
                if(direction == "w"):
                    if(current_room.route.get(Direction.WEST) != None):
                        self.Player.current_location = current_room.route.get(Direction.WEST)
                        self.state = GameState.State.ENTER_ROOM
                        break
                if(direction == "e"):
                    if(current_room.route.get(Direction.EAST) != None):
                        self.Player.current_location = current_room.route.get(Direction.EAST)
                        self.state = GameState.State.ENTER_ROOM
                        break
                print("Na drodze napotykasz solidną ścianę. Być może powinieneś spróbować pójść w innym kierunku?")

        if(self.state == GameState.State.EXIT):
            pass
