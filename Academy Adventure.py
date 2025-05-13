import random
from Endings import *
from Room import *
from Player import *
from Item import *
END_GAME=True
ALL_ROOMS={"room0":room0,"room1":room1,"room2":room2,"room3":room3,"room4":room4,"room5":room5,"room6":room6,"room7":room7,"room8":room8,"room9":room9,"room10":room10,"room11":room11,"room12":room12,"room13":room13,"room14":room14,"room15":room15,"room16":room16,"room17":room17,"room18":room18,"room19":room19,"room20":room20,"room21":room21,"room22":room22,"room23":room23,"room24":room24,"room25":room25}

#Generate levels
def generate_lvl_1(player=Player()):
    match player.current_room:
        case 0:
            if player.action == "search":
                print(f"Current Room: {room0.name}\n\
                      {room0.description}")
            else:
                pass
                 
        case 1:
            print("You go south. The door is a struggle to pull open. It grinds against the stone floor and you're surprised the wood doesn't fall apart under your hands. The room is swallowed in darkness.")
            if player.light == True:
                print(f"Current Room: {room1.name}\n\
                {room1.description}")
                if player.action == "search":
                    print(f"{room1.search_results}")
                else:
                    pass
            elif player.light == False:
                print(f"{room1.d_description}")  
                if player.action == "search":
                    print(f"{room1.d_search_results}")
                else:
                    pass
            else:
                pass

        case 2:
            if player.light == True:
                print(f"Current Room: {room2.name}\n\
                {room2.description}")
                if player.action == "search":
                    print(f"{room2.search_results}")
                else:
                    pass
            elif player.light == False:
                print(f"{room2.d_description}")
                if player.action == "search":
                    print(f"{room2.d_search_results}")
                else:
                    pass
            else:
                pass
        case 3:
            if player.light == True:
                print(f"Current Room: {room3.name}\n\
                {room3.description}")      
                if player.action == "search" and player.light == True:
                    print(f"{room3.search_results}")          
                #dark_room(player,room)
                else:
                    pass

            elif player.light == False:
                print(f"{room3.d_description}")
                if player.action == "search" and player.light == False:
                    print(f"{room3.d_search_results}")
                else:
                    pass
            else:
                pass

        case 4:
            if player.light == True:
                print(f"Current Room: {room4.name}\n\
                {room4.description}")

                #dark_room(player,room)
                if player.action == "search" and player.light == True:
                    print(f"{room4.search_results}")
                else:
                    pass

            elif player.light == False:
                print(f"{room4.d_description}")
                if player.action == "search" and player.light == False:
                    print(f"{room4.d_search_results}")
                else:
                    pass
            else:
                pass                
        case 5:
            if player.light == True:             
                print(f"Current Room: {room5.name}\n\
                {room5.description}")
                player.light = False
                if player.action == "search" and player.light == True:
                    print(f"{room5.search_results}")
                else:
                    pass
            else:
                pass
            
        case 6:
            print("\n\tThe Little Story of a Big Merc\n\t How are you supposed to do this with no armor or weapons? Maybe they stayed in the circle you first stepped through? Alas, they haven't. The mage is apologizing profusely and is no longer able to even hold the circle. You failed before you even started! You're reputation takes a blow, your purse takes a blow, and your self-esteem takes a blow.")
        case _:
            print("Out of Bounds")

def generate_lvl_2(player=Player()):
    match player.current_room:
        case 7:
            print(f"Current Room: {room7.name}\n\
                \t{room7.description}")
            if player.action == "search":
                print(f"{room7.search_results}")
        case 8:
            print(f"Current Room: {room8.name}\n\
                \t{room8.description}")
            if player.action == "search":
                print(f"{room8.search_results}")
        case 9:
            print(f"Current Room: {room9.name}\n\
                \t{room9.description}")
            if player.action == "search":
                print(f"{room9.search_results}")
        case 10:
            print(f"Current Room: {room10.name}\n\
                \t{room10.description}")
            if player.action == "search":
                print(f"{room10.search_results}")
        case 11:
            print(f"Current Room: {room11.name}\n\
                \t{room11.description}")
            if player.action == "search":
                print(f"{room11.search_results}")
        case 12:
            print(f"Current Room: {room12.name}\n\
                \t{room12.description}")
            if player.action == "search":
                print(f"{room12.search_results}")
        case 13:
            print(f"Current Room: {room13.name}\n\
                \t{room13.description}")
            if player.action == "search":
                print(f"{room13.search_results}")
        case 14:
            print(f"Current Room: {room14.name}\n\
                \t{room14.description}")
            if player.action == "search":
                print(f"{room14.search_results}")
        case 15:
            print(f"Current Room: {room15.name}\n\
                \t{room15.description}")
            if player.action == "search":
                print(f"{room15.search_results}")
        case 16:
            print(f"Current Room: {room16.name}\n\
                \t{room16.description}")
            if player.action == "search":
                print(f"{room16.search_results}")
        case 17:
            print(f"Current Room: {room17.name}\n\
                \t{room17.description}")
            if player.action == "search":
                print(f"{room17.search_results}")
        case _:
            print("Out of Bounds")

