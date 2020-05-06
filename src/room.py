# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.paths = []

    
    def __str__(self):
        return f"{self.name}\n\n{self.description}"

    ## need to initiate paths
    def set_path(self, direction, roomObj):
        self.paths.append({
            "direction": direction,
            "room": roomObj
        })
        