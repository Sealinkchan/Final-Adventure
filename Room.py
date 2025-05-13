import random
import Item.py
import Player.py

#Map

class Room:
    
    def __init__(self, index=0, light=False, name="", description="", search_results="", exit=False, enemies=0, connections=None, items=None,  end_game=False):
        self.index = index
        self.light = light
        self.name = name
        self.description = description
        self.search_results = search_results
        self.exit = exit
        self.enemies = enemies
        self.connections = connections if connections else {}
        self.items = items if items else []
        self.end_game = end_game

# Create Items

leather_armor = Item(name="Leather Armor Set of the Forgotten", description="Leather Armor Set that has somehow survived in the basement under the Academy for an untold number of years.", equipable=True, equip_slots=["head", "body", "feet"], health_bonus=5, defense_bonus=2)
potion = Item(name="Unknown Potion", description="Of dubious age, original effect, and viscous. You're not really gonna drink this are you?", equipable=False, health_bonus=-20, mana_bonus=-20)

# Create Room Objects

room0 = Room(index=0,light=True,
    name="Basement Teleportation Circle Room",
    description="The lightish red glow giving the dank, musky air an eerie atmosphere. Your boots barely make noise on the stone floor with a thick layer of dirt and grim to cushion your steps.",
    search_results="Any furniture that adorned this room has long turned to dust. The only reason the teleportation circle even worked seems to be due to it being carved directly into the stone. In the gloom, you can see a door directly in front of you, leading down.",
    exit=True, connections={"down": 1, "up": 20})
room1 = Room(index=1,light=False,
    name="Old Storage Room",
    connections={"up": 0, "down": 2},)
room2 = Room(index=2,light=False,
    name="Basement Hallway",
    connections={"up": 1, "down": 3, "left": 4, "right": 5}, items=[leather_armor])
room3 = Room(index=3,light=False,
    name="Old Religious Studies Classroom",
    connections={"left": 2})
room4 = Room(index=4, light=False,
    name="Old Potions Classroom",
    connections={"right": 2}, items=[potion],)
room5 = Room(index=5,light=True,
    name="Basement Teleportation Circle Exit",
    connections={"left": 2, "down": 7})
room6 = Room(index=6,name="The Little Story of a Big Merc",
    connections={"down": 0},
    end_game=True)

