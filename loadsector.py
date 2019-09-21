import enemy
from obstacle import Obstacle
from powerup import PowerUp
from vector2d import Vector2D

#holt die Daten für Sektor 1 vom Level
def get_sector_1():
	objects = [];
	
	enemy_set = [[150,22,0],[210,18,1],[210,28,2],[240,10,3],[240,15,3],[240,30,4],[240,35,4],[240,40,4]];
	enemies = [enemy.StrongEnemy(Vector2D(345,22),5)];
	for i in range(0,7):
		enemies.append(enemy.TinyEnemy(Vector2D(enemy_set[i][0],enemy_set[i][1]),enemy_set[i][2]));
	
	objects.append(enemies);
	obstacles = [
		Obstacle(Vector2D(150,3),5),
		Obstacle(Vector2D(150,48),6),
		Obstacle(Vector2D(230,3),2),
		Obstacle(Vector2D(230,39),1)
	];
	objects.append(obstacles);
	powerups = [
		PowerUp(Vector2D(50,22),2),
		PowerUp(Vector2D(180,22),3),
		PowerUp(Vector2D(250,22),1)
	];
	objects.append(powerups);
	return objects

#holt die Daten für Sektor 2 vom Level
def get_sector_2():
	objects = [];
	
	enemies = [
		enemy.TinyEnemy(Vector2D(500,10),7),
		enemy.TinyEnemy(Vector2D(500,15),7),
		enemy.TinyEnemy(Vector2D(500,35),7),
		enemy.TinyEnemy(Vector2D(500,40),7)
	];
	objects.append(enemies);
	obstacles = [
		Obstacle(Vector2D(230,3),2),
		Obstacle(Vector2D(230,39),1),
		Obstacle(Vector2D(380,3),8),
		Obstacle(Vector2D(430,27),7)
	];
	objects.append(obstacles);
	powerups = [
	];
	objects.append(powerups);
	return objects

#holt die Daten für Sektor 3 vom Level
def get_sector_3():
	objects = [];
	
	enemies = [
		enemy.StrongEnemy(Vector2D(525,25),7),
		enemy.TinyEnemy(Vector2D(610,32),0),
		enemy.TinyEnemy(Vector2D(620,37),0),
		enemy.TinyEnemy(Vector2D(610,42),0)
	];
	objects.append(enemies);
	obstacles = [
		Obstacle(Vector2D(380,3),8),
		Obstacle(Vector2D(430,27),7),
		Obstacle(Vector2D(525,3),5),
		Obstacle(Vector2D(525,48),6),
		Obstacle(Vector2D(590,3),8),
		Obstacle(Vector2D(610,3),8),
		Obstacle(Vector2D(630,3),8)
	];
	objects.append(obstacles);
	powerups = [
	];
	objects.append(powerups);
	return objects
	
	
#holt die Daten für den Boss Sektor vom Level	
def get_sector_end():
	objects = [];
	
	enemies = [
		enemy.Boss(Vector2D(720,20),6)
	];
	objects.append(enemies);
	obstacles = [
		Obstacle(Vector2D(525,3),5),
		Obstacle(Vector2D(525,48),6),
		Obstacle(Vector2D(590,3),8),
		Obstacle(Vector2D(610,3),8),
		Obstacle(Vector2D(630,3),8),
		Obstacle(Vector2D(705,3),2),
		Obstacle(Vector2D(705,39),1)
	];
	objects.append(obstacles);
	powerups = [
		PowerUp(Vector2D(670,4),2),
		PowerUp(Vector2D(685,4),3),
		PowerUp(Vector2D(670,7),2),
		PowerUp(Vector2D(685,7),3),
		PowerUp(Vector2D(670,45),1),
		PowerUp(Vector2D(685,45),1)
	];
	objects.append(powerups);
	return objects