#--------------------------------------
#
# Autor: Benny
# Created: 2.12.2017
#
# Graphics class
#
#--------------------------------------

#colorama
import colorama
from vector2d import Vector2D
import sys
import time
import os
import getch
from obj import Obj

#drawing engine class
class Graphics:
	#draws to screen
	def draw(objects,view, **kwargs):
		last_matrix = kwargs.get("matrix",[]); #last matrix
		matrix = [[["","","",""] for i in range(151)] for i in range(51)]; #matrix of the Gamefield if no matrix
		background = kwargs.get("background",[Obj(Vector2D(view.pos.x,0),Graphics.draw_rect(150,50,1," "),transparent = False)]);
		hud = kwargs.get("hud",[]);
		
		matrix = Graphics.create_Matrix(matrix,background,view);    #Background gets added to Matrix
		matrix = Graphics.create_Matrix(matrix,objects,view);	#All Objects get added to Matrix
		matrix = Graphics.create_Matrix(matrix,hud,view);		#Hud if visible gets added to Matrix
		
		if(last_matrix != []):
			last_style = "";
			last_font_color = "";
			last_background_color = "";
			for y in range(0,len(last_matrix)):
				for x in range(1,len(last_matrix[y])-2):
					if(last_matrix[y][x][3] != matrix[y][x][3] or last_matrix[y][x][2] != matrix[y][x][2] or last_matrix[y][x][1] != matrix[y][x][1]):
						if(matrix[y][x][0] != last_style):
							sys.stdout.write("\033["+str(y+1)+";"+str(x+1)+"H" + matrix[y][x][0]);
							last_style = matrix[y][x][0];
							
						if(matrix[y][x][1] != last_font_color):
							sys.stdout.write("\033["+str(y+1)+";"+str(x+1)+"H" + matrix[y][x][1]);
							last_font_color = matrix[y][x][1];
							
						if(matrix[y][x][2] != last_background_color):
							sys.stdout.write("\033["+str(y+1)+";"+str(x+1)+"H" + matrix[y][x][2]);
							last_background_color = matrix[y][x][2];
		
						sys.stdout.write("\033["+str(y+1)+";"+str(x+1)+"H" + matrix[y][x][3]);
		else:
			sys.stdout.write("\033[1;1H" + Graphics.convert_Matrix(matrix));
		
		sys.stdout.flush();
		return matrix
	
	def create_Matrix(matrix,objects,view):
		#puts objects inside the matrix on the correct pos
		for obj in objects:
			if(obj.texture.visible):	#check if object is visible
				texture = obj.texture.texture.split("\n");
				for y in range(len(texture)):
					for x in range(len(texture[y])):
						if(obj.texture.transparent and texture[y][x] == " "):
							pass;
						elif(int(obj.pos.y) + y >= 0 and int(obj.pos.y) + y < 51 and int(obj.pos.x) + x - int(view.pos.x) >= 0 and int(obj.pos.x) + x - int(view.pos.x) < 150):
							matrix[int(obj.pos.y) + y][int(obj.pos.x) + x - int(view.pos.x)][0] = obj.texture.style; #inputs style into matrix
							matrix[int(obj.pos.y) + y][int(obj.pos.x) + x - int(view.pos.x)][1] = obj.texture.fore_color;	#inputs front color into matrix
							matrix[int(obj.pos.y) + y][int(obj.pos.x) + x - int(view.pos.x)][2] = obj.texture.bg_color; #inputs bg color into matrix
							matrix[int(obj.pos.y) + y][int(obj.pos.x) + x - int(view.pos.x)][3] = texture[y][x];	#inputs char into matrix
						
		return matrix;
		
	def convert_Matrix(matrix):
		#converts matrix to printable string
		string = [];
		new_matrix = [[] for i in range(len(matrix))];
		
		last_style = "";
		last_font_color = "";
		last_background_color = "";
		
		for y in range(len(matrix)):
			for x in range(len(matrix[y])):
			
				if(matrix[y][x][0] == last_style):	#checks if same style as last obj
					matrix[y][x][0] = "";
				else:
					last_style = matrix[y][x][0];
					
				if(matrix[y][x][1] == last_font_color):	#checks if same font color as last obj
					matrix[y][x][1] = "";
				else:
					last_font_color = matrix[y][x][1];
					
				if(matrix[y][x][2] == last_background_color): #checks if same background color as last obj
					matrix[y][x][2] = "";
				else:
					last_background_color = matrix[y][x][2];
					
				new_matrix[y].append("".join(matrix[y][x]));
	
		for i in new_matrix:
			string.append("".join(i));
			
		return "\n".join(string);
			
	#returns a horizontal line as a string
	def draw_hline(width,type):
		charset = [" ","─","═","█"];
		
		return charset[type]*width;
	
	#returns a vertical line as a string
	def draw_vline(height,type):
		charset = [" ","│","║","█"];
		
		return (charset[type]+"\n")*height;
	
	#return a rectangle as a string
	def draw_rect(width,height,type,fill):
		charset = ["     ","┌┐│└┘","╔╗║╚╝","█████"];
		
		rect = charset[type][0] + Graphics.draw_hline(width-2,type) + charset[type][1] + "\n";
		for i in range(height-1):
			rect = rect + charset[type][2] + fill*(width-2) + Graphics.draw_vline(1,type);
		return rect + charset[type][3] + Graphics.draw_hline(width-2,type) + charset[type][4];