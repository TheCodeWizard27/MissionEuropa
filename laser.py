import colorama
from vector2d import Vector2D
from texture import Texture
from hitbox import Hitbox

#laser class
class Laser:
	dmg = 0;
	speed = 10;
	direction = 0;
	pos = Vector2D(0,0);
	hitbox = None;
	texture = Texture("─"*10,fore_color = colorama.Fore.RED,style = colorama.Style.BRIGHT);
	
	#constructor übergibt shaden position sowie richtung des lasers
	def __init__(self,pos,dmg,dir):
		self.dmg = dmg;
		self.direction = dir
		
		self.pos = pos;
		
		if(self.direction == 0):
			self.hitbox = Hitbox(self.pos, Vector2D(10,2));
		else:
			self.hitbox = Hitbox(self.pos, Vector2D(10,0));
		
		if(self.dmg >= 5):
			self.texture.texture = "="*10;
		else:
			self.texture.texture = "─"*10;
	
	#updated shuss position
	def update(self):
		if(self.direction == 0):
			self.pos.x += self.speed;
			self.hitbox.update_pos(Vector2D(self.pos.x-10,self.pos.y-1));
		else:
			self.hitbox.update_pos(Vector2D(self.pos.x,self.pos.y));
			self.pos.x -= self.speed;