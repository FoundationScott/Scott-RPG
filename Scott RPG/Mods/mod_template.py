# Player Modding Template:


# WARNING: DO NOT CHANGE ATTRIBUTES OF ANYTHING LISTED ABOVE WARNING TWO
import random
class Monster:
    def __init__(self, monster_id, name, level, strength, health, max_health, magic_type, skill_1, skill_2, skill_3, skill_1_damage, skill_2_damage, skill_3_damage, tameable, is_poisoned, is_burning, is_wet, vs_active, vs_count):
        self.id = monster_id
        self.name = name
        self.level = level
        self.strength = strength
        self.health = health
        self.max_health = max_health
        self.magic_type = magic_type
        self.skill_1 = skill_1
        self.skill_2 = skill_2
        self.skill_3 = skill_3
        self.skill_1_damage = skill_1_damage
        self.skill_2_damage = skill_2_damage
        self.skill_3_damage = skill_3_damage
        self.tameable = tameable
        self.is_poisoned = is_poisoned
        self.is_burning = is_burning
        self.is_wet = is_wet
        self.vs_active = vs_active
        self.vs_count = vs_count

    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0

class Sword:
    def __init__(self, nickname, name, attack_damage, durability, price, level_required):
        self.nickname = nickname
        self.name = name
        self.attack_damage = attack_damage
        self.durability = durability
        self.price = price
        self.level_required = level_required

    def set_level_required(self, level_required):
        self.level_required = level_required

class Shield:
    def __init__(self, nickname, name, protection, durability, price, level_required):
        self.nickname = nickname
        self.name = name
        self.protection = protection
        self.durability = durability
        self.price = price
        self.level_required = level_required

    def __str__(self):
        return self.name

class Knuckles:
    def __init__(self, nickname, name, attack_damage, durability, price, level_required):
        self.nickname = nickname
        self.name = name
        self.attack_damage = attack_damage
        self.durability = durability
        self.price = price
        self.level_required = level_required

    def __str__(self):
        return self.name

class Bow:
    def __init__(self, nickname, name, attack_damage, durability, current_arrow_type, arrow_amount, price, level_required):
        self.nickname = nickname
        self.name = name
        self.attack_damage = attack_damage
        self.durability = durability
        self.current_arrow_type = current_arrow_type
        self.arrow_amount = arrow_amount
        self.price = price
        self.level_required = level_required

    def hit_chance(self):
        c = random.randint(1, 20)
        if c >= 10:
            return True
        else:
            return False

    def __str__(self):
        return self.name

class Armor:
    def __init__(self, nickname, name, strength_boost, defense_boost, magic_boost, endurance_boost, level_required, price, armor_type):
        self.nickname = nickname
        self.name = name
        self.strength_boost = strength_boost
        self.defense_boost = defense_boost
        self.magic_boost = magic_boost
        self.endurance_boost = endurance_boost
        self.level_required = level_required
        self.price = price
        self.armor_type = armor_type

    def __str__(self):
        return self.name
# WARNING: DO NOT CHANGE ATTRIBUTES OF ANYTHING LISTED ABOVE HERE(MODIFYING IT WILL BREAK YOUR MOD DUE TO INCOMPATABILITY)


# WARNING: All functions below are examples of how to mod, please note the if you want to mod you must keep function names the same
def add_monster():
    # ID, name, level, strength, health, max health, type, skill 1, skill 2, skill 3, skill 1 damage, skill 2 damage, skill 3 damage, tameable, is poisoned, is burning, is wet, seduction active, and seduction stage
    monsters = {
        "Test Monster": Monster("TM1", "Test Monster", 1, 2, 10, 10, "Earth", "Attack 1", "Attack 2", "Attack 3", 1, 5, 10, False, False, False, False, False, 0),
    }
    return monsters

def add_sword():
    # Nickname, name, attack damage, durability, price, and level required
    swords = {
        "Test Sword": Sword("", "Test Sword", 10, 10, 10, 1),
    }
    return swords

def add_shield():
    # Nickname, name, protection, durability, price, and level required
    shields = {
        "Test Shield": Shield("", "Test Shield", 10, 10, 10, 1),
    }
    return shields

def add_knuckle():
    # Nickname, name, attack damage, durability, price, and level required
    knuckles = {
        "Test Knuckles": Knuckles("", "Test Knuckles", 15, 15, 15, 1),
    }
    return knuckles

def add_bow():
    # Nickname, name, attack damage, durability, current arrow type, arrow amount, price, and level required
    bows = {
        "Test Bow": Bow("", "Test Bow", 10, 10, None, 0, 10, 1),
    }
    return bows

def add_armor():
    # Nickname, name, strength boost, defense boost, magic boost, endurance boost, and level required, price, and armor type
    armors = {
        "Test Helmet": Armor("", "Test Helmet", 3, 5, 0, 0, 1, 3000, "Helmet"),
        "Test Chestplate": Armor("", "Test Chestplate", 3, 5, 0, 0, 1, 3000, "Chestplate"),
        "Test Leggings": Armor("", "Test Leggings", 3, 5, 0, 0, 1, 3000, "Leggings"),
        "Test Boots": Armor("", "Test Boots", 3, 5, 0, 0, 1, 3000, "Boots"),
    }
    return armors


def add_food():
    # Name, and hunger amount
    foods = {
        "Test Food": 1,
    }
    return foods

def add_drink():
    # Name, and thirst amount
    drinks = {
        "Test Drink": 1,
    }
    return drinks

def add_recipe():
    # Name, and ingredients
    recipes = {
        "Test Food Recipe": ["Ingredient 1", "Ingredient 2"],
    }
    return recipes