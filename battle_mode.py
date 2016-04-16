import pyglet
from pyglet.window import key


window = pyglet.window.Window()
image = pyglet.resource.image('images/seal.png')
image.width = 200
image.height = 200
imageX = 640 // 2 - image.width // 2 
imageY = 70 - image.height // 2



@window.event
def on_draw():

	window.clear()
	image.blit(imageX, imageY)
	print("test")


# advance text
# choose 
@window.event
def on_key_press(symbol, modifiers):
	global imageX
	global imageY
	imageX = imageX + 32
	imageY = imageY + 32
	on_draw()



pyglet.app.run()


