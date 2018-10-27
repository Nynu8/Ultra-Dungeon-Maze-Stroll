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
    WITH_PORTAL_KEY = 3
    EXIT = 4
    ENTRANCE = 5
    WITH_DOOR_KEY = 6

class Room:
    def __init__(self, type = Type.COMMON, description = ""):
        self.id = uuid.uuid4()
        self.route = {}
        self.type = type
        self.already_visited = False
        self.description = description

    def add_route(self, room_id, direction):
        self.route[direction] = room_id