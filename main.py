# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *

def main():
    print('Starting Asteroids!')
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)

    field = AsteroidField()
    player = Player(x, y)
    
    while True:
        screen.fill((0, 0, 0))

        for unit in drawable:
            unit.draw(screen)
        
        updatable.update(dt)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # this is a refresh of screen, the very last thing to be done
        dt = clock.tick(60) / 1000
        pygame.display.flip()


if __name__ == "__main__":
    main()