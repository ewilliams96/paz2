import pyglet

from parameters import TILE_SCALE

images = {name: pyglet.resource.image('images/'+name+'.png') for name in ['seal','grass','bird','player','pig']}

def drawImage(name,x,y):
	image = images[name]
	image.width = TILE_SCALE
	image.height = TILE_SCALE
	image.anchor_x = 0
	image.anchor_y = 0
	image.blit(TILE_SCALE*x,TILE_SCALE*y)
