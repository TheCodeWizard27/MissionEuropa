import time
import getch
import threading
from graphics import Graphics
from input import Input
from level import Level
from titlescreen import Titlescreen
from gameover import Gameover

#Class für die Engine in der das Spiel verwaltet wird
class Engine:
	graphics = Graphics();
	room_index = 0;
	input = Input();
	run = True;
	
	#Startet das Spiel und input thread
	def __init__(self):
		input_thread = threading.Thread(target=self.getinput);
		input_thread.start();
	
		while(self.run):
			self.room_switch();
	
	#Holt input und fügt ihn dem Input_buffer hinzu
	def getinput(self):
		while(self.run):
			self.input.add_input(ord(getch.getch()));
		
	#Wechselt room
	def room_switch(self):
		if (self.room_index == 0):
			self.room_index = self.main_loop(Titlescreen);
		elif(self.room_index == 1):
			self.room_index = self.main_loop(Level);
		elif(self.room_index == 2):
			self.room_index = self.main_loop(Gameover);
		else:
			self.run = False;
		
	#main loop berechnet zeit zum pausieren und ruft room funktionen auf
	def main_loop(self,room_class):
	
		room = room_class();
		
		while(room.run):
			
			start_time = time.time();
			
			#inner loop
			
			room.update(self.input);
			room.draw();
			
			#-----
			
			end_time = time.time();
			
			if(end_time - start_time < 1000./self.graphics.frame_limit and end_time - start_time >= 0):
				time.sleep((1000./self.graphics.frame_limit - (end_time - start_time))/1000);
				
		end = room.ends_with();
		room.clear_objects();
		del room;
		
		return end;