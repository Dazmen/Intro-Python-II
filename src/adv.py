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


room['outside'].set_path('n', room['foyer']) 
room['foyer'].set_path("s", room['outside'])
room['foyer'].set_path("n", room['overlook'])
room['foyer'].set_path("e", room['narrow'])
room['overlook'].set_path("s", room['foyer'])
room['narrow'].set_path("w", room['foyer'])
room['narrow'].set_path("n", room['treasure'])
room['treasure'].set_path("s", room['narrow'])

#
# Main
#

hero_name = input("\n\n\nSelect your name Hero!: ")
hero = Hero(hero_name, room['outside'])



directions = ['n', 'e', 's', 'w']

print(f"\n\n\n{hero.name}, you start your journey here")
print(f"\n{hero.current_room}")
print("\n\nInputs \n[N]orth [E]ast [S]outh [W]est [Q]uit")

while True:
    user_input = input("\nChoose your action: ").lower()

    if user_input == "q":
        print("Your game session has closed, have a good day!")
        break

    elif user_input in directions:
        hero.go_to_path(user_input)

    else:
        print("Invalid input, try again")