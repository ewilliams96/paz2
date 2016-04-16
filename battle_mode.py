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

	def startBattle(animal, player=None, level=None):
		
		
		imageName = 'images/' + animal.name + ".png"
		self.image = pyglet.resource.image(imageName)
		
		self.image.width = 200
		self.image.height = 200
		center_image(image)
		
		
		self.battleMessage = "You meet a " + a.name + " that has a mass of " + str(a.muscle + a.fat) +  "kg."
		

	def battleModeDraw():
		image.blit()
		display_label(battleMessage)

	def attack():
		Display.


	def run():
		Displa. 



	



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