def generate_lvl_1(room=Room(),player=Player()):
    msg = " "
    match room.index:
        case 0:
            print("Current Room: {room.name}\n\n\
            You step towards the nervous mage who is standing in front of a teleportation circle. It's glowing a weird lightish red color, which is not something you've seen before. You cautiously step into the circle and the world blinks for a moment, the sound of broken glass filling your ears, and the scent of rotten oranges in your nose. The world blinks back and you find yourself in your clothes. Somehow, that mage has managed to destroy your weapons and armor. You step from the circle, the lightish red glow giving the dank, musky air an eerie atmosphere. Your boots barely make noise on the stone floor with a thick layer of dirt and grim to cushion your steps. In the gloom, you can see a door that leads deeper.\n\
            \tWill you go up into the circle or go down?")
            user_input = input("> ").lower().strip()
            
            #"The Little Story of a Big Merc" Ending
            if user_input == 'up':
                print("You step back through the teleportation circle. How are you supposed to do this with no armor or weapons? Maybe they stayed in the circle you first stepped through? Alas, they haven't. The mage is apologizing profusely and is no longer able to even hold the circle. You failed before you even started! You're reputation takes a blow, your purse takes a blow, and your self-esteem takes a blow."),
                quit()

            elif(user_input == "down"):
                print("You go down. The door is a struggle to pull open. It grinds against the stone floor and you're surprised the wood doesn't fall apart under your hands. The room is swallowed in darkness. Will you summon a light or continue blindly forward?")
                player.summon_light()                         
            else:
                print("No can do! Down or up?")
                return room0

        case 1:
            if player.light:
                print(f"Current Room: {room.name}")
                room1.description = "The storeroom has been destroyed by fire. Charred shelves, burst pots, and broken crates are all that have been left here. The stone tiles have cracked and buckled from the heat."
                room1.search_results = "There is nothing salvageable here."
                
            else:
                room1.description = "You can faintly smell smoke in the air, but the room seems darker than you anticipated. You can walk in, but the glow of the circle behind you doesn't pierce through the darkness."
                room1.search_results = "You see nothing, but you fall into piles of something gritty and smooth when you trip on the broken stone tiles."

        case 2:
            if player.light:
                print(f"Current Room: {room.name}")
                room2.description = "Scraps of cloth cling to bars along the ceiling, remnants of banners or tapestries that used to decorate the hallway. The air is still, your careful movements disturbing the grave-like atmosphere."
                room2.search_results = "Any furniture that adorned this hallway has crumbled to dust or barely holds together. Something catches your eye among what seemed to be armor stands. You squat down, reaching through the disintegrating wood and feel something smooth and firm. You pull out a full set of leather armor. How it was still useable after so many years is beyond you. It's obviously enchanted. There are one door leading up, that which you've come through, one leading down, one to the left, and one to the right."
            else:
                room2.description = "Smells musty and the air is cold, but you can't see anything."
                room2.search_results = "You run your hand against the grimy wall to keep track of where you're going. You trip over piles of...something...a lot while attempting to find a door. You do find three other doors, but you don't know which one to take."

        case 3:
            if player.light:
                print(f"Current Room: {room.name}")
                room3.description = "The room is a mess. Shadows lengthen and shrink as you move through. The stones are uneven and you carefully make your way across them so you don't trip."
                room3.search_results = "Destroyed desks and casks in heaps in the corners and along the walls. Ruined religious relics crumbling in the debris. There is nothing of import that you can see. There is no other door other than the one you entered from."
            else:
                room3.description = "Smells musty and the air is cold, the darkness pressing against you."
                room3.search_results = "You run your hand against the grimy wall to keep track of where you're going. You trip over piles of...something...a lot while attempting to find a door. You can't keep close to the wall. You stumble over rotting wood...things, losing your sense of direction. You do find one door, but you don't know if it's the one you came in through."
                possible_destinations = [2, 3]
                if random.randint(1, 101) < 75:
                    random_destination = random.choice(possible_destinations)
                    print("The darkness is all encompassing. Did you even move to another room? Are you still in the same place?")
                return random_destination
        case 4:
            if player.light:
                print(f"Current Room: {room.name}")
                room4.description = "There's broken glass and piles of rotten wood that used to be desks scattered around the room. There's a strange scent in the air, mingling with the dust that's been disturbed by your entrance."
                room4.search_results = "There's a few potion bottles that have survived the years, but only one of which has anything inside of it. It's a viscous liquid that's yellow, shifting to red and blue in the light. There's no other door other than the one you entered through."
            else:
                room4.description = "Smells musty and odd, almost like the ghost of decomposing plants and chemicals, but you can't see anything."
                room4.search_results = "You can't even reach the wall. Glass cracks beneath your boots. Keeping your footing is interesting and you bump into things at waist level that double you over. You do find a door, but you don't know if it's the one you came in through."
                possible_destinations = [2, 4]
                if random.randint(1, 101) < 75:
                    random_destination = random.choice(possible_destinations)
                    print("The darkness is all encompassing. Did you even move to another room? Are you still in the same place?")
                return random_destination
        case 5:
            if player.light:
                print(f"Current Room: {room.name}")
                room5.description = "The circle in this room is the green that you're used to seeing. It shimmers in the floor it's set into. Your light winks out with a thought, knowing you'll be in the Academy proper soon."
                room5.search_results = "The room is bare of any other adornment. Not even the piles of debris are present that existed, if they ever existed to begin with."
                player.light = False
        case 6:
                print("How are you supposed to do this with no armor or weapons? Maybe they stayed in the circle you first stepped through? Alas, they haven't. The mage is apologizing profusely and is no longer able to even hold the circle. You failed before you even started! You're reputation takes a blow, your purse takes a blow, and your self-esteem takes a blow.")
                player.current_room = room20

# Create Item Objects

