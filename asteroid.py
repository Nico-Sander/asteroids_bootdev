import random

import pygame

from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius) 

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()     # kill the original asteroid either way

        if self.radius <= ASTEROID_MIN_RADIUS:      # no splitting required if the asteroid was small.
            return
        
        random_angle = random.uniform(20, 50) 
        new_rotation_plus, new_rotation_minus = self.velocity.rotate(random_angle), self.velocity.rotate(-random_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        new_asteroid_plus = Asteroid(self.position[0], self.position[1], new_radius)
        new_asteroid_minus = Asteroid(self.position[0], self.position[1], new_radius)
        
        new_asteroid_plus.velocity = new_rotation_plus * 1.2
        new_asteroid_minus.velocity = new_rotation_minus * 1.2

        



