# Import Libraries
import pygame
import random
import os
from time import sleep

# Import Game Files
from abilities import *
from items import *


### CHARACTER CLASS ###
class Character:
    def __init__(self, name, level, strength, intelligence, constitution, equipped_weapon):
        self.name = name
        self.level = level
        self.difficulty = 1

        self.strength = strength
        self.strength_reset = 0
        self.physical_damage = 0
        self.min_physical_damage = 0
        self.max_physical_damage = 0

        self.intelligence = intelligence
        self.intelligence_reset = 0
        self.magic_damage = 0
        self.min_magic_damage = 0
        self.max_magic_damage = 0

        self.constitution = constitution
        self.constitution_reset = 0
        self.health = 0
        self.max_health = 0

        self.skill_points = 1
        self.skill_points_reset = 0

        self.damage             = 0
        self.missed             = False

        self.equipped_weapon    = equipped_weapon
        self.equipped_armour    = none
        self.equipped_token     = none

        self.inventory_weapon   = [sword, mace, rune_sword, axe, vorpal_sword, staff]
        self.inventory_armour   = [chain_mail, plate_mail]
        self.inventory_token    = [health_ring, ring_of_intelligence, spikey_ring]

        self.magic_abilities    = [fire1, fire2, fire3, ice1, ice2, ice3]

    def convert_stats(self):
        self.physical_damage    = (self.strength + self.equipped_weapon.strength + self.equipped_armour.strength + self.equipped_token.strength)
        self.magic_damage       = (self.intelligence + self.equipped_weapon.intelligence + self.equipped_armour.intelligence + self.equipped_token.intelligence)
        self.max_health         = (self.constitution + self.equipped_weapon.constitution + self.equipped_armour.constitution + self.equipped_token.constitution) * 10 + 100

        self.min_physical_damage = self.equipped_weapon.physical_damage_note[0] + self.equipped_armour.physical_damage_note[0] + self.equipped_token.physical_damage_note[0]
        self.max_physical_damage = self.equipped_weapon.physical_damage_note[1] + self.equipped_armour.physical_damage_note[1] + self.equipped_token.physical_damage_note[1]

        self.min_magic_damage = self.equipped_weapon.magic_damage_note[0] + self.equipped_armour.magic_damage_note[0] + self.equipped_token.magic_damage_note[0]
        self.max_magic_damage = self.equipped_weapon.magic_damage_note[1] + self.equipped_armour.magic_damage_note[1] + self.equipped_token.magic_damage_note[1]

    def attack_physical(self):
        self.damage_done = random.randint(self.min_physical_damage, self.max_physical_damage) + self.physical_damage
        return self.damage_done

    def attack_magic(self, ability):
        self.damage_done = ability.magic_damage + random.randint(self.min_magic_damage, self.max_magic_damage) + self.magic_damage
        return self.damage_done

    def inventory(self):
        self.inventory = []


player              = Character("Lorther", 1, 10, 1, 1, sword)
npc_dustin_echos    = Character("Dustin Echos", 2, 2, 2, 2, rune_sword)
npc_aurore          =  Character("Aurore", 3, 3, 3, 3, vorpal_sword)  