import uuid
from enum import Enum

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
    ENTRANCE = 5

class Room:
    def __init__(self, type = Type.COMMON):
        self.id = uuid.uuid4()
        self.route = {}
        self.type = type

    def add_route(self, room_id, direction):
        self.route[direction] = room_id