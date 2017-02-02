from math import sqrt

class Bullet():
	def __init__(self, plus_x, plus_y, x, y):
		self.x = x
		self.y = y
		self.speed = 10
		self.x_speed = plus_x
		self.y_speed = plus_y
		self.x_end = plus_x
		self.y_end = plus_y
		self.length = 5
		self.correcture = 0
		self.color = (50,200,0)

	def distance_to(self, target):
		vector = (self.x - target.x, self.y - target.y)
		return abs(sqrt(vector[0]*vector[0]+vector[1]*vector[1]))

	def move(self):
		self.x += self.x_speed
		self.y += self.y_speed
		self.x_end += self.x_speed
		self.y_end += self.y_speed
