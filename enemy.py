import colorama
from vector2d import Vector2D
from texture import Texture
from loadtexture import load_texture
from hitbox import Hitbox
from laser import Laser
import random

#holt AI path und gibt ihn als array von richtungen zurück
def get_path(path):
	file = open("paths/paths","r");
	paths = file.readlines();
	path = list(map(int,paths[path].split(",")))
	converted_path = [];
	
	for i in path:
		converted_path.append(4);
		converted_path.append(i);
	
	return converted_path;

#Gegner vater klasse
class Enemy:
	isAlive = True;
	pos = Vector2D(0,0);
	hitbox = None;
	texture = None;
	laser = [];
	
	path_pos = 0;
	path = [];
	
	hp = 5;
	dmg = 1;
	speed = 1;
	
	#daten update von gegner und lauft denn vorgegebenen path ab
	def stat_update(self):
		if(self.path_pos < len(self.path)):
			if(self.path[self.path_pos] == 0):	self.pos.y -= self.speed;
			elif(self.path[self.path_pos] == 1):	self.pos.x += self.speed;
			elif(self.path[self.path_pos] == 2):	self.pos.y += self.speed;
			elif(self.path[self.path_pos] == 3):	self.pos.x -= self.speed;
			self.path_pos += 1;
			
		if(self.hp <= 0):
			self.isAlive = False;
			
		self.hitbox.update_pos(self.pos);
		
	#löscht alle inneren objekte für das neuerstellen
	def delete(self):
		self.pos = None;
		self.hitbox = None;
		self.texture = None;

#kleiner Gegner klasse		
class TinyEnemy(Enemy):
	
	#Konstruktor setzt position sowie path des gegners
	def __init__(self,pos,path):
		self.path = [];
		self.laser = [];
		self.path = get_path(path);
		self.pos = pos;
		self.texture = Texture(load_texture("entity",2),fore_color = colorama.Fore.CYAN);
		self.hitbox = Hitbox(pos,Vector2D(2,1));
	
	#updatet den gegner
	def update(self):
		self.stat_update();

#grosser Gegner klasse		
class StrongEnemy(Enemy):
	hp = 20;
	dmg = 2;
	cooldown_timer = 0;
	
	#Konstruktor setzt position sowie path des Gegners
	def __init__(self,pos,path):
		self.path = [];
		self.laser = [];
		self.path = get_path(path);
		self.pos = pos;
		self.texture = Texture(load_texture("entity",6),fore_color = colorama.Fore.CYAN);
		self.hitbox = Hitbox(pos,Vector2D(6,5));
	
	#updated den gegner und shiesst nach ablauf des cooldowns
	def update(self):
		self.stat_update();
		
		if(self.cooldown_timer > 0): self.cooldown_timer -= 1;
		else:	self.shoot();
	
	#erstellt schuss objekt
	def shoot(self):
		self.laser.append(Laser(Vector2D(self.pos.x -3,self.pos.y),self.dmg,1));
		self.laser.append(Laser(Vector2D(self.pos.x -3,self.pos.y + 4),self.dmg,1));
		self.cooldown_timer = random.randint(1,30);

#Boss klasse		
class Boss(Enemy):
	hp = 550;
	dmg = 1;
	cooldown_timer = 0;
	
	#erstellt boss an position und übergibt path
	def __init__(self,pos,path):
		self.path = [];
		self.laser = [];
		self.path = get_path(path);
		self.pos = pos;
		self.texture = Texture(load_texture("entity",7),fore_color = colorama.Fore.CYAN);
		self.hitbox = Hitbox(pos,Vector2D(30,8));
	
	#updatet Boss und schiesst wenn cooldown abgelaufen ist
	def update(self):
		self.stat_update();
		if(self.path_pos > len(self.path)-1): self.path_pos = 0;
		if(self.cooldown_timer > 0): self.cooldown_timer -= 1;
		else:	self.shoot();
	
	#erstellt schussobjekt vom boss
	def shoot(self):
		self.laser.append(Laser(Vector2D(self.pos.x + 7 -10,self.pos.y + 2),self.dmg,1));
		self.laser.append(Laser(Vector2D(self.pos.x + 7 -10,self.pos.y + 5),self.dmg,1));
		self.cooldown_timer = random.randint(1,30);