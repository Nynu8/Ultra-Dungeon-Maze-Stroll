import json, os

class TextData:
    def __init__(self):
        self.data = json.load(open(os.path.join('src/data', 'data.json'), encoding="utf-8"))

    def introduction(self):
        return self.data["introduction"]
    
    def room_data(self):
        print(self.data["room_data"])
        return self.data["room_data"]