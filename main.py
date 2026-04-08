import sys
import pygame

from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import SCREEN_WIDTH
from constants import SCREEN_HEIGHT
from logger import log_state
from player import Player
from logger import log_event
from shot import Shot

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(
        f"Screen width: {SCREEN_WIDTH}\n" +
        f"Screen height: {SCREEN_HEIGHT}"
    )
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    gameloop_clock = pygame.time.Clock()
    delta_seconds = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)
    player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()
    while True:
        log_state()
        for event in pygame.event.get():
            pass
        screen.fill("black")
        updatable.update(delta_seconds)
        for asteroid in asteroids:
            if player.collides_with(asteroid):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
            for shot in shots:
                if shot.collides_with(asteroid):
                    shot.kill()
                    asteroid.kill()
                    break;
        for sprite in drawable:
            sprite.draw(screen)
        pygame.display.flip()
        delta_seconds = gameloop_clock.tick(60) / 1000

if __name__ == "__main__":
    main()
