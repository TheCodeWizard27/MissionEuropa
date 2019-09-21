import colorama
from menu import Menu
from view import View
from drawengine import Graphics
from obj import Obj
from loadtexture import load_texture
from vector2d import Vector2D

#gameover class
class Gameover(Menu):
	
	#constructor fügt alle Gameover objekte zum zeichnen hinzu
	def __init__(self):
		self.room_objects = [
			Obj(Vector2D(self.view.pos.x+5,1),load_texture("other",1),style = colorama.Style.BRIGHT),
			Obj(Vector2D(self.view.pos.x+5,10),load_texture("other",4)),
			Obj(Vector2D(self.view.pos.x+5,15),load_texture("other",4)),
			Obj(Vector2D(self.view.pos.x+5+3,12),"Retry"),
			Obj(Vector2D(self.view.pos.x+5+3,17),"Exit")
		];