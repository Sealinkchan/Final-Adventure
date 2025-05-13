from Item import *

#Map

class Room:
    
    def __init__(self, index=0, light=False, name="", description="", d_description="", search_results="", d_search_results="", connections={}, items=[]):
        self.index = index
        self.light = light
        self.name = name
        self.description = description
        self.d_description = d_description
        self.search_results = search_results
        self.d_search_results = d_search_results
        self.connections = connections
        self.items = items 

#Generate lvl 1
room0 = Room(index=0,light=True,
    name="Basement Teleportation Room", 
    description="\tThe lightish red glow giving the dank, musky air an eerie atmosphere. Your boots barely make noise on the stone floor with a thick layer of dirt and grim to cushion your steps.",
    search_results="Any furniture that adorned this room has long turned to dust. The only reason the teleportation circle even worked seems to be due to it being carved directly into the stone. In the gloom, you can see a door directly in front of you, leading south.",
    connections={"south": 1, "north": 6})
room1 = Room(index=1,light=False,
    name="Old Storage Room",
    description="\tThe storeroom has been destroyed by fire. Charred shelves, burst pots, and broken crates are all that have been west here. The stone tiles have cracked and buckled from the heat. There is a door that leads south",
    search_results="There is nothing salvageable here.",
    d_description="\tYou can faintly smell smoke in the air, but the room seems darker than you anticipated. You can walk in, but the glow of the circle behind you doesn't pierce through the darkness. Will you summon a light or continue blindly forth?",
    d_search_results= "You see nothing, but you fall into piles of something gritty and smooth when you trip on the broken stone tiles.",
    connections={"north": 0, "south": 2})
room2 = Room(index=2,light=False,
    name="Basement Hallway",
    description= "\tScraps of cloth cling to bars along the ceiling, remnants of banners or tapestries that used to decorate the hallway. The air is still, your careful movements disturbing the grave-like atmosphere.",
    search_results="Any furniture that adorned this hallway has crumbled to dust or barely holds together. Something catches your eye among what seemed to be armor stands. You squat south, reaching through the disintegrating wood and feel something smooth and firm. You pull out a full set of leather armor. How it was still useable after so many years is beyond you. It's obviously enchanted. There are one door leading up, that which you've come through, one leading south, one to the west, and one to the east.",
    d_description="\tSmells musty and the air is cold, but you can't see anything.",
    d_search_results="You run your hand against the grimy wall to keep track of where you're going. You trip over piles of...something...a lot while attempting to find a door. You do find three other doors, but you don't know which one to take.",
    connections={"north": 1, "south": 3, "east": 4, "west": 5}, items=[leather_armor])
room3 = Room(index=3,light=False,
    name="Old Religious Studies Classroom",
    description="\tThe room is a mess. Shadows lengthen and shrink as you move through. The stones are uneven and you carefully make your way across them so you don't trip.",
    search_results="Destroyed desks and casks in heaps in the corners and along the walls. Ruined religious relics crumbling in the debris. There is nothing of import that you can see. There is no other door other than the one you entered from.",
    d_description="\tSmells musty and the air is cold, the darkness pressing against you.",
    d_search_results = "You run your hand against the grimy wall to keep track of where you're going. You trip over piles of...something...a lot while attempting to find a door. You can't keep close to the wall. You stumble over rotting wood...things, losing your sense of direction. You do find one door, but you don't know if it's the one you came in through.",
    connections={"north": 2})
room4 = Room(index=4, light=False,
    name="Old Potions Classroom",
    description="\tThere's broken glass and piles of rotten wood that used to be desks scattered around the room. There's a strange scent in the air, mingling with the dust that's been disturbed by your entrance.",
    search_results="There's a few potion bottles that have survived the years, but only one of which has anything inside of it. It's a viscous liquid that's yellow, shifting to red and blue in the light. There's no other door other than the one you entered through.",
    d_description="\tSmells musty and odd, almost like the ghost of decomposing plants and chemicals, but you can't see anything.",
    d_search_results="You can't even reach the wall. Glass cracks beneath your boots. Keeping your footing is interesting and you bump into things at waist level that double you over. You do find a door, but you don't know if it's the one you came in through.",
    connections={"west": 2}, items=[potion],)
room5 = Room(index=5,light=True,
    name="Basement Teleportation Exit",
    description="\tThe circle in this room is the green that you're used to seeing. It shimmers in the floor it's set into. Your light winks out with a thought, knowing you'll be in the Academy proper soon.",
    search_results="The room is bare of any other adornment. Not even the piles of debris are present that existed, if they ever existed to begin with.",
    connections={"east": 2, "south": 8})
room6 = Room(index=6,name="The Little Story of a Big Merc",
    connections={"south": 0})

#generate lvl 2

