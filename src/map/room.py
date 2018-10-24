import uuid
from enum import Enum
class Room:
    class Direction(Enum):
        NORTH = 1
        EAST = 2
        SOUTH = 3
        WEST = 4

    def __init__(self):
        self.id = uuid.uuid4()
        self.route = {}

    def add_route(self, room_id, direction):
        self.route[room_id] = direction
    