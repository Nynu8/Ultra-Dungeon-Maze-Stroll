from enum import Enum
from player.player import Player
from data.data import TextData
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
        self.TextData = TextData()
        self.Player.current_location = self.Labyrinth.find_start_room().id
        print(self.Player.current_location)

    def Update(self):
        if(self.state == GameState.State.NEW_GAME):
            message = self.TextData.introduction()
            print(message["beforeName"])
            self.Player.name = input("Nazywam się ")
            print(message["afterName"])
            input()
            self.state = GameState.State.ENTER_ROOM

        if(self.state == GameState.State.ENTER_ROOM):
            description = self.TextData.room_data()
            current_room = Labyrinth.get_room_by_id(self.Labyrinth, self.Player.current_location)
            if(current_room.already_visited == True):
                print(description[current_room.type.name]["visited"])
            else:
                print(description[current_room.type.name]["not_visited"])
        
            current_room.already_visited = True
            if(current_room.type == Type.ENTRANCE):
                print("wejscie")
                self.state = GameState.State.CHOOSE_ROOM

            elif(current_room.type == Type.WITH_KEY):
                print("z kluczem")
                self.Player.can_escape = True
                self.state = GameState.State.CHOOSE_ROOM

            elif(current_room.type == Type.EXIT):
                if(self.Player.can_escape == True):
                    self.state = GameState.State.EXIT
                else:
                    self.state = GameState.State.CHOOSE_ROOM
                print("wyjscie")
            
            elif(current_room.type == Type.PORTAL):
                print("opis")
                go_through_portal = input("Chcesz przejść przez portal? Tak/Nie")
                if(go_through_portal.lower() == "tak"):
                    print("Cos sie dzieje")
                    self.Player.current_location = self.Labyrinth.find_portal_room(current_room.id).id
                
                elif(go_through_portal.lower() == "nie"):
                    print("nie to nie")
                
                else: print("Portal nie rozumie o co ci chodzi")
                self.state = GameState.State.CHOOSE_ROOM

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
            print("wyszedles")
