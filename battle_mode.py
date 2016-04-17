import pyglet
from pyglet.window import key

# for testing
a = animal.Animal(0, 0, 'seal', 10, 10)
# sprite pos
x_pos = 320
y_pos = 240



class BattleMode:
	attackMessage = "attack"
	runMessage = "run"
	def center_image(image):
		image.anchor_x = image.width/2
		image.anchor_y = image.height/2

	def __init__(self):
		self.image = None
		self.player = None
		self.battleMessage = None
		self.level = None
		self.animal = None

	def startBattle(animal, player=None, level=None):
		self.animal = animal
		self.image.width = 200
		self.image.height = 200
		center_image(image)

		self.battleMessage = "You meet a " + a.name + " that has a mass of " + str(a.muscle + a.fat) +  "kg."
		

	def draw():
		display.drawImage(self.enemy)
		display_label(battleMessage)

	def attack():
		if(self.player.muscle > self.animal.muscle):
			self.battleMessage = "The "+self.animal.name+" kills and eats you.\n You died!"
			return 0
		else:
			self.player.fat += self.animal.fat/2;
			self.battleMessage = "You kill and eat the "+self.animal.name+"."
			return 1
	
	def otherKey():
		if(self.animal==None):
			return LEVEL
		else:
			return BATTLE

	def run():
		self.player.fat -= 1
			self.battleMessage = "You run from the "+self.animal.name+"."

'''
def display_label(string, x=None, y=None):
	label = pyglet.text.Label(string,
                          font_name='Courier',
                          font_size=18, 
                          x=320, y=100,
                          anchor_x='center', anchor_y='center', width=600, multiline=True)
	label.draw()

# draw battle screen
#@window.event
#def on_draw():
	# draw animal
#	window.clear()
	#image.blit(x_pos, y_pos)
#	print("test")
	# draw rectangle for text box
	#pyglet.graphics.draw()
#	display_label(battleMessage, 320, 100)


	




# advance text
# choose 



pyglet.app.run()

'''
