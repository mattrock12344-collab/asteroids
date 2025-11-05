from circleshape import CircleShape
import pygame
import random
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.color = (200, 200, 200)  # Light gray color for the asteroid

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.position, self.radius, width = 2)

    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()
        angle = random.uniform(20, 50)
        if self.radius < ASTEROID_MIN_RADIUS:
            return
        jeff_angle = self.velocity.rotate(angle)
        heff_angle = self.velocity.rotate(-angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        jeff = Asteroid(self.position.x, self.position.y, new_radius)
        heff = Asteroid(self.position.x, self.position.y, new_radius)
        jeff.velocity = jeff_angle * 1.2
        heff.velocity = heff_angle * 1.2