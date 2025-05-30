#Item Class

class Item:
    def __init__(self, name="", description="", equip_slots="", equipable=True, health_bonus=0, mana_bonus=0, defense_bonus=0, attack_bonus=0, required_job=None):
        self.name = name
        self.description = description
        self.equip_slots = equip_slots
        self.equipable = equipable
        self.health_bonus = health_bonus
        self.mana_bonus = mana_bonus
        self.defense_bonus = defense_bonus
        self.attack_bonus = attack_bonus
        self.required_job = required_job
       
leather_armor=Item(
    name="Leather Armor Set of the Forgotten",
    description="Leather Armor Set that has somehow survived in the basement under the Academy for an untold number of years.",
    equip_slots=["head", "body", "feet"],
    equipable=True,
    health_bonus=5,
    defense_bonus=2,)
gerren_sword=Item(
    name="Gerren's Enchanted Long Sword",
    description="Gerren worked really hard to enchant this sword! It's a plain looking sword, but its edges are sharp!",
    equip_slots=["weapon"],
    equipable=True,
    health_bonus=2,
    defense_bonus=1,
    attack_bonus=5,
    required_job="Swordlord")
lottie_gloves=Item(
    name="Lottie's Enchanted Pugilist Gloves",
    description="Lottie worked really hard on these! They're heavier than they look...what did Lottie put in these?!",
    equip_slots=["weapon"],
    equipable=True,
    health_bonus=2,
    defense_bonus=1,
    attack_bonus=5,
    required_job="Pugilist")
rylie_dagger=Item(
    name="Rylie's Enchanted Dagger Pair",
    description = "Rylie worked really hard on these! They both have colored hilts wrought of wood with vines around the hilt. The color choice is a bit off...one is red and the other is green...",
    equip_slots=["weapon"],
    equipable=True,
    health_bonus=2,
    defense_bonus=1,
    attack_bonus=5,
    required_job="Rogue")
poultice=Item(
    name="Health Poultice",
    description="This poutice will heal for 10 HP. Pretty good for a student!",
    equipable=False,
    health_bonus=10)
armor_potion=Item(
    name="Armor Potion",
    description="Ups Defense by 3 for 10 minutes!",
    equipable=False,
    defense_bonus=3)
attack_potion=Item(
    name="Attack Potion",
    description="Ups Attack Power by 3 for 10 minutes!",
    equipable=False,
    attack_bonus=3)
tar_bomb=Item(
    name="Tar Bomb",
    description="Eats through attack and defense!",
    equipable=False,
    defense_bonus=-1,
    attack_bonus=-2,)
erosion_bomb=Item(
    name="Erosion Bomb",
    description="Eats health! Even metal foes are not safe!",
    equipable=False,
    health_bonus=-8,)
whirlwind_scroll=Item(
    name="Whirlwind Scroll",
    description="Need to clear the air? This is the best way to do it! You can use spellscrolls even where there is anti-magic fog in the air.",
    equipable=False,
    mana_bonus=-15,)
celestial_wine=Item(
    name="Celestial Wine",
    description="A little taste of where Angels dwell. Too bad you'll be too trashed to enjoy past the first sip.",
    equipable=False,
    health_bonus=-5,
    mana_bonus=15,
    defense_bonus=2,)
blood_wine=Item(
    name="Blood Wine",
    description="Feeling a little iron deficient? This is not the way to fix that.",
    equipable=False,
    health_bonus=15,
    mana_bonus=-5,
    attack_bonus=2,)
unknown_potion=Item(
    name="Unknown Potion",
    description="Of dubious age, original effect, and viscous. You're not really gonna drink this are you?",
    equipable=False,
    health_bonus=-20,
    mana_bonus=-20,)

#Items

leather_armor = Item(name="Leather Armor Set of the Forgotten", description="Leather Armor Set that has somehow survived in the basement under the Academy for an untold number of years.")
potion = Item(name="Unknown Potion", description="Of dubious age, original effect, and viscous. You're not really gonna drink this are you?")
celestial_wine = Item(name="Celestial Wine", description="A little taste of where Angels dwell. Too bad you'll be too trashed to enjoy past the first sip.")
blood_wine = Item(name="Blood Wine", description="Feeling a little iron deficient? This is not the way to fix that.")
gerren_sword = Item(name="Gerren's Enchanted Long Sword", description="Gerren worked really hard to enchant this sword! It's a plain looking sword, but its edges are sharp!")
lottie_gloves = Item(name="Lottie's Enchanted Pugilist Gloves", description="Lottie worked really hard on these! They're heavier than they look...what did Lottie put in these?!")
rylie_dagger = Item(name="Rylie's Enchanted Dagger Pair", description="Rylie worked really hard on these! They both have colored hilts wrought of wood with vines around the hilt. The color choice is a bit off...one is red and the other is green...")
poultice = Item(name="Health Poultice", description="This poutice will heal for 10 HP. Pretty good for a student!") 
tar_bomb = Item(name="Tar Bomb", description="Eats through attack and defense!")
erosion_bomb = Item(name="Erosion Bomb", description="Eats health! Even metal foes are not safe!")
armor_potion = Item(name="Armor Potion", description="Ups Defense by 3 for 10 minutes!")
attack_potion = Item(name="Attack Potion", description="Ups Attack Power by 3 for 10 minutes!")
whirlwind_scroll = Item(name="Whirlwind Scroll", description="Need to clear the air? This is the best way to do it! You can use spellscrolls even where there is anti-magic fog in the air.")
