import random
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
VOID = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'void.png')), (width, height))

# robot declaration constants
ROBO_WIDTH, ROBOT_HEIGHT = 40, 40
ROBOT_IMAGE = pygame.transform.scale(
    pygame.image.load(os.path.join('Assets', 'spaceship_red.png')),
    (ROBO_WIDTH, ROBOT_HEIGHT))
ROBOT = pygame.transform.rotate(ROBOT_IMAGE, 180)

# world declaration constants
WIN = pygame.display.set_mode((width, height))
VEL = 5
OBS_WIDTH, OBS_HEIGHT = 50, 50
max_obs = 10

# obstacle declaration constants
ASTEROID_IMAGE = pygame.transform.scale(pygame.image.load(
    os.path.join('Assets', 'asteroid.png')), (OBS_WIDTH, OBS_HEIGHT))

# variables recieved from robot.py
asteroids = []

# event declaration
USER_HIT = pygame.USEREVENT + 1

# font declaration
HEALTH_FONT = pygame.font.SysFont('robotoslab', 40)



class Asteroid:
    def __init__(self, x, y, velocity, image):
        self.x = x
        self.y = y
        self.velocity = velocity
        self.image = image
        self.width = OBS_WIDTH
        self.height = OBS_HEIGHT


def detect_collision():
    for ast, obs in asteroids:
        if robot.colliderect(obs):
            pygame.event.post(pygame.event.Event(USER_HIT))


def create_asteroid():
    global asteroids
    
    x = random.randint(0, width - OBS_WIDTH)
    y = 0 - OBS_HEIGHT
    velocity = random.randint(1, VEL)
    asteroid = Asteroid(x, y, velocity, ASTEROID_IMAGE)
    obs = pygame.Rect(x, y, OBS_WIDTH, OBS_HEIGHT)
    if len(asteroids) < max_obs:
        asteroids.append((asteroid,obs))
    

def move_asteroids():
    global asteroids
    
    for ast,obs in asteroids:
        ast.y += ast.velocity
        obs.y += ast.velocity
        
        if ast.y > height:
            asteroids.remove((ast,obs))


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
    global asteroids, robot_health
    
    create_asteroid()
    WIN.blit(VOID, (0, 0))

    health_bar = HEALTH_FONT.render("HEALTH: "+str(robot_health), 1, SILVER)
    WIN.blit(health_bar, (450, 10))
    WIN.blit(ROBOT, (robot.x, robot.y))
    
    for ast, obs in asteroids:
        WIN.blit(ast.image, (ast.x, ast.y))
    move_asteroids()

    pygame.display.update()

def main():
    global robot, robot_health

    robot = pygame.Rect(width//2-ROBOT.get_width(),
                        height-100, ROBO_WIDTH, ROBOT_HEIGHT)
    robot_health = 50

    run = True
    clock = pygame.time.Clock()

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == USER_HIT:
                robot_health -= 1
        
        detect_collision()
        setup_world()
        listen()

    pygame.quit()


if __name__ == '__main__':
    main()