def generate_lvl_3(player=Player()):
    match player.current_room:
        case 18:
            print(f"Current Room: {room18.name}\n\
                \t{room18.description}")
            if player.action == "search":
                print(f"{room18.search_results}")
        case 19:
            print(f"Current Room: {room19.name}\n\
                \t{room19.description}")
            if player.action == "search":     
                print(f"{room19.search_results}") 
        case 20:
            print(f"Current Room: {room20.name}")
            room_seventeen(player)
            if player.action == "search":
                print(f"{room20.search_results}")                      
        case _:
            print("Out of Bounds")


#Summon Light
def summon_light(player=Player()):
    print("Do you want to summon your light?")
    lightChoice = input("> ")
    if lightChoice == "yes":
        print("A cool blue-gold light appears in your outstretched palm. It grows brighter, till the room is illuminated with its gentle glow. You gently lob it up, and it hangs above you, keeping east over your head as you walk.\n\
        \tWill you give your light ball companion a name?")
        nameChoice = input("> ")
        if nameChoice == "yes":
            print("It's a little weird you want to name a small ball of light, but this is always the way you've done things. It's your steadfast partner. The only one you can trust.")
            name = input("What is the ball of light's name?\t")
            print(f"{name} is a great choice!")
            player.light = True
        elif nameChoice == "no":
            print("Really? Name a ball of light? Psh. You're a strong, silent mercenary.")
            player.light = True
        else:
            print("Hmmm... do you want to give the ball of light a name or what? Yes or No?")
    elif lightChoice == "no":
        print("Odd, considering you don't have darkvision, but you do enjoy a challenge every now and then. You stumble across the floor, tripping on uneven stone tiles. You crash into...something...and would probably get a splinter if you hadn't managed to keep your gloves through that weird teleport. You grope until you find a door you don't think is the one you came through. Will you go through the door or try to go back the way you came? So, north or south?")    
    else:
        print("Was that a yes or a no?")

#Actions
def player_action(player=Player()):
    
    match player.action:
        case "go": #Go
            new_room_name = f"room" + str(player.current_room)
            room = ALL_ROOMS[new_room_name]
            room_choice(room,player)
            if player.current_room <= 6:
                generate_lvl_1(player)
            elif player.current_room > 6 and player.current_room <= 17:
                if player.current_room == 7:
                    print("\n\tDirections from the Hallway are now - 'door1', 'door2', 'door3', etc... 'door11'. \n")
                else:
                    pass
                generate_lvl_2(player)
            elif player.current_room > 17 and player.current_room <= 20:
                generate_lvl_3(player)
        case "search": #Search
            if player.current_room <= 6:
                generate_lvl_1(player)
            elif player.current_room > 6 and player.current_room <= 17:
                generate_lvl_2(player)
            elif player.current_room > 17 and player.current_room <= 20:
                generate_lvl_3(player)
        case "light":
            summon_light(player)
        case "return":
            kids_check(player)
            imperial_loss(player)
            determine_ending(player)
        case "quit":
            quit()
        case _:
            print("What were you going to do? Search, go, or light?")

#Room Choice

def room_choice(room=Room(),player=Player()):

    #Handles room movement based on player input and room connections in the direction the player wants to move (e.g., "north", "south", "east", "west").
    print("Which direction do you want to go?\t")
    direction=input("> ")

    if direction in room.connections:
        next_room_index=room.connections[direction]
        player.current_room=next_room_index
    else:
        print("There doesn't appear to be a door you can reach that way.")
              
#Random Room Generation if Player is in total darkness and is stupid and doesn't turn on light   

def dark_room(player=Player(),room=Room()):
    if player.light == False and room.light == False:
        if random.randint(1, 101) < 75:
            possible_destinations = [1,2,3,4]      
            random_direction = random.choice(possible_destinations)
            player.current_room = random_direction
        else:
            pass 
    else:
        print("The darkness is all encompassing. Maybe you need a light.") 
  
#Room17

def room_seventeen(player=Player()):
    description_parts=[]
    description_part2=" are waiting for you in the stairwell, quiet despite the raucous noise rising from the lower level. You all share a grim nod before looking down the stairs, gathering yourselves to face the fight below."
    if 9 in player.visited_rooms:
        description_parts.append="Artifice Professor"
    elif 10 in player.visited_rooms:
        description_parts.append="Herbology Professor, Scrying Professor"
    elif 12 in player.visited_rooms:
        description_parts.append="Bard Professor"
    elif 13 in player.visited_rooms:
        description_parts.append="Alchemy Professor, Trapmaster Professor, Spell Scribe Professor"
    elif 15 in player.visited_rooms:
        description_parts.append="Beast Lord Professor, Teleportation Professor"
    
    if player.visited_rooms <= 8:
        print("You walk into the stairwell and the eerie noise rises up from the floor below. After dealing with the unnatural silence of the Academy so far, it's unnerving to hear the raucous noise below.")
    else:
        print(description_parts+description_part2)

