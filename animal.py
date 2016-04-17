import random
from parameters import * 
import level

class Animal:
	def __init__(self, xPos, yPos, name=None, fat=None, muscle=None):
		if name == None:
			name = 'seal'
		if fat == None:
			fat = random.randint(0,30)
		if muscle == None:
			muscle  = random.randint(0,30)
		self.name = name
		self.fat = fat
		self.muscle = muscle
		self.xPos = xPos
		self.yPos = yPos
