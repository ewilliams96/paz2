import pyglet
import random

from parameters import RIGHT, UP, LEFT, DOWN,  LEVEL, BATTLE, SCREEN_WIDTH, SCREEN_HEIGHT
from level import Level

mappe = Level()
window = pyglet.window.Window(SCREEN_WIDTH, SCREEN_HEIGHT, resizable=False, visible=True)
mode = LEVEL

@window.event
def on_key_press(symbol, modifiers):
	key = pyglet.window.key
	mappe.handlekey(symbol)
	
@window.event
def on_draw():
	window.clear()
	mappe.draw()
		

pyglet.app.run()