celestial_wine = Item(name="Celestial Wine", description="A little taste of where Angels dwell. Too bad you'll be too trashed to enjoy past the first sip.", equipable=False, health_bonus=-5, mana_bonus=15, defense_bonus=2)
blood_wine = Item(name="Blood Wine", description="Feeling a little iron deficient? This is not the way to fix that.", equipable=False, health_bonus=15, mana_bonus=-5, attack_bonus=2)
gerren_sword = Item(name="Gerren's Enchanted Long Sword", description="Gerren worked really hard to enchant this sword! It's a plain looking sword, but its edges are sharp!", equip_slots="weapon", equipable=True, health_bonus=2, defense_bonus=1, attack_bonus=5)
lottie_gloves = Item(name="Lottie's Enchanted Pugilist Gloves", description="Lottie worked really hard on these! They're heavier than they look...what did Lottie put in these?!", equip_slots="weapon", equipable=True, health_bonus=2, defense_bonus=1, attack_bonus=5)
rylie_dagger = Item(name="Rylie's Enchanted Dagger Pair", description="Rylie worked really hard on these! They both have colored hilts wrought of wood with vines around the hilt. The color choice is a bit off...one is red and the other is green...", equip_slots="weapon", equipable=True, health_bonus=2, defense_bonus=1, attack_bonus=5)
poultice = Item(name="Health Poultice", description="This poutice will heal for 10 HP. Pretty good for a student!", equipable=False, health_bonus=10) 
tar_bomb = Item(name="Tar Bomb", description="Eats through attack and defense!", equipable=False, defense_bonus=-1, attack_bonus=-2)
erosion_bomb = Item(name="Erosion Bomb", description="Eats health! Even metal foes are not safe!", equipable=False, health_bonus=-8)
armor_potion = Item(name="Armor Potion", description="Ups Defense by 3 for 10 minutes!", equipable=False, defense_bonus=3)
attack_potion = Item(name="Attack Potion", description="Ups Attack Power by 3 for 10 minutes!", equipable=False, attack_bonus=3)
whirlwind_scroll = Item(name="Whirlwind Scroll", description="Need to clear the air? This is the best way to do it! You can use spellscrolls even where there is anti-magic fog in the air.", equipable=False, mana_bonus=-15)

# Create Room Objects

room7 = Room(index=7, name="Second Floor Hallway",
                description="There's the cloying scent of boiled cabbage in the air, a magic nullifying weapon created by the Imperium. This tool was why the Academy was overrun. None of the Professors could easily use any spell that wouldn't destroy the building to punch through the anti-magic fog.",
                search_results="There are plaques with the room numbers hanging over the ten doors along the hallway, five on each side. 2-6, 2-7, 2-8, 2-9, 2-10, 2-11, 2-12, 2-13, 2-14, 2-15. Beyond that, the hallway is pretty bare of adornment. There are some corpses in Imperial uniforms, though they have nothing of note left on them.",
                connections={"up": 8, "down": 9, "up": 10, "down": 11, "up": 12, "down": 13, "up": 14, "down": 15, "up": 16, "down": 17}, items=[])
room8 = Room(index=8, name="Teleportation Classroom 2-15",
                description="The room is bright! There are no windows, but the mage lights glow strongly. It's obvious that there was a rush to leave this room, as the chairs and desks are haphazardly moved out of the way.",
                search_results="There are plaques with the room numbers hanging over the ten doors along the hallway, five on each side. 2-6, 2-7, 2-8, 2-9, 2-10, 2-11, 2-12, 2-13, 2-14, 2-15. Beyond that, the hallway is pretty bare of adornment. There are some corpses in Imperial uniforms, though they have nothing of note left on them." ,
                connections={"down": 7, "up": 5}, items=[celestial_wine, blood_wine])
room9 = Room(index=9, name="Artifice Classroom 2-14",
                description = "The room has artifice tools, weapons, and miscellaneous gear strewn all over scarred tables with stools haphazardly set about the room in various states of position. There is a Professor and five young students in the far corner of the classroom. They look wary until they see that you're obviously not from the Imperial Army. The smell of cabbage is thick in here. You don't think you'll be able to eat it again. You inform the Artifice Professor that the Teleportation Circle in the Teleportation Classroom is active and will take them to the basement floor where they can teleport to the outside. He nods, tells you that he will ensure the students exit the danger zone, then will return and wait for you in the stairwell if you're going to face the Imperial forces that are on the first floor. He also invites you to anything you could use from the classroom.",
                search_results = "There are quite a few nice pieces of equipment, but nothing is a full armor set. There's an enchanted sword, a set of enchanted pugilist gloves, and a pair of enchanted daggers that catch your eye. Other than that, the rest of the finished gear is too weak or have enchantments that wouldn't help you. Though why someone would want a helm that turns all sound heard to kitten mews, you have no idea. There is nothing more in the classroom of note.",
                connections={"up": 7}, items=[gerren_sword, lottie_gloves, rylie_dagger])
room10 = Room(index=10, name="Herbology Classroom 2-13",
                description = "The Herbology room is the only one so far that doesn't reek of cabbage. The heavy scent of earth, fertilizer, and growing things permeates the air. There are two professors and nine young students among the plants. You nearly get something chucked at you before you call out that you were friend and not foe. You inform the professors of the escape route. The Herbology Professor goes to lead the students to safety, promising to return and wait for you in the stairwell if you're going to challenge the Imperials downstairs. The Scrying Professor offers to do the same, as they will be taking up the rear to ensure the children don't wander off.",
                search_results = "There is a riot of greenery existing in every nook and cranny of the room. You find three herbal poultices that would help with healing in a pinch. Everything else is in the raw form, which you don't have the experience of knowledge to make use of.",
                connections={"down": 7}, items=[poultice])
