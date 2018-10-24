from .room import Room

class Labyrinth:
    def __init__(self):
        self.room_list = []
        start = Room()
        room1 = Room()
        start.add_route(room1.id, Room.Direction.NORTH)
        self.room_list.append(start)
        room2 = Room()
        start.add_route(room1.id, Room.Direction.NORTH)
        self.room_list.append(room1)
        room1 = Room()