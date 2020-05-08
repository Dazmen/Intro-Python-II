from rooms_file import room
from player import Hero

# Character Creation and Intro
hero_name = input("\n\n\nSelect your name Hero!: ")
hero = Hero(hero_name, room['outside'])

print(f"\n\n\n{hero.name}, you start your journey here")
print(f"\n{hero.current_room}")
print("\n\nInputs \n[N]orth [E]ast [S]outh [W]est [Q]uit [M]enu")

directions = ['n', 'e', 's', 'w']

# Menu Loop/controller
def menu():
    while True:
        user_input = input("View: [I]ventory [E]quipped-Items or [Ex]it-menu: ").lower()

        if user_input == "ex":
            break
        elif user_input == "i":
            print('INV feature not implemented yet!')
            break
        elif user_input == "e":
            print("EQUP feature not implemented yet!")
            break
        else:
            print("Invalid Input! Try Again...")

# Main Loop/controller
while True:
    user_input = input("\nChoose your action: ").lower()

    if user_input == "q":
        print("Your game session has closed, have a good day!")
        break

    elif user_input in directions:
        hero.go_to_path(user_input)

    elif user_input == "m":
        menu()
        
    else:
        print("Invalid Input! Try Again... ")

    hero.display_stats()