room7 = Room(index=7, name="Second Floor Hallway",
    description="\tThere's the cloying scent of boiled cabbage in the air, a magic nullifying weapon created by the Imperium. This tool was why the Academy was overrun. None of the Professors could easily use any spell that wouldn't destroy the building to punch through the anti-magic fog.",
    search_results="There are plaques with the room numbers hanging over the ten doors along the hallway, five on each side.\n\n\t2-6, 2-7, 2-8, 2-9, 2-10, 2-11, 2-12, 2-13, 2-14, 2-15.\n\n\tBeyond that, the hallway is pretty bare of adornment. There are some corpses in Imperial uniforms, though they have nothing of note west on them.",
    connections={"door2": 8, "door3": 9, "door4": 10, "door5": 11, "door6": 12, "door7": 13, "door8": 14, "door9": 15, "door10": 16, "door11": 17}, items=[])
room8 = Room(index=8, name="Teleportation Classroom 2-15",
    description="\tThe room is bright! There are no windows, but the mage lights glow strongly, safe in the glass balls attached to the walls. It's obvious that there was a rush to leave this room, as the chairs and desks are haphazardly moved out of the way.",
    search_results="This circle was inlaid with silver, if you judge it east, making it a permanent fixture to the classroom.\n\tYou do a cursory check of all the cabinets and shelves. You do find a bottle of Celestial Wine and a bottle of Blood Wine in the Professor's desk. You shove all the desks and furniture used as a barricade against the door. The door leading south and out of the room is locked from the inside and outside.\n\tYou know this since the Teleportation students were some of the few who escaped. The Professor stayed to try to help evacuate other students. Door is to the south.",
    connections={"south": 7, "north": 5}, items=[celestial_wine, blood_wine])
room9 = Room(index=9, name="Artifice Classroom 2-14",
    description = "\tThe room has artifice tools, weapons, and miscellaneous gear strewn all over scarred tables with stools haphazardly set about the room in various states of position. There is a Professor and five young students in the far corner of the classroom. They look wary until they see that you're obviously not from the Imperial Army. The smell of cabbage is thick in here. You don't think you'll be able to eat it again.\n\tYou inform the Artifice Professor that the Teleportation Circle in the Teleportation Classroom is active and will take them to the basement floor where they can teleport to the outside. He nods, tells you that he will ensure the students exit the danger zone, then will return and wait for you in the stairwell if you're going to face the Imperial forces that are on the first floor. He also invites you to anything you could use from the classroom.",
    search_results = "There are quite a few nice pieces of equipment, but nothing is a full armor set. There's an enchanted sword, a set of enchanted pugilist gloves, and a pair of enchanted daggers that catch your eye. Other than that, the rest of the finished gear is too weak or have enchantments that wouldn't help you. Though why someone would want a helm that turns all sound heard to kitten mews, you have no idea. There is nothing more in the classroom of note. Door is to the north.",
    connections={"north": 7}, items=[gerren_sword, lottie_gloves, rylie_dagger])
room10 = Room(index=10, name="Herbology Classroom 2-13",
    description = "\tThe Herbology room is the only one so far that doesn't reek of cabbage. The heavy scent of earth, fertilizer, and growing things permeates the air. There are two professors and nine young students among the plants. You nearly get something chucked at you before you call out that you were friend and not foe. You inform the professors of the escape route.\n\tThe Herbology Professor goes to lead the students to safety, promising to return and wait for you in the stairwell if you're going to challenge the Imperials southstairs. The Scrying Professor offers to do the same, as they will be taking up the rear to ensure the children don't wander off.",
    search_results = "There is a riot of greenery existing in every nook and cranny of the room. You find three herbal poultices that would help with healing in a pinch. Everything else is in the raw form, which you don't have the experience of knowledge to make use of. Door is to the south.",
    connections={"south": 7}, items=[poultice])
room11 = Room(index=11, name="Scrying Classroom 2-12",
    description = "\tThis room is a similar state of disarray that you've encountered thus far. Thick velvet curtains are draped around the room, softening and masking the stone walls with the thick purple fabric. It was even a few degrees warmer in here, making the chill in the air disappear.",
    search_results = "There are no students or professors hiding in this room. There are some scrying implements and tools, but you have no need for them. You do find a few notes that were obviously being passed between students, but nothing else interesting. Door is to the north.",
    connections={"north": 7}, items=[])
room12 = Room(index=12, name="Bardic Classroom 2-11", 
    description="\tThere are many instruments in the room. It's impressive that so many could fit! The walls are also lined with soft velvet, in addition to the ceiling and floor. The Bardic Professor and three young students are in the cabbage scented room. You tell them it's safe to get the children out of the academy. The Bardic Professor offers to help you when they're done escorting the students and will meet you in the stairwell, if you'll have them.",
    search_results="There is nothing of note that you can use to your advantage in this room. Door is to the south.",                
    connections={"south": 7}, items=[])
