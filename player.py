from math import sin, cos, pi, sqrt
import bullets
import pygame
import os


class Player:
    def __init__(self, game):
        pygame.init()
        self.game = game
        self.x = game.screen_x/2
        self.y = game.screen_y/2
        self.top_x = -40
        self.top_y = -40
        self.top_c = -30 / sqrt((self.top_x * self.top_x) + (self.top_y * self.top_y))
        self.left_x = -40
        self.left_y = -40
        self.left_c = 0
        self.right_x = -40
        self.right_y = -40
        self.right_c = 0
        self.top_rot = 0
        self.left_rot = 50
        self.right_rot = -10
        self.gun = 0
        self.lives = 10
        self.rotation_size = 2 * (pi / 180)
        self.step_size = 2
        self.rotation = 0.785398
        self.left_rotate(self.left_rot * (pi / 180))
        self.right_rotate(self.right_rot * (pi / 180))
        self.bullets = []
        self.color = (50, 200, 0)
        self.laser = pygame.mixer.Sound(os.path.join(os.getcwd(), 'assets', 'laser.ogg'))

    def shoot(self):
        self.bul_c = 10 / sqrt((self.top_x * self.top_x) + (self.top_y * self.top_y))
        self.bullets.append(
            bullets.Bullet(self.rotation, self.x + (self.top_x * self.top_c),
                           self.y + (self.top_y * self.top_c)))
        self.laser.play()

    def check_enemy_hit(self, enemy):
        death = False
        for idx, b in enumerate(self.bullets):
            if b.x > self.game.screen_x + 900 or b.x < -900 or b.y > self.game.screen_y + 900 or b.y < -900:
                del self.bullets[idx]
            elif b.distance_to(enemy) < 20:
                death = enemy.register_hit()
                del self.bullets[idx]

        return death

    def all_rotate_left(self):
        self.rotate(-self.rotation_size)

    def all_rotate_right(self):
        self.rotate(self.rotation_size)

    def left_rotate(self, rads):
        cosin = cos(rads)
        sinus = sin(rads)
        self.left_x = cosin * self.left_x - sinus * self.left_y
        self.left_y = sinus * self.left_x + cosin * self.left_y
        self.left_c = 20 / sqrt((self.left_x * self.left_x) + (self.left_y * self.left_y))

    def right_rotate(self, rads):
        cosin = cos(rads)
        sinus = sin(rads)
        self.right_x = cosin * self.right_x - sinus * self.right_y
        self.right_y = sinus * self.right_x + cosin * self.right_y
        self.right_c = 20 / sqrt((self.right_x * self.right_x) + (self.right_y * self.right_y))

    def top_rotate(self, rads):
        cosin = cos(rads)
        sinus = sin(rads)
        self.top_x = cosin * self.top_x - sinus * self.top_y
        self.top_y = sinus * self.top_x + cosin * self.top_y
        self.top_c = -30 / sqrt((self.top_x * self.top_x) + (self.top_y * self.top_y))

    def rotate(self, rads):
        self.rotation += rads
        self.left_rotate(rads)
        self.right_rotate(rads)
        self.top_rotate(rads)

    def forward_top(self):
        pass

    def forward(self):
        self.x += self.step_size * cos(self.rotation)
        self.y += self.step_size * sin(self.rotation)

    def backward(self):
        self.x -= self.step_size * cos(self.get_deg_rotation())
        self.y -= self.step_size * sin(self.get_deg_rotation())

    def get_deg_rotation(self):
        return self.rotation * (pi/180)

    def get_lives(self):
        return self.lives

    def get_gun(self):
        return self.gun
