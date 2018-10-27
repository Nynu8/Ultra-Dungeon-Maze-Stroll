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
        QUIT = 5

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
        
            if(current_room.type == Type.ENTRANCE):
                self.state = GameState.State.CHOOSE_ROOM

            elif(current_room.type == Type.WITH_PORTAL_KEY):
                self.Player.can_use_portal = True
                self.state = GameState.State.CHOOSE_ROOM

            elif(current_room.type == Type.WITH_DOOR_KEY):
                self.Player.can_escape = True
                self.state = GameState.State.CHOOSE_ROOM

            elif(current_room.type == Type.EXIT):
                if(self.Player.can_escape == True):
                    self.state = GameState.State.EXIT
                else:
                    self.state = GameState.State.CHOOSE_ROOM
            
            elif(current_room.type == Type.PORTAL1):
                if(self.Player.can_use_portal):
                    if(current_room.already_visited == True and self.Labyrinth.find_portal_room(current_room.id).already_visited == True):
                        print(description[current_room.type.name]["portal_opened"]["visited"])
                    else:
                        print(description[current_room.type.name]["portal_opened"]["not_visited"])
                    go_through_portal = input("Chcesz przejść przez portal? (Tak/Nie) ")
                    if(go_through_portal.lower() == "tak"):
                        print("Cos sie dzieje...")
                        self.Player.current_location = self.Labyrinth.find_portal_room(current_room.id).id
                        self.State = GameState.State.ENTER_ROOM
                    elif(go_through_portal.lower() == "nie"):
                        print("Nie to nie... Obrażony portal się wyłącza") 
                        self.state = GameState.State.CHOOSE_ROOM
                    else: 
                        print("Portal nie rozumie o co ci chodzi. Chyba go nie obraziłeś?")  
                        self.state = GameState.State.CHOOSE_ROOM    
                else:
                    self.state = GameState.State.CHOOSE_ROOM

            elif(current_room.type == Type.PORTAL2):
                go_through_portal = input("Chcesz przejść przez portal? (Tak/Nie) ")
                if(go_through_portal.lower() == "tak"):
                    print("Cos sie dzieje...")
                    self.Player.current_location = self.Labyrinth.find_portal_room(current_room.id).id
                    self.State = GameState.State.ENTER_ROOM
                elif(go_through_portal.lower() == "nie"):
                    print("Nie to nie... Obrażony portal się wyłącza")   
                    self.state = GameState.State.CHOOSE_ROOM 
                else: 
                    print("Portal nie rozumie o co ci chodzi. Chyba go nie obraziłeś?")
                    self.state = GameState.State.CHOOSE_ROOM

            else:
                print(current_room.description)
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
                if(direction == "q"):
                    self.state = GameState.State.QUIT
                    break
                print("Na drodze napotykasz solidną ścianę. Być może powinieneś spróbować pójść w innym kierunku?\n")

        if(self.state == GameState.State.EXIT):
            print(self.TextData.ending())
            return False
        
        if(self.state == GameState.State.QUIT):
            print("\b\rZnudziło Ci się błądzenie po labiryncie. Doszedłeś do wniosku że i tak nienawidzisz wszystkich i wszystkiego. Postanowiłeś usiąść i czekać na koniec z godnością")
            return False
        current_room.already_visited = True
        return True
