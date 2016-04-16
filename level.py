import pyglet
from math import floor

from parameters import RIGHT, UP, LEFT, DOWN, TILES_TALL, TILES_WIDE
from player import Player
from animal import Animal
from display import drawImage

class Level:
	def __init__(self):
		self.animalist = [Animal(10,10), Animal(1,0)]
		self.player = Player()
	
	def move(self,direction):
		if (direction == RIGHT):
			self.player.xPos += 1
		elif (direction == UP):
			self.player.yPos += 1
		elif (direction == LEFT):
			self.player.xPos -= 1
		elif (direction == DOWN):
			self.player.yPos -= 1

	def draw(self):
		for i in range(20):
			for j in range(15):
				drawImage('grass',i,j)
		for animal in self.animalist:
			drawImage(animal.name, animal.xPos - self.player.xPos, animal.yPos-self.player.yPos)
		drawImage("player",floor(TILES_WIDE/2),floor(TILES_TALL/2))
