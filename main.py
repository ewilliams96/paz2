import pyglet
import random

from parameters import RIGHT, UP, LEFT, DOWN,  LEVEL, BATTLE
from level import Level

mappe = Level()
window = pyglet.window.Window(640, 480, resizable=False, visible=True)
mode = LEVEL

@window.event
def on_key_press(symbol, modifiers):
	key = pyglet.window.key
	if(mode == LEVEL):
		if symbol == key.LEFT:
			mode = mappe.move(LEFT)
		elif symbol == key.RIGHT:
			mode = mappe.move(RIGHT)
		elif symbol == key.UP:
			mode = mappe.move(UP)
		elif symbol == key.DOWN:
			mode = mappe.move(DOWN)
	elif(mode == BATTLE):
		if symbol == key.A:
			level.kill( battleMode.attack() )
		elif symbol == key.R:
			level.kill( battleMode.run() )
		else:
			mode = battleMode.otherKey()
	
@window.event
def on_draw():
	window.clear()
	if(mode=='level'):
		mappe.draw()
	elif(mode=='battle'):
		battlemode.draw()
		

pyglet.app.run()
