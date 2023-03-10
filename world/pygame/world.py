import pygame
import os

#border of world
width, height = 900, 900

#color declaration constants
SILVER = (192, 192, 192)
BLUE = (50, 80, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

#graphics declaration constants
FPS = 60

#robot declaration constants
ROBO_WIDTH, ROBO_HEIGHT = 40, 40

#world declaration constants
WIN = pygame.display.set_mode((width, height))

def setup_world():
    WIN.fill(BLUE)


def main():
    
    run = True
    clock = pygame.time.Clock()
    
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        setup_world()
    
    pygame.quit()


if __name__ == '__main__':
    main()