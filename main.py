import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
import sys

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    game_clock = pygame.time.Clock()
    dt = 0

    asteroids = pygame.sprite.Group()
    bullets = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Player.containers = (updatable, drawable)
    Shot.containers = (bullets, updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # update loop
        for u in updatable:
            u.update(dt)

        # collision check loops
        for a in asteroids:
            if a.is_colliding(player):
                print("Game over!")
                sys.exit(0)

        for a in asteroids:
            for b in bullets:
                if a.is_colliding(b):
                    a.split()
                    b.kill()

        # render loop
        screen.fill((0, 0, 0))
        
        for d in drawable:
            d.draw(screen)

        pygame.display.flip()
        dt = game_clock.tick(60) / 1000

if __name__ == "__main__":
    main()