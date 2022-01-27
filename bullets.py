from math import sqrt, sin, cos


class Bullet:
    def __init__(self, rotation, x, y):
        self.x = x
        self.y = y
        self.speed = 10
        self.rotation = rotation
        self.x_end = x + (20 * cos(rotation))
        self.y_end = y + (20 * sin(rotation))
        self.color = (200, 0, 0)

    def distance_to(self, target):
        vector = (self.x - target.x, self.y - target.y)
        return abs(sqrt(vector[0] * vector[0] + vector[1] * vector[1]))

    def move(self):
        self.x += self.speed * cos(self.rotation)
        self.y += self.speed * sin(self.rotation)
        self.x_end += self.speed * cos(self.rotation)
        self.y_end += self.speed * sin(self.rotation)
        pass
