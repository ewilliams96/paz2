from parameters import RIGHT, UP, LEFT, DOWN, TILE_SIZE

class Level:
	def __init(self):
		self.animallist = []
		self.player = Player()
	
	def move(direction):
		if (direction == RIGHT):
			self.player.x += 1
		else if (direction == UP):
			self.player.y += +y
		else if (direction == LEFT):
			self.player.x -= 1
		else if (direction == DOWN):
			self.player.y -= 1

	def draw(self):
		grass = pyglet.resource.image('images/grass.png')
		grass.width = 32
		grass.height = 32
		for i in range(20):
			for j in range(15):
				grass.blit(x*TILE_SIZE, y*TILE_SIZE)
		for animal in self.animalist:
			animalImage = pyglet.resource.image('images/'+animal.name+'.png')
			animalImage.width = 32
			animalImage.height = 32
			animalImage.blit(animal.x*TILE_SIZE - self.player.x, animal.y*TILE_SIZE - self.player.y)
