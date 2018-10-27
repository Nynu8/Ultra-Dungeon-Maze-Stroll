from .room import Room
from .room import Direction
from .room import Type

class Labyrinth:
    def __init__(self):
        self.room_list = []
        start = Room(Type.ENTRANCE)
        room1 = Room(description="Wchodzisz do małego pokoju, w którym poza drzwiami, którymi właśnie wszedłeś, nie ma żadnych innych. Na przeciwległej ścianie wisi jedynie obraz przedstawiający łąkę pełną grzybów i postać z brodą w długich szatach przypominającą druida albo maga z kreskówek. \"Architekci tego labiryntu chyba średnio mieli pomysł na to jak zagospodarować pomieszczenia\" myślisz.")
        start.add_route(room1.id, Direction.WEST)
        room2 = Room(description="Znajdujesz się w pokoju przechodnim, zza kolejnych drzwi skierowanych na północ dostrzegasz jednak ciekawsze pomieszczenie.")
        start.add_route(room2.id, Direction.EAST)
        room3 = Room(description="Jesteś w pokoju, z którego wychodzą trzy korytarze, widzisz też szerokie schody prowadzące w dół w kierunku północnym.")
        start.add_route(room3.id, Direction.NORTH)
        self.room_list.append(start)
        room1.add_route(start.id, Direction.EAST)
        self.room_list.append(room1)
        room2.add_route(start.id, Direction.WEST)
        room4= Room(Type.PORTAL1)
        room2.add_route(room4.id, Direction.NORTH)
        self.room_list.append(room2)
        room4.add_route(room2.id, Direction.SOUTH)
        room4.add_route(room3.id, Direction.WEST)
        self.room_list.append(room4)
        room5 = Room(description="Docierasz do wielkiej sali, zdobiony strop podpierają grube filary. Możesz wejść schodami z powrotem na górę w południowym kierunku lub wybrać jedno z trzech tajemniczych przejść.")
        room3.add_route(start.id, Direction.SOUTH)
        room3.add_route(room4.id, Direction.EAST)
        room3.add_route(room5.id, Direction.NORTH)
        self.room_list.append(room3)
        room6 = Room(description="Trafiasz do pomieszczenia z kolejnymi drzwiami skierowanymi na północ.")
        room7 = Room(description="Są tu drzwi, dzięki którym możesz pójść w kierunkach północnym lub zachodnim.")
        room8 = Room(description="Idziesz na północ i trafiasz do pokoju z przejściem po stronie wschodniej.")
        room5.add_route(room3.id, Direction.SOUTH)
        room5.add_route(room6.id, Direction.WEST)
        room5.add_route(room7.id, Direction.EAST)
        room5.add_route(room8.id, Direction.NORTH)
        self.room_list.append(room5)
        room9 = Room(Type.WITH_PORTAL_KEY)
        room6.add_route(room5.id, Direction.EAST)
        room6.add_route(room9.id, Direction.NORTH)
        self.room_list.append(room6)
        room9.add_route(room6.id, Direction.SOUTH)
        self.room_list.append(room9)
        room10 = Room(Type.PORTAL2)
        room11 = Room(Type.WITH_DOOR_KEY)
        room12 = Room(description="Delikatne światło okazuje się być jedynie świeczką na kamiennej półce. Nic ciekawego tu nie ma. ")
        room10.add_route(room11.id, Direction.EAST)
        room10.add_route(room12.id, Direction.NORTH)
        self.room_list.append(room10)
        room11.add_route(room10.id, Direction.WEST)
        self.room_list.append(room11)
        room12.add_route(room10.id, Direction.SOUTH)
        self.room_list.append(room12)
        room13 = Room(description="Z tego pomieszczenia możesz pójść na na zachód, wschód lub południe.")
        room7.add_route(room5.id, Direction.WEST)
        room7.add_route(room13.id, Direction.NORTH)
        self.room_list.append(room7)
        room8.add_route(room5.id, Direction.SOUTH)
        room8.add_route(room13.id, Direction.EAST)
        self.room_list.append(room8)
        room14 = Room(Type.EXIT)
        room13.add_route(room7.id, Direction.SOUTH)
        room13.add_route(room8.id, Direction.WEST)
        room13.add_route(room14.id, Direction.EAST)
        self.room_list.append(room13)
        room14.add_route(room13.id, Direction.WEST)
        self.room_list.append(room14)

    def get_room_by_id(self, id):
        for room in self.room_list:
            if(room.id == id):
                return room

    def find_start_room(self):
        for room in self.room_list:
            if(room.type == Type.ENTRANCE):
                return room
    
    def find_portal_room(self, id):
        for room in self.room_list:
            if((room.type == Type.PORTAL1 or room.type == Type.PORTAL2) and room.id != id):
                return room