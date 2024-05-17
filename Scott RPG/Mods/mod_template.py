# Player Modding Template:


# WARNING 1: DO NOT CHANGE ATTRIBUTES OF ANYTHING LISTED ABOVE WARNING TWO
from mod_loader import *
# WARNING 2: DO NOT CHANGE ATTRIBUTES OF ANYTHING LISTED ABOVE HERE(MODIFYING IT WILL BREAK YOUR MOD DUE TO INCOMPATIBILITY)


# READ ME: All functions below are examples of how to mod, please note the if you want to mod you must keep function names the same

# Name, ID, name, level, strength, health, max health, type, skill 1, skill 2, skill 3, skill 1 damage, skill 2 damage, skill 3 damage, tameable, is poisoned, is burning, is wet, seduction active, and seduction stage
add_monster({"Test Monster": Monster("TM1", "Test Monster", 1, 2, 10, 10, "Earth", "Attack 1", "Attack 2", "Attack 3", 1, 5, 10, False, False, False, False, False, 0),}):

# Name, nickname, name, attack damage, durability, price, and level required
add_sword({"Sword Name": Sword("", "Sword Name", 10, 10, 10, 1),)

# Name, nickname, name, protection, durability, price, and level required
add_shield(shield={"Shield Name": Shield("", "Shield Name", 10, 10, 10, 1),})

# Name, nickname, name, attack damage, durability, price, and level required
add_knuckle({"Knuckles Name": Knuckles("", "Knuckles Name", 15, 15, 15, 1),})

add_bow({"Bow Name": Bow("", "Bow Name", 10, 10, None, 0, 10, 1),})

# Name, nickname, name, strength boost, defense boost, magic boost, endurance boost, level required, price, and armor type
add_armor({"Helmet Name": Armor("", "Helmet Name", 3, 5, 0, 0, 1, 3000, "Helmet"),}, {"Chestplate Name": Armor("", "Chestplate Name", 3, 5, 0, 0, 1, 3000, "Chestplate"),}, {"Leggings Name": Armor("", "Leggings Name", 3, 5, 0, 0, 1, 3000, "Leggings"),}, {"Boots Name": Armor("", "Boots Name", 3, 5, 0, 0, 1, 3000, "Boots"),})

# Name, and hunger amount
add_food({"Food Name": 1})

# Name, and thirst amount
add_drink({"Drink Name": 1})

# Name, and ingredients
add_recipe({"Recipe Name": ["Ingredient 1", "Ingredient 2"]})
