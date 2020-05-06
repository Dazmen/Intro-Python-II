from room import Room
from player import Hero
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together
# print(room['foyer'])
room['outside'].set_path('n', room['foyer']) 
room['foyer'].set_path("s", room['outside'])
room['foyer'].set_path("n", room['overlook'])
room['foyer'].set_path("e", room['narrow'])
room['overlook'].set_path("s", room['foyer'])
room['narrow'].set_path("w", room['foyer'])
room['narrow'].set_path("n", room['treasure'])
room['treasure'].set_path("s", room['narrow'])
# room['outside'].n = room['foyer']
# room['foyer'].s = room['outside']
# room['foyer'].n = room['overlook']
# room['foyer'].e = room['narrow']
# room['overlook'].s = room['foyer']
# room['narrow'].w = room['foyer']
# room['narrow'].n = room['treasure']
# room['treasure'].s = room['narrow']

#
# Main
#

hero_name = input("Select your name Hero! ")
# Make a new player object that is currently in the 'outside' room.
hero = Hero(hero_name, room['outside'])
##### Attempting to have users create their own hero name



# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

directions = ['n', 'e', 's', 'w']

print(f"\n{hero.name}, you start your journey here \n")

while True:
    # print the current room
    # print room/enviroment descriptions
    # print input instructions
    print(f"\n You enter the {hero.current_room}")
    print("\n[N]orth \n[E]ast \n[S]outh \n[W]est \n[Q]uit")

    user_input = input("\nChoose your action: ").lower()
    # A way to exit the loop
    if user_input == "q":
        print("Your game session has closed, have a good day!")
        break

    elif user_input in directions:
        # move the hero have a try/except block for validation and error handling
        # try:
        hero.go_to_path(user_input)
        print(f"you move to the {user_input} room")

        # except:
        #     print(f"uInput {user_input}")
        #     print("There is no path in that direction")
    else:
        print("Invalid input, try again")