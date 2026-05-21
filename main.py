import pygame

from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField


def main():
    # initializes game
    print(f"""Starting Asteroids with pygame version: {pygame.version.ver}
Screen width: {SCREEN_WIDTH}
Screen height: {SCREEN_HEIGHT}""")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    
    # creates groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    # initializes player instance
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # create asteroids
    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    asteroidfield = AsteroidField()

    # creates an infinite game loop
    while True:
        log_state()
        for event in pygame.event.get():
            pass
        
        # draws background and calculates delta time
        screen.fill("black")
        dt = clock.tick() / 1000
        
        # updates updatables
        updatable.update(dt)

        # draws drawables
        for item in drawable:
            item.draw(screen)
        
        # draws the frame
        pygame.display.flip()
        
        # allows the exit button to function
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return


if __name__ == "__main__":
    main()
