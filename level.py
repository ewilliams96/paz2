import pyglet
from math import floor, ceil

from parameters import RIGHT, UP, LEFT, DOWN, TILES_TALL, TILES_WIDE, LEVEL, BATTLE, SCREEN_WIDTH, SCREEN_HEIGHT, END, WIN, IN_PROG, ANIMAL_TYPES
from player import Player
from animal import Animal
from display import drawTile, drawImage, drawText
import random 

class Level:
	def __init__(self):
		self.animalist = [Animal(10,10), Animal(1,0)]
		self.player = Player()
		self.obstacles = [] # obstacles such as trees, rocks, etc 
		self.mode = LEVEL

		self.battle_animal = None
		self.battle_status = None
	
	# HANDLE KEY PRESS
	def handlekey(self, symbol):
		key = pyglet.window.key
		print("key press")
		print(self.mode)

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
				self.attack()
			elif symbol == key.R:
				self.run()
			else:
				self.mode = self.otherKey()
	
### LEVEL MODE DRAWING AND FUNCTIONS 

	def draw(self):
		if(self.mode == LEVEL):
			self.levelDraw()
		else:
			self.battleDraw()

	def move(self,direction):
		self.randomAnimals(direction)
		attemptMoveX = self.player.xPos + direction[0]
		attemptMoveY = self.player.yPos + direction[1]

		result = self.checkCollision(attemptMoveX, attemptMoveY)
		if isinstance(result, Animal):
			self.startBattle(result)
		elif result == None:
			self.player.xPos = attemptMoveX
			self.player.yPos = attemptMoveY



	def levelDraw(self):
		for i in range(-floor(TILES_WIDE/2),ceil(TILES_WIDE/2)):
			for j in range(-floor(TILES_TALL/2),ceil(TILES_TALL/2)):
				drawTile('grass',i,j)
		for animal in self.animalist:
			exists = self.checkAnimals(animal)
			if(exists == True):
				drawTile(animal.name, animal.xPos - self.player.xPos, animal.yPos-self.player.yPos)
			else:
				pass# don't draw animal if no longer exists 
		drawTile("player",0,0)

	# generate random animals onto list to draw on map
	def randomAnimals(self,direction):
		animalType = random.choice(ANIMAL_TYPES)
		upper = [0,0]
		lower = [0,0]
		screenSize = [TILES_WIDE,TILES_TALL]

		for i in [0,1]:
			if direction[i] == 0:
				lower[i] = - screenSize[i]
				upper[i] =  screenSize[i]
			elif direction[i] == -1:
				lower[i] =  - screenSize[i]
				upper[i] =  1- screenSize[i]
			elif direction[i] == 1:
				lower[i] =  screenSize[i]-1
				upper[i] =  screenSize[i]

		xLoc = self.player.xPos + random.randint(lower[0], upper[0])
		yLoc = self.player.yPos + random.randint(lower[1], upper[1])

		newAnimal = Animal(xLoc, yLoc, animalType)
		self.animalist.append(newAnimal)


	#  move animal 
	def moveAnimal(self, animal):
		direction = random.randint(0, 3)
		


	def checkAnimals(self, animal):
		if(abs(animal.xPos - self.player.xPos) > TILES_WIDE or
			abs(animal.yPos - self.player.yPos) > TILES_TALL):
			print("???")
			self.animalist.remove(animal)
			return False
		else:
			return True
	# param - x, y to check 
	# return object type if obj at x,y
	# return None if no obj at x, y 

		xLoc = random.randint(lower[0], upper[0])
		yLoc = random.randint(lower[1], upper[1])

		newAnimal = Animal(xLoc, yLoc, animalType)
		self.animalist.append(newAnimal)


	#  move animal 
	def moveAnimal(self, animal):
		direction = random.randint(0, 3)
		


	def checkAnimals(self, animal):
		if(abs(animal.xPos - self.player.xPos) > TILES_WIDE or
			abs(animal.yPos - self.player.yPos) > TILES_TALL):
			print("???")
			self.animalist.remove(animal)
			return False
		else:
			return True
	# param - x, y to check 
	# return object type if obj at x,y
	# return None if no obj at x, y 
	def checkCollision(self, x, y):
		# check if animal still on screen, False if animal is no longer on screen
		if(self.player.xPos == x and self.player.yPos == y):
			return self.player
		for animal in self.animalist:
			if(animal.xPos == x and animal.yPos == y):
				return animal
		'''
		for obstacle in self.obstacles:
			if(obstacle.xPos == x and obstacle.yPos == y):
				return type(obstacle)
		'''

		return None

### BATTLE MODE FUNCTIONS ###
	def startBattle(self, animal):
		self.battle_animal = animal
		self.battleMessage = "You meet a " + animal.name + " that has a mass of " + str(animal.muscle + animal.fat) +  "kg."
		self.mode = BATTLE
		self.battle_status = IN_PROG


	def battleDraw(self):
		drawImage(self.battle_animal.name, 320,240,200,200)
		drawText(self.battleMessage, SCREEN_WIDTH/2, SCREEN_HEIGHT/4, SCREEN_WIDTH)

	# result of attack in battle mode
	def attack(self):
		if(self.player.muscle > self.battle_animal.muscle):
			self.battleMessage = "The "+self.battle_animal.name+" kills and eats you.\n You died!"
			self.battle_status = END

		else:
			self.player.fat += self.battle_animal.fat/2;
			self.battleMessage = "You kill and eat the "+self.battle_animal.name+"."
			
			# remove animal from list after killed so not rendered again
			self.animalist.remove(self.battle_animal)
			# set to none to indicate battle finished on otherKey()
			self.battle_status = WIN


			
	def run(self):
		self.battleMessage = "You run away from the " + self.battle_animal.name+"."
		# indicate battle is over on next key press 
		self.battle_status = WIN



	def otherKey(self):
		if(self.battle_status == WIN):
			return LEVEL
		# if game over screen
		if(self.battle_status == END):
			self.gameOver()
		if(self.battle_status == IN_PROG):
			return BATTLE



	def gameOver(self):
		skull = Animal(0, 0, "skull")
		self.battle_animal = skull
		self.battleMessage = "GAME OVER. "

