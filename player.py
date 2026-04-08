import pygame

from circleshape import CircleShape
from constants import PLAYER_RADIUS, PLAYER_SHOOT_SPEED
from constants import LINE_WIDTH
from constants import PLAYER_TURN_SPEED
from constants import PLAYER_SPEED
from constants import PLAYER_SHOOT_COOLDOWN_SECONDS
from shot import Shot


class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.__shoot_cd_timer = 0

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

    def __move(self, delta_seconds):
        unit_vector = pygame.Vector2(0, 1)
        rotated_vector = unit_vector.rotate(self.rotation)
        rotated_with_speed_vector = rotated_vector * PLAYER_SPEED * delta_seconds
        self.position += rotated_with_speed_vector

    def __shoot(self):
        if self.__shoot_cd_timer > 0:
            return
        self.__shoot_cd_timer = PLAYER_SHOOT_COOLDOWN_SECONDS
        shot = Shot(self.position.x, self.position.y)
        unit_vector = pygame.Vector2(0, 1)
        rotated_vector = unit_vector.rotate(self.rotation)
        rotated_with_speed_vector = rotated_vector * PLAYER_SHOOT_SPEED
        shot.velocity = rotated_with_speed_vector

    def update(self, delta_seconds):
        self.__shoot_cd_timer -= delta_seconds
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.__move(delta_seconds)
        if keys[pygame.K_s]:
            self.__move(-delta_seconds)
        if keys[pygame.K_a]:
            self.__rotate(-delta_seconds)
        if keys[pygame.K_d]:
            self.__rotate(delta_seconds)
        if keys[pygame.K_SPACE]:
            self.__shoot()
