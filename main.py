import pyglet
import random

from parameters import RIGHT, UP, LEFT, DOWN
from level import Level

mappe = Level()
window = pyglet.window.Window(640, 480, resizable=False, visible=True)

@window.event
def on_key_press(symbol, modifiers):
	key = pyglet.window.key
	if symbol == key.LEFT:
		mappe.move(LEFT)
	elif symbol == key.RIGHT:
		mappe.move(RIGHT)
	elif symbol == key.UP:
		mappe.move(UP)
	elif symbol == key.DOWN:
		mappe.move(DOWN)
	
@window.event
def on_draw():
	window.clear()
	mappe.draw()

pyglet.app.run()
