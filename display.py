import pyglet
from math import floor, ceil

from parameters import TILE_SCALE, TILES_WIDE, TILES_TALL

images = {name: pyglet.resource.image('images/'+name+'.png') for name in ['seal','grass','bird','player','pig','skull','rock']}
sprite = pyglet.sprite.Sprite

def drawTile(name,x,y):
	image = images[name]
	image.width = TILE_SCALE
	image.height = TILE_SCALE
	image.anchor_x = 0
	image.anchor_y = 0
	image = sprite(image,
		x=TILE_SCALE*(x+floor(TILES_WIDE/2)),
		y=TILE_SCALE*(y+floor(TILES_TALL/2)))
	image.draw()


def drawImage(name,x,y,width,height):
	image = images[name]
	image.width = width
	image.height = height
	image.anchor_x = width/2
	image.anchor_y = height/2
	image = sprite(image,
		x=x,
		y=y)
	image.draw()

def drawText(string,x,y,width, font_size=None, color=(255,255,255,255)):
	if font_size == None:
		font_size = 18
	else:
		font_size = font_size
	text = pyglet.text.Label(string, font_name='Courier', font_size=font_size, x=x, y=y, anchor_x='center', width=width, multiline=True, color=color)
	text.draw()
