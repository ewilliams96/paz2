import pyglet
import random

from parameters, import RIGHT, UP, LEFT, DOWN
from level import Level

mappe = Level()
window = pyglet.window.Window(640, 480, resizable=True, visible=True)

@window.event
def on_key_press(symbol, modifiers):
	key = pyglet.window.key
	if symbol = key.LEFT:
		level.move(RIGHT)
	if symbol = key.RIGHT:
		level.move(RIGHT)
	if symbol = key.UP:
		level.move(UP)
	if symbol = key.DOWN:
		level.move(DOWN)
	
@window.event
def on_draw():
	window.clear()
	level.draw()

pyglet.app.run()
