#Import Libraries
import pygame
import random
import os
from time import sleep

# Import Game Files
###

### ABILITY CLASS ###
class Ability:
	def __init__(self, name, physical_damage, magic_damage, healing, miss, other):
		self.name 				= name
		self.physical_damage 	= physical_damage
		self.magic_damage 		= magic_damage
		self.healing			= healing 
		self.miss 				= miss



fire1			= Ability("Fire I", 0 , random.randint(1, 6), 0, 0, None)
fire2			= Ability("Fire II", 0 , random.randint(6, 12), 0, 0, None)