import pygame

from circleshape import CircleShape
from constants import PLAYER_RADIUS
from constants import LINE_WIDTH
from constants import PLAYER_TURN_SPEED


class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), LINE_WIDTH)

    def __rotate(self, delta_seconds):
        self.rotation += delta_seconds * PLAYER_TURN_SPEED

    def update(self, delta_seconds):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.__rotate(-delta_seconds)
        if keys[pygame.K_d]:
            self.__rotate(delta_seconds)