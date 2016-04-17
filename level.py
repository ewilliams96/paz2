import pyglet
from math import floor

from parameters import RIGHT, UP, LEFT, DOWN, TILES_TALL, TILES_WIDE, LEVEL, BATTLE
from player import Player
from animal import Animal
from display import drawTile, drawImage
import random 

class Level:
	def __init__(self):
		self.animalist = [Animal(10,10), Animal(1,0)]
		self.player = Player()
		self.obstacles = [] # obstacles such as trees, rocks, etc 
		self.mode = LEVEL

		self.battle_animal = None
		self.battle_status = None

	def handlekey(self, symbol):
		key = key = pyglet.window.key
		if(self.mode == LEVEL):
			if symbol == key.LEFT:
				self.move(LEFT)
			elif symbol == key.RIGHT:
				self.move(RIGHT)
			elif symbol == key.UP:
				self.move(UP)
			elif symbol == key.DOWN:
				self.move(DOWN)
			for animal in self.animalist:
				self.moveAnimal(animal)
		elif(self.mode == BATTLE):
			if symbol == key.A:
				level.kill( attack() )
			elif symbol == key.R:
				level.kill( run() )
			else:
				self.mode = battleMode.otherKey()
	
	def draw(self):
		if(self.mode == LEVEL):
			self.levelDraw()
		else:
			self.battleDraw()

	def move(self,direction):

		attemptMoveX = self.player.xPos + direction[0]
		attemptMoveY = self.player.yPos + direction[1]

		result = self.checkCollision(attemptMoveX, attemptMoveY)
		if isinstance(result, Animal):
			self.startBattle(result)
		elif result == None:
			self.player.xPos = attemptMoveX
			self.player.yPos = attemptMoveY



	def levelDraw(self):
		for i in range(20):
			for j in range(15):
				drawTile('grass',i,j)
		for animal in self.animalist:
			exists = self.checkAnimals(animal)
			if(exists == True):
				drawTile(animal.name, animal.xPos - self.player.xPos, animal.yPos-self.player.yPos)
			else:
				pass# don't draw animal if no longer exists 
		drawTile("player",floor(TILES_WIDE/2),floor(TILES_TALL/2))


	#  move animal 
	def moveAnimal(self, animal):
		direction = random.randint(0, 3)
		


	def checkAnimals(self, animal):
		if(animal.xPos - self.player.xPos < 0 or animal.xPos - self.player.xPos > 20):
			self.animalist.remove(animal)
			return False
		elif(animal.yPos - self.player.yPos < 0 or animal.yPos - self.player.yPos > 15):
			self.animalist.remove(animal)
			return False
		else:
			return True
		if(self.player.xPos == x and self.player.yPos == y):
			return type(self.player)
	# param - x, y to check 
	# return object type if obj at x,y
	# return None if no obj at x, y 
	def checkCollision(self, x, y):
		# check if animal still on screen, False if animal is no longer on screen

		for animal in self.animalist:
			if(animal.xPos == x and animal.yPos == y):
				return animal
		'''
		for obstacle in self.obstacles:
			if(obstacle.xPos == x and obstacle.yPos == y):
				return type(obstacle)
		'''

		return None

	def startBattle(self, animal):
		self.battle_animal = animal
		self.battleMessage = "You meet a " + a.name + " that has a mass of " + str(a.muscle + a.fat) +  "kg."
		self.mode = BATTLE


	def battleDraw(self):
		drawImage(self.battle_animal.name, 320,240,200,200)
		#display_label(battleMessage)

	def attack(self):
		if(self.player.muscle > self.animal.muscle):
			self.battleMessage = "The "+self.animal.name+" kills and eats you.\n You died!"
			return 0
		else:
			self.player.fat += self.animal.fat/2;
			self.battleMessage = "You kill and eat the "+self.animal.name+"."
			return 1
	
	def otherKey(self):
		if(self.animal==None):
			return LEVEL