room11 = Room(index=11, name="Scrying Classroom 2-12",
                description = "This room is a similar state of disarray that you've encountered thus far. Thick velvet curtains are draped around the room, softening and masking the stone walls with the thick purple fabric. It was even a few degrees warmer in here, making the chill in the air disappear.",
                search_results = "There are no students or professors hiding in this room. There are some scrying implements and tools, but you have no need for them. You do find a few notes that were obviously being passed between students, but nothing else interesting.",
                connections={"up": 7}, items=[])
room12 = Room(index=12, name="Bardic Classroom 2-11",
                description = "There are many instruments in the room. It's impressive that so many could fit! The walls are also lined with soft velvet, in addition to the ceiling and floor. The Bardic Professor and three young students are in the cabbage scented room. You tell them it's safe to get the children out of the academy. The Bardic Professor offers to help you when they're done escorting the students and will meet you in the stairwell, if you'll have them.",
                search_results = "There is nothing of note that you can use to your advantage in this room.",
                connections={"down": 6}, items=[])
room13 = Room(index=13, name="Trap Making Classroom 2-10",
                description = "The Trap Making Classroom makes you nervous enough that you knock before entering. Good thing you did! There are two professors holding sharp and heavy implements that would not feel good! The Alchemy Professor, Trapmaster Professor, and Spell Scribe Professor listen raptly as you bring them up to speed. They have fifteen students to corral, telling you that they'll join you in the stairwell if you are going to take on the fight downstairs.",
                search_results = "A quick search gives you a tar bomb and a rust bomb. There's nothing else you can make do with on the fly.",
                connections={"up": 6}, items=[tar_bomb, erosion_bomb])
room14 = Room(index=14, name="Alchemy Classroom 2-9",
                description = "The classroom is a little warmer than you were expecting. There are strange instruments that localize the flame in a small area under small glass cauldrons. Various liquids of interesting shades and hues are on the shelves. The classroom looked empty, but you could feel the presence of others regardless. You call out that you're here to get them out. That their professor was already making their way to the teleportation circle in the basement. Six heads pop out of various places, blinking owlishly before lining up in front of you like ducklings.",
                search_results = "There are no finished potions according to the students. There is only one Armor and Attack Potion made by the professor. The rest are dubious at best. The students wouldn't swear to the quality of any of the others. You decide that maybe you should skip out on trying random potions...",
                connections={"down": 7}, items=[armor_potion, attack_potion])
room15 = Room(index=15, name="Beast Studies Classroom 2-8",
                description = "You knock on the Beast Classroom, unsure what to expect when you break the lock to open the door. Two professors stand with eight more students. There are some angry guard beasts that relax when the Beast Lord Professor gives the command. You fill them in on the goings on. The Beast Lord Professor and the Teleportation Professor look at each other and nodding. They round all the students up, promising to meet you in the stairwell if you were going to take on the battle below.",
                search_results = "There isn't anything fit for consumption in this room for you. There are plenty of stat buffing items, but they're made for animals and monsters, not fit for consumption by anyone else.",
                connections={"up": 7}, items=[])
room16 = Room(index=16, name="Spell Writing Classroom 2-7",
                description = "You easily get through the final door on this side of the hallway. The room is cozy, smelling of ink and parchment. Glass pens are carefully stored next to inkwells. Rolls of scrolls are stuffed in the cubby shelves. Books are haphazardly stacked on every other surface that isn't a student's desk.",
                search_results = "Spell scrolls are usable to anyone with the ability to use magical devices, which you can. You don't have all day to look very hard, so you rifle through the tags of completed spell scrolls. You find a lot of spell scrolls that are passable, but not really something you can use. Sin You do strike gold when you find a wind spell that could be very useful in clearing the air... ",
                connections={"down": 7}, items=[whirlwind_scroll])
room17 = Room(index=17, name="Stairwell 2-6",
                description="You walk into the stairwell and the eerie noise rises up from the floor below. After dealing with the unnatural silence of the Academy so far, it's unnerving to hear the rabble noise below.",
                search_results="There's nothing really of note, except a picture of a landscape. Very classy.",
                connections={"up": 7}, items=[])
