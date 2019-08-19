class Room(object):

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.path = {}
        
    def go(self, direction):
        print("test")
        return self.path.get(direction, None)
        
    def add_paths(self, paths):
        self.path.update(paths)


room = Room("bob", "tall")
room.go("left")