room13 = Room(index=13, name="Trap Making Classroom 2-10",
    description = "\tThe Trap Making Classroom makes you nervous enough that you knock before entering. Good thing you did! There are two professors holding sharp and heavy implements that would not feel good! The Alchemy Professor, Trapmaster Professor, and Spell Scribe Professor listen raptly as you bring them up to speed. They have fifteen students to corral, telling you that they'll join you in the stairwell if you are going to take on the fight southstairs.",
    search_results = "A quick search gives you a tar bomb and a rust bomb. There's nothing else you can make do with on the fly. Door is to the north.",
    connections={"north": 7}, items=[tar_bomb, erosion_bomb])
room14 = Room(index=14, name="Alchemy Classroom 2-9",
    description = "\tThe classroom is a little warmer than you were expecting. There are strange instruments that localize the flame in a small area under small glass cauldrons. Various liquids of interesting shades and hues are on the shelves. The classroom looked empty, but you could feel the presence of others regardless. You call out that you're here to get them out. That their professor was already making their way to the teleportation circle in the basement. Six heads pop out of various places, blinking owlishly before lining up in front of you like ducklings.",
    search_results = "There are no finished potions according to the students. There is only one Armor and Attack Potion made by the professor. The rest are dubious at best. The students wouldn't swear to the quality of any of the others. You decide that maybe you should skip out on trying random potions... Door is to the south.",
    connections={"south": 7}, items=[armor_potion, attack_potion])
room15 = Room(index=15, name="Beast Studies Classroom 2-8",
    description = "\tYou knock on the Beast Classroom, unsure what to expect when you break the lock to open the door. Two professors stand with eight more students. There are some angry guard beasts that relax when the Beast Lord Professor gives the command. You fill them in on the goings on. The Beast Lord Professor and the Teleportation Professor look at each other and nodding. They round all the students up, promising to meet you in the stairwell if you were going to take on the battle below.",
    search_results = "There isn't anything fit for consumption in this room for you. There are plenty of stat buffing items, but they're made for animals and monsters, not fit for consumption by anyone else. Doors is to the north.",
    connections={"north": 7}, items=[])
room16 = Room(index=16, name="Spell Writing Classroom 2-7",
    description = "\tYou easily get through the final door on this side of the hallway. The room is cozy, smelling of ink and parchment. Glass pens are carefully stored next to inkwells. Rolls of scrolls are stuffed in the cubby shelves. Books are haphazardly stacked on every other surface that isn't a student's desk.",
    search_results = "Spell scrolls are usable to anyone with the ability to use magical devices, which you can. You don't have all day to look very hard, so you rifle through the tags of completed spell scrolls. You find a lot of spell scrolls that are passable, but not really something you can use. Sin You do strike gold when you find a wind spell that could be very useful in clearing the air... Door is to the south.",
    connections={"south": 7}, items=[whirlwind_scroll])
room17 = Room(index=17, name="Stairwell 2-6",
    search_results="There's nothing really of note, except a picture of a landscape. Very classy. Stairs lead south and the door is to the north.",
    connections={"north": 7, "south": 18}, items=[])
room22 = Room(name="Did Your Job and Went Home With No Drama")
room25 = Room(name="How Long Have You Worked as a Merc, Anyway.")

#Generate lvl 3

room18 = Room(name="First Floor Stairwell",
    description="\tIt's rather noisy, masking your footsteps as you go south the stairs. The ground level stairwell is clean and maintained.",
    search_results="There is nothing of note except the large double doors that lead to the Main Lobby. Door is to the west and the stairs lead north.",
    connections={"north": 17, "west": 19}, items=[])
room19 = Room(name="Main Lobby",
    description="\tThe Academy lobby has quite a few invaders inside of it. It looks like the Centurian in charge is also in there. They thought they could take the school hostage since the young students would keep the retaliation at a minimum.\n\tYou wonder if this is some sort of stalling or misdirection tactic, but then remind yourself to take care of the problem at hand.\n\tIt's a rough battle, even with the things you picked up here and there. At the end of the battle, the automatons are destroyed and the lackeys put down. You keep the leader hostage, as surely someone will want to interrogate him",
    search_results="That cabbage scent is thick in this room! The invaders have stripped anything of note and tossed it in the corner. Maybe the grunts got bored while negotiations were underway? Door to the east leads to the stairwell and a new door is to the south. The exit, perhaps?",
    connections={"south": 20, "east": 18})
room20 = Room(name="Academy Foyer",
    description="\tThe entry to the Academy and where any parents and students would get a glowing first impression on a normal day.",
    search_results="It's a mess! But certainly because of the soldiers, as opposed to the fault of the whoever keeps the Academy clean. The paintings of the Professors and Dean are hanging up along the walls that lead to the exit. Door to the north. You should probably use the Return spell now.",
    connections={"north": 19}, items=[])
room21 = Room(name="Single-handedly Beat All Their Men")
room23 = Room(name="Dog. Just Dog.")
room24 = Room(name="A Big Man with an Old Soul")