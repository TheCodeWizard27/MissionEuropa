import colorama
from vector2d import Vector2D
from hitbox import Hitbox
from texture import Texture
from loadtexture import load_texture

#Klasse für Hindernisse
class Obstacle:
	isAlive = True;
	pos = Vector2D(0,0);
	hitbox = None;
	texture = None;
	
	dmg = 2;
	
	#constructor setzt position, textur sowie hitbox je nach hinderniss type
	def __init__(self,pos,type):
		self.pos = pos;
		if(type in [1,2]):
			self.texture = Texture(load_texture("obstacles",0 if type == 1 else 1),bg_color = colorama.Back.BLUE,fore_color = colorama.Fore.CYAN);
			self.hitbox = Hitbox(self.pos,Vector2D(3,11));
		if(type in [3,4]):
			self.texture = Texture(load_texture("obstacles",2 if type == 3 else 3),bg_color = colorama.Back.BLUE,fore_color = colorama.Fore.CYAN);
			self.hitbox = Hitbox(self.pos,Vector2D(2,2));
		if(type in [5,6]):
			self.texture = Texture(load_texture("obstacles",4 if type == 5 else 5),bg_color = colorama.Back.BLUE,fore_color = colorama.Fore.CYAN);
			self.hitbox = Hitbox(self.pos,Vector2D(6,2));
		if(type in [7,8]):
			self.texture = Texture(load_texture("obstacles",6 if type == 7 else 7),bg_color = colorama.Back.BLUE,fore_color = colorama.Fore.CYAN,transparent = False);
			self.hitbox = Hitbox(self.pos,Vector2D(7,24));
	
	#löscht alle inneren objekte für das neuerstellen
	def delete(self):
		self.pos = None;
		self.hitbox = None;
		self.texture = None;