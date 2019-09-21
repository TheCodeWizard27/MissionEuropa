import colorama
from menu import Menu
from view import View
from drawengine import Graphics
from obj import Obj
from loadtexture import load_texture
from vector2d import Vector2D

#Titlescreen class
class Titlescreen(Menu):

	#constructor fügt alle Titlescreen objekte zum zeichnen hinzu
	def __init__(self):
		self.room_objects = [
			Obj(Vector2D(self.view.pos.x+5,1),load_texture("other",0),style = colorama.Style.BRIGHT),
			Obj(Vector2D(self.view.pos.x+5,10),load_texture("other",4)),
			Obj(Vector2D(self.view.pos.x+5,15),load_texture("other",4)),
			Obj(Vector2D(self.view.pos.x+5+3,12),"Start Game"),
			Obj(Vector2D(self.view.pos.x+5+3,17),"Exit"),
			Obj(Vector2D(self.view.pos.x+50, 12), "How to play:\n W,A,S,D                              = Bewegen(ohne schiessen)\n Pfeil Tasten                         = Bewegen(mit schiessen)\n Alle Tasten ausser W,A,S,D,Enter,Esc = Schiessen")
		];