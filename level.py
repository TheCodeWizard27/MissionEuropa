#graphical imports
import colorama
from drawengine import Graphics
from vector2d import Vector2D
from view import View
from sector import Sector
import enemy
from obstacle import Obstacle
from powerup import PowerUp
import os
import sys
from obj import Obj
from loadtexture import load_texture
import loadsector

#Object imports
from player import Player
from obj import Obj

#Level class
class Level:
	last_matrix = [];
	view = None;
	run = True;
	score_window = False;
	hud = [];
	sector = []
	player = None;
	score = 0;
	endswith = 2;

	#reseted arrays
	def __init__(self):
		self.player = Player();
		self.view = View();
		
		sector1 = loadsector.get_sector_1();
		sector2 = loadsector.get_sector_2();
		sector3 = loadsector.get_sector_3();
		sector_end = loadsector.get_sector_end();
		
		self.sector.append(Sector((0,375),0.5,sector1[0],sector1[2],sector1[1]));
		self.sector.append(Sector((360,500),1,sector2[0],sector2[2],sector2[1]));
		self.sector.append(Sector((500,650),1,sector3[0],sector3[2],sector3[1]));
		self.sector.append(Sector((650,750),0.5,sector_end[0],sector_end[2],sector_end[1]));
	
	#updated das Spiel checkt hitboxen leben usw.
	def update(self, input):
		self.input_handler(input);
		self.updater();
		self.hitbox_checker();
		self.killer();
	
	#konvertiert den input zu aktionen
	def input_handler(self,input):
		while(len(input.input_buffer) > 0):
			key = input.get_input();
			
			if(key in [119,97,115,100,72,75,80,77]):
				self.player.move_player(key);
			elif(key in [32,13]):
				if(self.score_window):
					self.run = False;
			else:
				if(not self.score_window and self.score > 0):
					self.score -= 1;
				self.player.shoot();
			input.rm_input();
	
	#updated alle relevanten ojekte
	def updater(self):
		if(self.sector[0].isFinished):
			if(len(self.sector) > 1):
				del self.sector[0];
			else:
				self.endswith = 0;
				self.score_window = True;
		
		if(self.run):
			if(self.view.hitbox.x2 < self.sector[0].range[1]):
				self.view.update(self.sector[0].speed);
				self.player.pos.x += self.sector[0].speed;
			
			self.player.update();
			
			for i in self.player.laser:
				i.update();
				
			for i in self.sector[0].enemies:
				for j in i.laser:
					j.update();
				if(i.hitbox.check_hitbox(self.view.hitbox)):
					i.update();
					
			self.sector[0].update();
	
	
	#handlet die Hitboxen
	def hitbox_checker(self):
		if(self.run):
			while(self.player.hitbox.y2 > 50 or self.player.hitbox.y < 3 or self.player.hitbox.x2 > self.view.hitbox.x2+1 or self.player.hitbox.x < self.view.hitbox.x + 6):	#checkt ob spieler im spielbereich ist
				self.player.res_pos(self.view.hitbox);
				self.player.hitbox.update_pos(self.player.pos);
							
			for i in self.sector[0].obstacles:
				for j in self.player.laser:
					if(i.hitbox.check_hitbox(j.hitbox)):
						self.player.laser.remove(j);
			
			for i in self.sector[0].powerups:
				if(i.hitbox.check_hitbox(self.player.hitbox)):
					i.isAlive = False;
					self.player.act_powerup(i.type);
			
			self.check_laser_view();
			self.check_player_gethit();
	
	#check ob alle laser objekte im sichtfeld sind und löscht sie demensprechend
	def check_laser_view(self):
		for i in self.player.laser:	#checks laser
				if(not i.hitbox.check_hitbox(self.view.hitbox)):	self.player.laser.remove(i);
				else:
					for j in self.sector[0].enemies:
						if(i in self.player.laser and i.hitbox.check_hitbox(j.hitbox)):
							j.hp -= i.dmg;
							self.score += 25;
							self.player.laser.remove(i);
							
		for i in self.sector[0].enemies:
			for j in i.laser:
				if(j.hitbox.x < self.view.hitbox.x):
					i.laser.remove(j);
				elif(j.hitbox.check_hitbox(self.player.hitbox)):
					i.laser.remove(j);
					self.player.act_iframes(i.dmg);
	
	def check_player_gethit(self):
		for i in self.sector[0].enemies + self.sector[0].obstacles:
				if(i.hitbox.check_hitbox(self.player.hitbox)):
					self.player.act_iframes(i.dmg);
	
	#löscht alle tote objekte
	def killer(self):
		if(self.run):
			if(not self.player.isAlive):
				self.run = False;
			
			for i in self.sector[0].enemies + self.sector[0].powerups + self.sector[0].obstacles:
				if(not i.isAlive or i.pos.x < self.view.pos.x):
					if(i in self.sector[0].enemies):	self.sector[0].enemies.remove(i);
					elif(i in self.sector[0].powerups):	self.sector[0].powerups.remove(i);
					elif(i in self.sector[0].obstacles):	self.sector[0].obstacles.remove(i);
					
	#zeichnet Raum
	def draw(self):
		temp_objects = [];
		
		if(self.score_window):	self.draw_score();
		else:
			if(self.run):
				for i in self.sector[0].enemies:
					for j in i.laser:
						if(j.hitbox.check_hitbox(self.view.hitbox)):
							temp_objects.append(j);
					if(i.hitbox.check_hitbox(self.view.hitbox)):
						temp_objects.append(i);
				for i in self.sector[0].obstacles:
					if(i.hitbox.check_hitbox(self.view.hitbox)):
						temp_objects.append(i);
				for i in self.sector[0].powerups:
					if(i.hitbox.check_hitbox(self.view.hitbox)):
						temp_objects.append(i);
			temp_objects.append(self.player);
			
			for i in self.player.laser:
				temp_objects.append(i);
			
			hud = [
				Obj(Vector2D(self.view.pos.x+1,2),Graphics.draw_hline(148,1)),
				Obj(Vector2D(self.view.pos.x+1,1),"HP:["+"█"*(self.player.hp*2)+" "*(10-self.player.hp*2)+"]",fore_color = colorama.Fore.RED,bg_color = colorama.Back.BLACK,style = colorama.Style.BRIGHT),
				Obj(Vector2D(self.view.pos.x+135,1),"Score:["+" "*(6-len(str(self.score)))+ str(self.score) + "]")
			];
					
			self.last_matrix = Graphics.draw(temp_objects,self.view,matrix = self.last_matrix,hud = hud);
	
	#Zeichnet Score
	def draw_score(self):
		temp_objects = [
			Obj(Vector2D(self.view.pos.x + 5,1),load_texture("other",2)),
			Obj(Vector2D(self.view.pos.x + 5,7),load_texture("other",3)),
			Obj(Vector2D(self.view.pos.x + 5,15),load_texture("other",4)),
			Obj(Vector2D(self.view.pos.x + 5,22),load_texture("other",4)),
			Obj(Vector2D(self.view.pos.x + 8,17),"Your Score : " + str(self.score)),
			Obj(Vector2D(self.view.pos.x + 8,24),"Press enter to continue...")
		];
		
		self.last_matrix = Graphics.draw(temp_objects,self.view);
	
	#löscht alle inneren Objects für den neueinsatz des levels
	def clear_objects(self):
		self.view.delete();
		self.player.delete();
		for i in self.sector:
			i.delete();
			
		self.view = None;
		self.player = None;
		self.last_matrix = [];
		self.hud = [];
		self.sector = [];
	
	#gibt zur engine zurück ob Game Over oder das Level beendet wurde	
	def ends_with(self):	return self.endswith;