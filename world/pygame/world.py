import time
import pygame
import os
pygame.font.init()

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
FONT = pygame.font.SysFont('comicsans', 30)

# robot declaration constants
ROBO_WIDTH, ROBOT_HEIGHT = 40, 40
ROBOT_IMAGE = pygame.transform.scale(
    pygame.image.load(os.path.join('Assets', 'spaceship_red.png')),
    (ROBO_WIDTH, ROBOT_HEIGHT))
ROBOT = pygame.transform.rotate(ROBOT_IMAGE, 180)

# world declaration constants
WIN = pygame.display.set_mode((width, height))
VEL = 5


def listen():

    keys_pressed = pygame.key.get_pressed()

    if keys_pressed[pygame.K_UP] and robot.y + VEL > 0:
        robot.y -= VEL
    if keys_pressed[pygame.K_DOWN] and robot.y - VEL < height-45:
        robot.y += VEL
    if keys_pressed[pygame.K_LEFT] and robot.x - VEL > 0:
        robot.x -= VEL
    if keys_pressed[pygame.K_RIGHT] and robot.x + VEL < width-45:
        robot.x += VEL


def setup_world():
    WIN.fill(BLUE)

    time_text = FONT.render(f"{round(elapsed_time)}s", 1, 'white')
    WIN.blit(time_text, (10, 10))

    WIN.blit(ROBOT, (robot.x, robot.y))

    pygame.display.update()


def main():
    global robot, elapsed_time

    robot = pygame.Rect(width//2-ROBOT.get_width(),
                        height-100, ROBO_WIDTH, ROBOT_HEIGHT)

    run = True
    clock = pygame.time.Clock()
    start_time = time.time()
    elapsed_time = 0

    while run:
        clock.tick(FPS)
        elapsed_time = time.time() - start_time
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        setup_world()
        listen()

    pygame.quit()


if __name__ == '__main__':
    main()
