from vector2d import Vector2D

#hitbox klasse fuer kollision detection
class Hitbox:
	pos = Vector2D(0,0);
	size = Vector2D(0,0);
	x = 0;
	x2 = 0;
	y = 0;
	y2 = 0;
	
	#Konstruktor für hitbox setzt position und grösse
	def __init__(self,pos,size):
		self.pos = pos;
		self.size = size;
		self.x = self.pos.x;
		self.x2 = self.pos.x + self.size.x;
		self.y = self.pos.y;
		self.y2 = self.pos.y + self.size.y;
	
	#gibt zurück ob hitboxen überlappen
	def check_hitbox(self, hitbox):
		if(self.x <= hitbox.x2 and self.x2 >= hitbox.x and self.y <= hitbox.y2 and self.y2 >= hitbox.y):
			return True;
		else:
			return False;
	
	#updatet position der hitbox
	def update_pos(self,pos):
		self.pos = pos;
		self.x = self.pos.x;
		self.x2 = self.pos.x + self.size.x;
		self.y = self.pos.y;
		self.y2 = self.pos.y + self.size.y;