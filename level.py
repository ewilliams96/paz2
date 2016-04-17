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
		self.obstacles = [] # obstacles such as trees, rocks, etc 
	
	def move(self,direction):
		if (direction == RIGHT):
			collision = checkCollision(self.player.xPos + 1, self.player.yPos)
			if(collision == Animal):
				# enter battle 
			elif(colission == Obstacle):
				# do nothing (can't move in this direction)
			else:
				self.player.xPos += 1
		elif (direction == UP):

			collision = checkCollision(self.player.xPos, self.player.yPos + 1)

			if(collision == Animal):
				#enter battle
			elif(collision == Obstacle):
				# do nothing can't move
			else:
				self.player.yPos += 1
		elif (direction == LEFT):
			collision = checkCollision(self.player.xPos - 1, self.player.yPos)
			
			if(collision == Animal):
				#enter battle
			elif(collision == Obstacle):
				# do nothing can't move
			else:
				self.player.xPos -= 1

		elif (direction == DOWN):
			collision = checkCollision(self.player.xPos, self.player.yPos - 1)
			
			if(collision == Animal):
				#enter battle
			elif(collision == Obstacle):
				# do nothing can't move
			else:
				self.player.yPos -= 1

	def draw(self):
		for i in range(20):
			for j in range(15):
				drawImage('grass',i,j)
		for animal in self.animalist:
			exists = checkAnimals(animal, self)
			if(exists == True):
				drawImage(animal.name, animal.xPos - self.player.xPos, animal.yPos-self.player.yPos)
			else:
				# don't draw animal if no longer exists 
		drawImage("player",floor(TILES_WIDE/2),floor(TILES_TALL/2))

	# check if animal still on screen, False if animal is no longer on screen
	def checkAnimals(animal, self):
		if(animal.xPos - self.player.xPos < 0 or animal.xPos - self.player.xPos > 20):
			animalist.remove(animal)
			return False
		elif(animal.yPos - self.player.yPos < 0 or animal.yPos - self.player.yPos > 15):
			animalist.remove(animal)
			return False
		else:
			return True

	#  move animal 
	def moveAnimal(animal):
		#direction = random.randint(0, 3)
		if(direction == RIGHT):
			collision = checkCollision(animal.xPos + 1, animal.yPos)
			if(collision == Player:
				#enter battle
			elif(collision == Obstacle):
				# do nothing can't move
			else:
				animal.xPos += 1
		elif(direction == LEFT):
			collision = level.checkCollision(animal.xPos - 1, animal.yPos)
			if(collision == Player:
				#enter battle
			elif(collision == Obstacle):
				# do nothing can't move
			else:
				animal.xPos -= 1
		elif(direction == UP):
			collision = level.checkCollision(animal.xPos, animal.yPos + 1)
			if(collision == Player:
				#enter battle
			elif(collision == Obstacle):
				# do nothing can't move
			else:
				animal.yPos += 1
		elif(direction == DOWN):

			collision = level.checkCollision(animal.xPos, animal.yPos - 1)
			if(collision == Player:
				#enter battle
			elif(collision == Obstacle):
				# do nothing can't move
			else:
				animal.yPos -= 1 


	# param - x, y to check 
	# return object type if obj at x,y
	# return None if no obj at x, y 
	def checkCollision(x, y):
		if(self.player.xPos == x and self.player.yPos == y):
			return type(self.player)

		for animal in self.animalist:
			if(animal.xPos == x and animal.yPos == y):
				return type(animal)

		for obstacle in self.obstacles:
			if(obstacle.xPos == x and obstacle.yPos == y):
				return type(obstacle)

		return None


		

