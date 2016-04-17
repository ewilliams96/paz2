import pyglet

from parameters import TILE_SCALE

window = pyglet.window.Window(640, 480, resizable=False, visible=True)
images = {name: pyglet.resource.image('images/'+name+'.png') for name in ['seal','grass','bird','player','pig']}

def drawTile(name,x,y):
	image = images[name]
	image.width = TILE_SCALE
	image.height = TILE_SCALE
	image.anchor_x = 0
	image.anchor_y = 0
	image.blit(TILE_SCALE*x,TILE_SCALE*y)

def drawImage(name,x,y,width,height):
	image = images[name]
	image.width = width
	image.height = height
	image.anchor_x = width/2
	image.anchor_y = height/2
	image.blit(TILE_SCALE*x,TILE_SCALE*y)

