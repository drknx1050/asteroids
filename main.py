import pygame

from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state
from player import Player


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

    # adds player class to updatable and drawable group
    Player.containers = (updatable, drawable)
    # initializes player instance
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

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
