#Input object speicher input
class Input:
	input_buffer = [];

	#Fügt gedrückte Taste in Code am Input_buffer hinzu
	def add_input(self,key):	self.input_buffer.append(key);
	
	#holt input aus dem buffer
	def get_input(self):
		return self.input_buffer[0];
	
	#Löscht erstes element im buffer
	def rm_input(self):	del self.input_buffer[0];