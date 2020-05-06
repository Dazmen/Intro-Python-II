# Write a class to hold player information, e.g. what room they are in
# currently.

class Hero:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
    
    def go_to_path(self, direction):
        for path in self.current_room.paths:
            print("TESTTTTTTTTTTTTTT",path)
            if direction == path["direction"]:
                self.current_room = path['room']
            else:
                print("You can't travel there!")