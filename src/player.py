# Write a class to hold player information, e.g. what room they are in
# currently.

class Hero:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
    
    def go_to_path(self, direction):
        is_path = False

        for path in self.current_room.paths:
            if direction == path["direction"]:
                self.current_room = path['room']
                print(f"\nYou enter the {self.current_room}")
                print("\n\nInputs \n[N]orth [E]ast [S]outh [W]est [Q]uit\n")
                is_path = True

        if is_path == False:
            print("You can't travel there!")