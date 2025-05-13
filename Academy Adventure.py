import os
import random
import Item.py
import Player.py
import Room.py

def clear():
    os.system("cls" if os.name == "nt" else "clear")

#Mobs and Boss
class Enemy:
    def __init__(self, monster):
        self.name = ''
        self.monster = monster
        self.stats = {"health": 10, "attack": 1, "defense": 0}
        
    def assign_mob(self, monster): #added self.
        match monster:
            case 1:
                self.name = "Imperial Gunner"
                self.monster = monster
                self.stats = {"health": 45, "attack": 5, "defense": 1}
            case 2:
                self.name = "Imperial Automaton"
                self.monster = monster
                self.stats = {"health": 60, "attack": 8, "defense": 5}
            
    def assign_boss(self, boss): #added self.
        match boss:
            case 1:
                self.name = "Imperial Centurion"
                self.monster = boss
                self.stats = {"health": 75, "attack": 10, "defense": 4}

#Directions

def process_direction():
    direction=input("> ").lower().strip()
    if direction in ["up","down","left","right"]:
        return direction
    else:
        print("An interesting suggestion, but you aren't capable of going that 'direction'.")

#Room Choice

def room_choice(room=Room(),player=Player()):

    #Handles room movement based on player input and room connections in the direction the player wants to move (e.g., "up", "down", "right", "left").

    current_room=room.index
    direction=input("> ").lower().split()

    if direction == "up": #check for direction availble
        if room.connections["up"]:
            #generate next room 
            #tell player about room
            next_room_index=room.connections["up"]
            next_room=room.description
        else: #rebuke player            
            print("Seems there's no accessible door in that direction.")
    elif direction =="down":
            #check for direction availble
        if room.connections["down"]:
            #generate next room 
            #tell player about room
            next_room_index=room.connections["down"]
            next_room=room.description
        else:
            #rebuke player
            print("Seems there's no accessible door in that direction.")
    elif direction =="left":
            #check for direction availble
        if room.connections["left"]:
            #generate next room 
            #tell player about room
            next_room_index=room.connections["left"]
            next_room=room.description
        else:
            #rebuke player
            print("Seems there's no accessible door in that direction.")
    elif direction=="right":
            #check for direction availble
        if room.connections["right"]:
            #generate next room 
            #tell player about room
            next_room_index=room.connections["right"]
            next_room=room.description
        else:
            #rebuke player
            print("Seems there's no accessible door in that direction.")
    else:
        print("An interesting suggestion, but you aren't capable of going that 'direction'.")
    
    if current_room:
        next_room_index=room.connections

        if next_room_index:
          next_room=room(next_room_index)
          if next_room:
            player.current_room = next_room_index
            print(f"You are now in {next_room["name"]}.")
            print(next_room["description"])
            return next_room_index
          else:
            print("Seems there's no accessible door in that direction.")
            return room.index # player stays in same room.
        else:
            print("Seems there's no accessible door in that direction.")
            return room.index # player stays in same room.
        
    #Random Room Generation if Player is in total darkness and is stupid and doesn't turn on light
    elif player.light == False and room.light == False:
        if random.randint(1, 101) < 75:
            possible_destinations = [1, 2, 3, 4]
            next_room_index = current_room["connections"][random_direction]                 
            random_direction = random.choice(possible_destinations)
            print("The darkness is all encompassing. Did you even move to another room? Are you still in the same place? Maybe you need a light.")  
        else:
            print("The darkness is all encompassing. Did you even move to another room? Are you still in the same place? Maybe you need a light.") 
    else:
        print("The darkness is all encompassing. Did you even move to another room? Are you still in the same place? Maybe you need a light.") 
        return current_room # player stays in same room.

#Room Search
def search_room(room=Room(),player=Player()):
    current_room=player.current_room
    if current_room:
        print(player.current_room["search_results"])
    else:
        print("You can't do that, {player.name}.")

#Checking for Room Items

def check_room_items(room=Room(),item=Item()):

    if room.items:
        for item.name in room.items:
            print("item.name")
        else:
            pass
    else: 
        None

#Picking up Items

