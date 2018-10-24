import uuid
from enum import Enum
class Room:
    class Direction(Enum):
        NORTH = 1
        EAST = 2
        SOUTH = 3
        WEST = 4
    class Type(Enum):
        COMMON = 1
        PORTAL = 2
        WITH_KEY = 3
        EXIT = 4
        
    def __init__(self):
        self.id = uuid.uuid4()
        self.route = {}
        self.type = ()

    def add_route(self, room_id, direction):
        self.route[room_id] = direction

    def add_type(self, room_type=Room.Type.COMMON):
        self.type = room_type
    
    