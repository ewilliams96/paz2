from parameters import RIGHT, UP, LEFT, DOWN

class Level:
	def __init(self):
		self.animallist = []
		self.player = Player()
	
	def move(direction):
		if (direction == RIGHT):
			self.player.x = self.player.x +1
		else if (direction == UP):
			self.player.y = self.player.x +y
		else if (direction == LEFT):
			self.player.x = self.player.x -1
		else if (direction == DOWN):
			self.player.y = self.player.y -1

	def draw(self):
		for animal in self.animalist:
			pyglet.resource.image(animal['name']+'..
