#Import Libraries
import pygame
import random
import os
from time import sleep

# Import Game Files
###

### ITEM CLASS ###
class Item:
	def __init__(self, name, strength, intelligence, constitution, physical_damage, magic_damage, physical_damage_note, magic_damage_note):
		self.name					= name
		self.strength 				= strength
		self.intelligence			= intelligence
		self.constitution 			= constitution
		self.physical_damage 		= physical_damage
		self.magic_damage 			= magic_damage
		self.physical_damage_note 	= physical_damage_note
		self.magic_damage_note 		= magic_damage_note







none 					= Item("", 0, 0, 0, 0, 0, [0, 0], [0, 0])

mace 					= Item("Mace", 1, 1, 1, random.randint(1, 6), 0, [1, 6], [0, 0])
sword 					= Item("Sword", 2, 0, 1, random.randint(1, 6), 0, [1, 6], [0, 0])
rune_sword 				= Item("Rune Sword", 4, 0, 2, random.randint(2, 12), 0, [2, 12], [0, 0])
axe						= Item("Axe", 4, 0, 2, random.randint(1, 6), 0, [1, 6], [0, 0])
vorpal_sword 			= Item("Vorpal Sword", 1, 1, 1, random.randint(1, 11), 0, [1, 11], [0, 0])
staff					= Item("Magic Staff", 0, 3, 0, random.randint(0, 4), random.randint(6, 12), [0, 4], [6, 12])

chain_mail 				= Item("Chain Mail", 2, 0, 1, None, None, [0, 0], [0, 0])
plate_mail 				= Item("Plate Mail", 1, 0, 2, None, None, [0, 0], [0, 0])

health_ring				= Item("Health Ring", 0, 0, 4, None, None, [0, 0], [0, 0])
ring_of_intelligence 	= Item("Ring of Intelligence", 0, 4, 0, None, random.randint(1, 2), [0, 0], [1, 2])
spikey_ring				= Item("Spikey Ring", 4, 0, -2, random.randint(1, 4), None, [1, 4], [0, 0])










