from .room import Room
from .room import Direction
from .room import Type

class Labyrinth:
    def __init__(self):
        self.room_list = []
        start = Room(Type.ENTRANCE)
        room1 = Room()
        start.add_route(room1.id, Direction.WEST)
        room2 = Room()
        start.add_route(room2.id, Direction.EAST)
        room3 = Room()
        start.add_route(room3.id, Direction.NORTH)
        self.room_list.append(start)
        room1.add_route(start.id, Direction.EAST)
        self.room_list.append(room1)
        room2.add_route(start.id, Direction.WEST)
        room4= Room(Type.PORTAL)
        room2.add_route(room4.id, Direction.NORTH)
        self.room_list.append(room2)
        room4.add_route(room2.id, Direction.SOUTH)
        room4.add_route(room3.id, Direction.WEST)
        self.room_list.append(room4)
        room5 = Room()
        room3.add_route(start.id, Direction.SOUTH)
        room3.add_route(room4.id, Direction.EAST)
        room3.add_route(room5.id, Direction.NORTH)
        self.room_list.append(room3)
        room6 = Room()
        room7 = Room()
        room8 = Room()
        room5.add_route(room3.id, Direction.SOUTH)
        room5.add_route(room6.id, Direction.WEST)
        room5.add_route(room7.id, Direction.EAST)
        room5.add_route(room8.id, Direction.NORTH)
        self.room_list.append(room5)
        room9 = Room(Type.WITH_KEY)
        room6.add_route(room5.id, Direction.EAST)
        room6.add_route(room9.id, Direction.NORTH)
        self.room_list.append(room6)
        room9.add_route(room6.id, Direction.SOUTH)
        self.room_list.append(room9)
        room10 = Room(Type.PORTAL)
        room11 = Room()
        room12 = Room()
        room10.add_route(room11.id, Direction.EAST)
        room10.add_route(room12.id, Direction.NORTH)
        self.room_list.append(room10)
        room11.add_route(room10.id, Direction.WEST)
        self.room_list.append(room11)
        room12.add_route(room10.id, Direction.SOUTH)
        self.room_list.append(room12)
        room13 = Room()
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