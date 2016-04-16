import random
import parameters
class Animal:
	def __init(self, xPos, yPos, name=None, fat=None, muscle=None):
		self.name = name
		self.fat = fat
		self.muscle = muscle
		self.xPos = xPos
		self.yPos = yPos

	# 	
	def move():
		direction = random.randint(1, 4)
		if(direction == 1):

