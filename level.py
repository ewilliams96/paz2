import pyglet
from parameters import RIGHT, UP, LEFT, DOWN
from player import Player
from animal import Animal
TILE_SIZE = 32

class Level:
	def __init__(self):
		self.animalist = [Animal(10,10)]
		self.player = Player()
	
	def move(self,direction):
		if (direction == RIGHT):
			self.player.xPos += 1
		elif (direction == UP):
			self.player.y += 1
		elif (direction == LEFT):
			self.player.xPos -= 1
		elif (direction == DOWN):
			self.player.y -= 1

	def draw(self):
		grass = pyglet.resource.image('images/grass.png')
		grass.width = 32
		grass.height = 32
		for i in range(20):
			for j in range(15):
				grass.blit(i*TILE_SIZE, j*TILE_SIZE)
		for animal in self.animalist:
			animalImage = pyglet.resource.image('images/'+animal.name+'.png')
			animalImage.width = 32
			animalImage.height = 32
			animalImage.blit(animal.xPos*TILE_SIZE - self.player.xPos, animal.y*TILE_SIZE - self.player.y)
