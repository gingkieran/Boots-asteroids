from turtle import position

import pygame
import random

from pygame.transform import rotate
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_event

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)
    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen,"white",self.position,self.radius,LINE_WIDTH)

    def update(self, dt: float) -> None:
        self.position += (self.velocity*dt)


    def split(self) -> None:
        self.kill()
        old = self.radius
        position = self.position
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            rnd = random.randint(20, 50)
            new_radius = old - ASTEROID_MIN_RADIUS
            first_direction = self.velocity.rotate(rnd)
            second_direction = self.velocity.rotate(-rnd)
            new_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
            old_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
            new_asteroid.velocity = first_direction * 1.2
            old_asteroid.velocity = second_direction * 1.2
