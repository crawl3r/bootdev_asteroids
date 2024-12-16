import pygame
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            rand_angle = random.uniform(20, 50)
            forward_a = self.velocity.rotate(rand_angle)
            forward_b = self.velocity.rotate(-rand_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS

            ast_a = Asteroid(self.position.x, self.position.y, new_radius)
            ast_b = Asteroid(self.position.x, self.position.y, new_radius)

            ast_a.velocity = forward_a * 1.2
            ast_b.velocity = forward_b * 1.2

    def draw(self, screen):
        pygame.draw.circle(
            surface=screen, 
            color=(255,255,255), 
            center=self.position, 
            radius=self.radius
        )

    def update(self, dt):
        self.position += (self.velocity * dt)