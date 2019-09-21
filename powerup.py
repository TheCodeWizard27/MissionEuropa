import colorama
from vector2d import Vector2D
from hitbox import Hitbox
from texture import Texture
from loadtexture import load_texture

#powerup klasse
class PowerUp:
	isAlive = True;
	pos = Vector2D(0,0);
	hitbox = None;
	texture = None;
	type = 0;
	
	#constructor setzt position sowie textur nach type des powerups
	def __init__(self,pos,type):
		self.pos = pos;
		self.type = type;
		if(type == 1):
			self.texture = Texture(load_texture("entity",3),fore_color = colorama.Fore.GREEN,style = colorama.Style.BRIGHT);
		elif(type == 2):
			self.texture = Texture(load_texture("entity",4),fore_color = colorama.Fore.BLUE,style = colorama.Style.BRIGHT);
		elif(type == 3):
			self.texture = Texture(load_texture("entity",5),fore_color = colorama.Fore.RED,style = colorama.Style.BRIGHT);
		self.hitbox = Hitbox(self.pos,Vector2D(3,3));
	
	#löscht alle inneren objekte für das neuerstellen
	def delete(self):
		self.pos = None;
		self.hitbox = None;
		self.texture = None;