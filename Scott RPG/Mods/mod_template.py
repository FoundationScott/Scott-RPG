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

def add_monster():
    # ID, name, level, strength, health, max health, type, skill 1, skill 2, skill 3, skill 1 damage, skill 2 damage, skill 3 damage, tameable, is poisoned, is burning, is wet, seduction active, and seduction stage
    monsters = {
        "Test Monster": Monster("TM1", "Test Monster", 1, 2, 10, 10, "Earth", "Attack 1", "Attack 2", "Attack 3", 1, 5, 10, False, False, False, False, False, 0),
        "Test Monster 2": Monster("TM25", "Test Monster 2", 25, 5, 20, 20, "Water", "Attack 1", "Attack 2", "Attack 3", 5, 10, 15, True, False, False, False, False, 0)
    }
    return monsters

def add_sword():
    # Nickname, name, attack damage, durability, price, and level required
    swords = {
        "Test Sword": Sword("", "Test Sword", 10, 10, 10, 1),
        "Test Sword 2": Sword("", "Test Sword 2", 10, 10, 10, 1)
    }
    return swords
