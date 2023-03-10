import pygame
import os

# border of world
width, height = 900, 900

# color declaration constants
SILVER = (192, 192, 192)
BLUE = (50, 80, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

# graphics declaration constants
FPS = 60

# robot declaration constants
ROBO_WIDTH, ROBO_HEIGHT = 40, 40
ROBOT_IMAGE = pygame.transform.scale(
    pygame.image.load(os.path.join('Assets', 'spaceship_red.png')),
    (ROBO_WIDTH, ROBO_HEIGHT))
ROBOT = pygame.transform.rotate(ROBOT_IMAGE, 180)

# world declaration constants
WIN = pygame.display.set_mode((width, height))
VEL = 5


def listen():

    keys_pressed = pygame.key.get_pressed()

    if keys_pressed[pygame.K_UP]:
        robot.y -= VEL
    if keys_pressed[pygame.K_DOWN]:
        robot.y += VEL
    if keys_pressed[pygame.K_LEFT]:
        robot.x -= VEL
    if keys_pressed[pygame.K_RIGHT]:
        robot.x += VEL


def setup_world():
    WIN.fill(BLUE)

    WIN.blit(ROBOT, (robot.x, robot.y))

    pygame.display.update()


def main():
    global robot

    robot = pygame.Rect(width//2-ROBOT.get_width(),
                        height-100, ROBO_WIDTH, ROBO_HEIGHT)

    run = True
    clock = pygame.time.Clock()

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        setup_world()
        listen()

    pygame.quit()


if __name__ == '__main__':
    main()
