from hitbox import Hitbox
from vector2d import Vector2D

#sichtfeld class
class View:
	pos = None;
	size = None;
	hitbox = None;
	
	#constructor erstellt standart sicht mit hitbox
	def __init__(self):
		self.pos = Vector2D(0,0);
		self.size = Vector2D(154,50);
		self.hitbox = Hitbox(Vector2D(self.pos.x+1,self.pos.y+1),Vector2D(self.size.x -2, self.size.y -1));
	
	#updated die position des Sichtfeldes
	def update(self, speed):
		self.pos.x += speed;
		self.hitbox.update_pos(Vector2D(self.pos.x-5,self.pos.y+3));
	
	#löscht alle daten vom sichtfeld
	def delete(self):
		self.pos = None;
		self.size = None;
		self.hitbox = None;