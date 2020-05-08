from weapons import weapons

class Hero:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.gold = 0
        self.inventory = []
        # Item Mangment
        self.main_hand = weapons["rusty_dagger"]
        self.off_hand = []
        self.helmet = []
        self.armor = []
        # Stats
        self.max_HP = 100 
        self.current_HP = 100
        self.max_MP = 50
        self.current_MP = 50
        self.AC = 10 
        self.hit_mod = 0 + self.main_hand.hit_mod
    
    def go_to_path(self, direction):
        is_path = False

        for path in self.current_room.paths:
            if direction == path["direction"]:
                self.current_room = path['room']
                print(f"\nYou enter the {self.current_room}")
                print("\n\nInputs \n[N]orth [E]ast [S]outh [W]est [Q]uit [M]enu\n")
                is_path = True

        if is_path == False:
            print("You can't travel there!")

    def display_stats(self):
        print(f"HP:{self.current_HP}/{self.max_HP}   MP:{self.current_MP}/{self.max_MP}   AC:{self.AC}   Attack_Bonus:{self.hit_mod}")

    

    ## to-do list
    ## create methods to inspect rooms and fallen foes for items/loot

    ## create methods to interact with items

    ## Create methods to equip gear

    ## create methods to navigate inventory

    ## create methods for attacking and casting
    ##### add attack methods directly to the weapons

    ## how to have gear affect stats?
    ##### create methods that add the accumulated stat bonuses