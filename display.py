import pyglet
from math import floor

from parameters import TILE_SCALE, TILES_WIDE, TILES_TALL

images = {name: pyglet.resource.image('images/'+name+'.png') for name in ['seal','grass','bird','player','pig']}

def drawTile(name,x,y):
	image = images[name]
	image.width = TILE_SCALE
	image.height = TILE_SCALE
	image.anchor_x = 0
	image.anchor_y = 0
	image.blit(TILE_SCALE*(x+floor(TILES_WIDE/2)), TILE_SCALE*(y+floor(TILES_TALL/2)))

def drawImage(name,x,y,width,height):
	image = images[name]
	image.width = width
	image.height = height
	image.anchor_x = width/2
	image.anchor_y = height/2
	image.blit(TILE_SCALE*x,TILE_SCALE*y)

def drawText(string,x,y,width):
	text = pyglet.text.Label(string, font_name='Courier', font_size=18, x=x, y=y, anchor_y='center', width=width, multiline=True)
