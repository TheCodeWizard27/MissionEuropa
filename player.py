import colorama
from vector2d import Vector2D
from texture import Texture
from loadtexture import load_texture
from hitbox import Hitbox
from laser import Laser

#player class
class Player:
	isAlive = True;
	pos = None;
	hitbox = None;
	texture = Texture(load_texture("entity",0),fore_color = colorama.Fore.GREEN,style = colorama.Style.BRIGHT);
	facing = 0; #0 up 1 right 2 down 3 left
	state = 0;	#0 = normal 1 = shooting 2 = shield active 3 = i_frames
	laser = [];
	
	hp = 5;
	dmg = 2;
	speed = 3;
	
	dmg_timer = 0;
	cooldown_timer = 0;
	invincibility = False;
	invincibility_timer = 0;
	shield = False;
	
	#constructor setzt die position hitbox sowie texture vom spieler
	def __init__(self):
		self.pos = Vector2D(10,22);
		self.hitbox = Hitbox(self.pos,Vector2D(11,3))
		self.texture.add_Frame(0,2,load_texture("entity",1),fore_color = colorama.Fore.CYAN,style = colorama.Style.BRIGHT);
		self.texture.add_Frame(0,3,load_texture("entity",0),fore_color = colorama.Fore.WHITE,style = colorama.Style.BRIGHT);
	
	#bewegt den Spieler und setzt seine blickrichtung
	def move_player(self,key):
		
		if(self.state != 1):
			if(key in [119,72]):
				self.pos.y -= self.speed;
				self.facing = 0;
			elif(key in [100,77]):
				self.pos.x += self.speed;
				self.facing = 1;
			elif(key in [115,80]):
				self.pos.y += self.speed;
				self.facing = 2;
			elif(key in [97,75]):
				self.pos.x -= self.speed;
				self.facing = 3;
			self.state = 1;
	
	#reseted die position des spielers
	def res_pos(self,view_hitbox):
		if(self.hitbox.x2 >= view_hitbox.x2+1):	self.pos.x -= 0.5;
		elif(self.hitbox.x <= view_hitbox.x+6):	self.pos.x += 0.5;
		if(self.hitbox.y2 > 50):	self.pos.y -= 0.5;
		elif(self.hitbox.y < 3):	self.pos.y += 0.5;
			
	#updated alle daten des spielers
	def update(self):
		if(self.hp <= 0):	self.isAlive = False;
		if(self.dmg_timer > 0):	self.dmg_timer -= 1;
		else:	self.dmg = 2;
		if(self.cooldown_timer > 0):	self.cooldown_timer -= 1;
		
		if(self.invincibility_timer > 0):
			self.invincibility_timer -= 1;
			self.state = 3;
		else:
			self.invincibility = False;
			if(self.shield):
				self.state = 2;
				self.hitbox.size.x = 18;
			else:
				self.hitbox.size.x = 11;
				self.state = 0;
				
		self.texture.update(0,self.state);
		self.hitbox.update_pos(self.pos);
	
	#erstellt ein schuss objekt wenn der cooldown abgelofen ist
	def shoot(self):
		if(self.cooldown_timer == 0):
			self.laser.append(Laser(Vector2D(self.pos.x+10,self.pos.y+1),self.dmg,0));
			self.cooldown_timer = 1;
	
	#setzt powerup ein
	def act_powerup(self,type):
		if(type == 1):	self.hp += 1;
		elif(type == 3):	self.act_dmg();
		elif(type == 2):	self.shield = True;
	
	#aktiviert damage powerup
	def act_dmg(self):
		self.dmg_timer = 90;
		self.dmg = 5;
	
	#aktiviert iframes
	def act_iframes(self,dmg):
		if(not self.invincibility):
			if(self.shield):
				self.shield = False;
			else:
				self.hp -= dmg;
			self.invincibility_timer = 15;
			self.invincibility = True;
	
	#löscht alle daten für den neuerstell des spielers
	def delete(self):
		self.pos = None;
		self.hitbox = None;
		self.texture = None;
		
		