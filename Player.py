#Imported defined functions
from Item import *
from Room import *

#Player Classes

class Player:

    def __init__(self):
        self.name = ''
        self.job = ''
        self.light = False
        self.stats = {"health": 10, "mana": 10, "defense": 0, "attack": 1}
        self.inventory = []
        self.equipped = {"head": None, "body": None, "weapon": None, "feet": None}
        self.visited_rooms = []
        self.saved_all_children = False
        self.fought_imperials = False
        self.num_rooms_explored = 1
        self.current_room = 0

    def apply_indigestion(self):
        print(f"{self.name} feels an uncomfortable rumbling in their stomach.")

    def set_job(self, job):
        self.job = job
        match self.job:
            case "swordlord":
                self.stats["health"] += 40
                self.stats["mana"] += 20
                self.stats["defense"] += 2
                self.stats["attack"] += 2
            case "rogue":
                self.stats["health"] += 30
                self.stats["mana"] += 15
                self.stats["defense"] += 1
                self.stats["attack"] += 3
            case "pugilist":
                self.stats["health"] += 40
                self.stats["mana"] += 10
                self.stats["defense"] += 2
                self.stats["attack"] += 2

    def add_visited_room(self,room_index):
        if room_index not in self.visited_rooms:
            self.visited_rooms.append(room_index)
        else:
            pass

    def equip(self, item=Item): 
        if item not in self.inventory:
            print(f"'{item}' not found in inventory.")
            return

        for slot in item.equip_slots:
            if slot not in self.equipped:
                print(f"'{item}' cannot be equipped.")
                return

            if self.equipped[slot] is not None:
                print(f"You already have an item equipped in the '{slot}' slot.")
                return

            if item.required_job == self.job:
                print(f"You must be a {self.job} to equip {item}")
                return

            self.equipped[slot] = item
            self.inventory.remove(item)
            print(f"'{item}' equipped in the '{slot}' slot.")

    def unequip(self, item):
        for slot in self.equipped:
            if self.equipped[slot] == item:
                self.equipped[slot] = None
                self.inventory.append(item)
                print(f"'{item}' unequipped from the '{slot}' slot.")
    def summon_light(self,room=Room()):
        lightChoice = input("> ").lower().strip()
        if (lightChoice == "yes"):
            self.light = True
            self.current_room = room
            print("A cool blue-gold light appears in your outstretched palm. It grows brighter, till the room is illuminated with its gentle glow. You gently lob it up, and it hangs above you, keeping right over your head as you walk.\n\
            \tWill you give your light ball companion a name?")
            nameChoice = input("> ")
            if (nameChoice == "Yes"):
                print("It's a little weird you want to name a small ball of light, but this is always the way you've done things. It's your steadfast partner. The only one you can trust.")
                name = input("What is the ball of light's name?")
                print(f"{name} is a great choice!")
                self.light = True
            elif nameChoice == "No":
                print("Really? Name a ball of light? Psh. You're a strong, silent mercenary.")
                self.light = True
            else:
                print("Hmmm... do you want to give the ball of light a name or what? Yes or No?")
        elif (lightChoice == "no"):
            print("Odd, considering you don't have darkvision, but you do enjoy a challenge every now and then. You stumble across the floor, tripping on uneven stone tiles. You crash into...something...and would probably get a splinter if you hadn't managed to keep your gloves through that weird teleport. You grope until you find a door you don't think is the one you came through. Will you go through the door or try to go back the way you came? So, up or down?")
            self.current_room = room
        else:
            print("Was that a yes or a no?") 