def get_item(player=Player(),room=Room(),item=Item()):
  item = check_room_items(room, item)
  if item:
    if item not in player.inventory:
      player.inventory.append(item)
      room.items.remove(item)
      return f"You picked up {"item.name"}!"
    else:
      return f"{"item.name"} is already on your person."
  else:
    return f"Can't find {"item.name"}."

#Game Endings     
def determine_ending(player=Player()):

    if player.saved_all_children == True and player.fought_imperials == True:
        return 24  # "A Big Man with an Old Soul"
    elif player.saved_all_children == True and player.fought_imperials == False:
        return 22  # "Did Your Job and Went Home With No Drama"
    elif player.saved_all_children == False and player.fought_imperials == True:
        return 21  # "Sing-handedly Beat All Their Men"
    elif player.saved_all_children == False and player.fought_imperials == True and player.num_rooms_explored > 1:
        return 23 # "Dog. Just Dog."
    elif player.saved_all_children==False and player.fought_imperials==False and player.num_rooms_explored > 1:
        return 25 # "How Long Have You Worked as a Merc, Anyway."

if __name__ == "__main__":

    def character_creation(player=Player()):
              
        print('You are a mercenary that\'s been hired to go the back way into a magic Academy to save the Professors and Students that are still trapped on the second floor of the building. You\'re good at your job and are looking forward to those sweet gold coins weighing down your pockets, so you agree to go in the "back way". As you walk towards the person in charge who your handler told you to contact, they turn and look at you, asking, "You\'re here to help, right?"')
        
        answerPlayer=input("> ").lower().split()
        
        if answerPlayer=="yes":
            print("Oh thank goodness! We've been waiting for you!\t")
        elif answerPlayer=="no":
            print("Disappointing. We're waiting for someone. Can you please move on?")
            quit()
        else:
            print("Sorry, I missed that. Was that a yes or no?\t")
            return

        player.name=input("What's your name, Mercenary?\t")
        print(f"Well met, {player.name}!")

        job=input(f"What's your job, {player.name}? Swordlord, Pugilist, or Rogue?\t").lower().strip()
        player.set_job(job)
        if player.job=="swordlord":
            print(f"Well met, Swordlord {player.name}! We're pleased you've agreed to help.")
        elif player.job=="pugilist":
            print(f"Well met, Pugilist {player.name}! We're pleased you've agreed to help.")
        elif player.job=="rogue":
            print(f"Well met, Rogue {player.name}! We're pleased you've agreed to help.")
        else:
            print("Sorry, I didn't catch that. Swordlord, Pugilist, or Rogue?\t")

def main(player = Player()):
#Instructions
    print("""Welcome to Academy Chaos
    Save the professors and children in the academy!

    Moves:
    {direction} (Up, Down, Left, Right, circle)
    get {item} (adds nearby item to inventory)
    search (searches current room)
    use {item} (uses items)
    equip {item} (Equips items)
    light (Turn on light)
    Press Enter to continue...
    """)   
    input()

    
    character_creation(player=Player())
    player.inventory=[]
    player.saved_all_children=False
    player.fought_imperials=False
    player.num_rooms_explored=1
    start_game()

def start_game(player=Player(),room=Room(),item=Item()):

    while True:  # Single game loop

        current_room=room[player.current_room]
        print(current_room["description"])
        player.inventory=[]

        action = input("> ").lower().strip()
        if action == "light":
            player.light = True
            print(current_room["room.name"])
            print(current_room["room.description"])

        elif action == "Get":  # Item pick up logic.
            if current_room:
                item_found = False
                for room_items in current_room["items"]:
                    item.name = room_items
                    if room.items == room_items:
                        if room_items not in player.inventory:
                            player.inventory.append(room_items)
                            msg = f"You picked up {room_items[item.name]}!"
                            room.items.remove(room_items)
                        else:
                            msg = f"{room_items[item.name]} is already on your person."
                        item_found = True
                        break
                if not item_found:
                    msg=(f"Can't find {item}.")
            else:
                msg = f"There are no items to get here."
            print(msg)
        elif action == "search":
            print(player.current_room["search_results"])
            break
        
        elif action == "Exit":
            break

        else:
            msg = f"You can't do that, {player.name}."
            print(msg)

if __name__ == "__main__":
    main()