room22 = Room(name="Did Your Job and Went Home With No Drama",
              description="You got all the children and professors out of the Academy. You did decide against facing off with the Imperials, though. Your reputation takes no hit as a whole, but the Professors that wanted to take on the Imperials don't think much of you. The Professors still took a 'scorched earth' approach, just leveing the building since there was no on the inside to take on the Imperials. You get a tidy sum.",
              end_game=True)
room25 = Room(name="How Long Have You Worked as a Merc, Anyway.",
              description="You got some children and professors out of the Academy. You did decide against facing off with the Imperials, though. Your reputation takes a small hit and the Professors that wanted to take on the Imperials don't think much of you. Not to mention the Professors and the parents of the children you didn't bother to save. The Professors come up with a plan together while you get paid a portion of what you were offered, as you didn't finish the job completely. You're ushered off the grounds and will see a dip in work for a while.",
              end_game=True)

def generate_lvl_2(room=Room(),player=Player()):
   
    match room.index:

        case 7:
            return room7
        case 8:
            return room8
        case 9:
            return room9
        case 10:
            return room10
        case 11:
            return room11
        case 12:
            return room12
        case 13:
            return room13
        case 14:
            return room14
        case 15:
            return room15
        case 16:
            return room16
        case 17:
            description_parts = []
            if 9 in player.visited_rooms:
                description_parts.append("Artifice Professor")
            if 10 in player.visited_rooms:
                description_parts.append("Herbology Professor, Scrying Professor")
            if 12 in player.visited_rooms:
                description_parts.append("Bard Professor")
            if 13 in player.visited_rooms:
                description_parts.append("Alchemy Professor, Trapmaster Professor, Spell Scribe Professor")
            if 15 in player.visited_rooms:
                description_parts.append("Beast Lord Professor, Teleportation Professor")
            if description_parts:
                room17.description = " are waiting for you in the stairwell, quiet despite the raucous noise rising from the lower level. You all share a grim nod before looking down the stairs, gathering yourselves to face the fight below.".join(description_parts)
            else:
                room17.description = "You walk into the stairwell and the eerie noise rises up from the floor below. After dealing with the unnatural silence of the Academy so far, it's unnerving to hear the raucous noise below."
            return room17
        case 22:
            return room22
        case 25:
            return room25
        
#Create Room Objects for Level 3

room18 = Room(name="First Floor Stairwell",
            description="It's rather noisy, masking your footsteps as you go down the stairs. The ground level stairwell is clean and maintained.",
            search_results="There is nothing of note except the large double doors that lead to the Main Lobby.",
            connections={"up": 17, "left": 19}, items=[])
room19 = Room(name="Main Lobby",
            description="The Academy lobby has quite a few invaders inside of it. It looks like the Centurian in charge is also in there. They thought they could take the school hostage since the young students would keep the retaliation down.",
            search_results="That cabbage scent is thick in this room! They have stripped anything of note and tossed it in the corner. Maybe the grunts got bored while negotiations are underway?",
            connections={"down": 20, "right": 18})
room20 = Room(name="Academy Foyer",
            description="The entry to the Academy and where any parents and students would get a glowing first impression on a normal day.",
            search_results="It's a mess! But certainly because of the soldiers, as opposed to the fault of the whoever keeps the Academy clean. The paintings of the Professors and Dean are hanging up along the walls that lead to the exit.",
            exit=True, connections={"up": 19}, items=[])
room21 = Room(name="Sing-handedly Beat All Their Men",
              description="You manage to kill off the Imperials that were wrecking havok on the Academy. The one who hired you is pleased, but would have been happier if you'd gotten the children out before you started the fight. That's the whole reason they hired you, after all. You get a tidy sum, anyway. Your reputation doesn't suffer either.",
              end_game=True)
room23 = Room(name="Dog. Just Dog.",
              description="Some Professors got to help, but others didn't, because you didn't feel like going through all the classrooms. The one who hired you had mixed feelings. You did get some of the children out, but you didn't get them all out before facing off with the Imperials. The left out Professors are very sour towards you. Your reputation doesn't suffer, however, and you get a tidy sum.",
              end_game=True)
room24 = Room(name="A Big Man with an Old Soul",
              description="You and the Professors took no prisoners. Not only did you save all the children, you cleared out the school of the invading Imperials! Your reputation skyrockets and you get a nice bonus from the student's parents. You get to keep all the stuff you picked up, too. A satisfying ending to a job that was a little more complicated than you were expecting.",
              end_game=True)

#generate_lvl_3 Function

def generate_lvl_3(room=Room()):
    match room.index:
        case 18:
            return room18
        case 19:
            return room19
        case 20:
            return room20
        case 21:
            return room21
        case 23:
            return room23
        case 24:
            return room24