#Saved Kids
def kids_check(player=Player()):
    counter=0
    if 9 in player.visited_rooms:
        counter+=1
    elif 10 in player.visited_rooms:
        counter+=1
    elif 12 in player.visited_rooms:
        counter+=1
    elif 13 in player.visited_rooms:
        counter+=1
    elif 14 in player.visited_rooms:
        counter+=1
    elif 15 in player.visited_rooms:
        counter+=1
    else:
        print("Tracker Error: Visited Rooms")
    if counter == 6:
        player.saved_all_children=True
    else:
        print("Counter invalid")

#Imperial Check
def imperial_loss(player=Player()):
    if 19 in player.visited_rooms:
        player.fought_imperials=True
    else:
        player.fought_imperials=False

#Game Endings
     
def determine_ending(player=Player()):
    if player.saved_all_children == True and player.fought_imperials == True:
        endings(24)  # "A Big Man with an Old Soul"
    elif player.saved_all_children == True and player.fought_imperials == False:
        endings(22)  # "Did Your Job and Went Home With No Drama"
    elif player.saved_all_children == False and player.fought_imperials == True:
        endings(21)  # "Single-handedly Beat All Their Men"
    elif player.saved_all_children == False and player.fought_imperials == True and player.num_rooms_explored >= 8 and player.num_rooms_explored <= 18:
        endings(23) # "Dog. Just Dog."
    elif player.saved_all_children==False and player.fought_imperials==False and player.num_rooms_explored > 8 and player.num_rooms_explored <= 12:
        endings(25) # "How Long Have You Worked as a Merc, Anyway."

def character_creation(player=Player()):
              
    print('You are a mercenary that\'s been hired to go the back way into a magic Academy to save the Professors and Students that are still trapped on the second floor of the building. You\'re good at your job and are looking forward to those sweet gold coins weighing down your pockets, so you agree to go in the "back way". As you walk towards the person in charge who your handler told you to contact, they turn and look at you, asking,\n\t"You\'re here to help, right?"')
    
    answerPlayer=input("> ").lower().split()[0]
    
    if answerPlayer == "yes":
        print("Oh thank goodness! We've been waiting for you!\t")
    elif answerPlayer == "no":
        print("Disappointing. We're waiting for someone. Could you please move on?")
        quit()
    else:
        print("Sorry, I missed that. Was that a yes or no?\t")

    player.name=input("What's your name, Mercenary?\t")
    print(f"Well met, {player.name}!")

    job=input(f"What's your job, {player.name}? Swordlord, Pugilist, or Rogue?\t").lower()
    player.set_job(job)
    if player.job =="swordlord":
        print(f"Well met, Swordlord {player.name}! We're pleased you've agreed to help.\n\n")
    elif player.job=="pugilist":
        print(f"Well met, Pugilist {player.name}! We're pleased you've agreed to help.\n\n")
    elif player.job=="rogue":
        print(f"Well met, Rogue {player.name}! We're pleased you've agreed to help.\n\n")
    else:
        print("Sorry, I didn't catch that. Swordlord, Pugilist, or Rogue?\t")

def main():
    player = Player()
#Instructions
    print("""Welcome to Academy Chaos
    Save the professors and children stuck in the academy!

    Moves:
    go (available directions: north, south, west, east)
    search (searches current room)
    light (Turn on light)
    return (spell to take you out of the Academy)
    quit (to quit the game...quitter)\n\
    You might want to grab a pen and paper to help draw out the map.\n\
    Press Enter to continue...
    """)   
    input()
    
    character_creation(player)
    print("You step towards the nervous mage who is standing in front of a teleportation circle. It's glowing a weird lightish red color, which is not something you've seen before. You cautiously step into the circle and the world blinks for a moment, the sound of broken glass filling your ears, and the scent of rotten oranges in your nose. The world blinks back and you find yourself in your clothes. Somehow, that mage has managed to destroy your weapons and armor. You step from the circle, the lightish red glow giving the dank, musky air an eerie atmosphere. Your boots barely make noise on the stone floor with a thick layer of dirt and grim to cushion your steps. In the gloom, you can see a door that leads deeper.\n\
        Will you search the room? Go south? Go north?\n\t")
      
    player.action = input("> ")
    player_action(player)

    start_game(player)

#Game Loop
def start_game(player=Player()):

    while END_GAME:  # Single game loop
        print("Will you search the room? Go forth? Do you need a light? Or are you ready to use return spell?\n\t")
        player.action = input("> ")
        player_action(player)
    #Game Ending 

if __name__ == "__main__":
    main()
