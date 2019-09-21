
#sector class
class Sector:
	range = (0,0);
	speed = 0;
	isFinished = False;
	enemies = [];
	powerups = [];
	obstacles = [];
	
	#constructor übergibt die range, gegner, powerups sowie hindernisse des spiels
	def __init__(self, range, speed, enemies, powerups, obstacles):
		self.range = range;
		self.speed = speed;
		self.enemies = enemies;
		self.powerups = powerups;
		self.obstacles = obstacles;
	
	#checkt ob raum leer ist
	def update(self):
		if(len(self.enemies) <= 0):
			self.isFinished = True;
	
	#löscht alle inneren objects für das neuerstellen
	def delete(self):
		for i in self.enemies + self.powerups + self.obstacles:
			i.delete();
		self.enemies = [];
		self.powerups = [];
		self.obstacles = [];
			