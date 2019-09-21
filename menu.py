import colorama
from view import View
from drawengine import Graphics
from obj import Obj
from loadtexture import load_texture
from vector2d import Vector2D

#menu vater class
class Menu:
	endswith = 1;
	view = View();
	run = True;
	room_objects = [];
	menu_i = 0;
	
	#updated menu objekte mit highlights sowie zeichen
	def update(self,input):
		while(len(input.input_buffer) > 0):
			key = input.get_input();
			if(key in [119,115,72,80]):
				if(self.menu_i == 0):
					self.menu_i = 1;
				else:
					self.menu_i = 0;
			elif(key in [32,13]):
				self.run = False;
				if(self.menu_i == 1):
					self.endswith = -1;
					
			input.rm_input();
			
		if(self.menu_i == 0):
			self.room_objects[3].texture.style = self.room_objects[1].texture.style = colorama.Style.BRIGHT;
			self.room_objects[3].texture.texture += " <" if " <" not in self.room_objects[3].texture.texture else "";
			self.room_objects[4].texture.style = self.room_objects[2].texture.style = colorama.Style.DIM;
			self.room_objects[4].texture.texture = self.room_objects[4].texture.texture.replace(" <","");
		else:
			self.room_objects[3].texture.style = self.room_objects[1].texture.style = colorama.Style.DIM;
			self.room_objects[3].texture.texture = self.room_objects[3].texture.texture.replace(" <","");
			self.room_objects[4].texture.style = self.room_objects[2].texture.style = colorama.Style.BRIGHT;
			self.room_objects[4].texture.texture += " <" if " <" not in self.room_objects[4].texture.texture else "";
	
	#zeichnet menu
	def draw(self):
		Graphics.draw(self.room_objects,self.view);
	
	#dummy für clear_objects funktion die in der engine aufgerufen wird
	def clear_objects(self):
		pass;
	
	#gibt resultat vom menu zurück
	def ends_with(self):	return self.endswith;