import time
import random
import pygame
import os
pygame.font.init()
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
VEL = 10
OBS_WIDTH, OBS_HEIGHT = 50, 50
max_obs = 10

# obstacle declaration constants
ASTEROID_IMAGE = pygame.transform.scale(pygame.image.load(
    os.path.join('Assets', 'asteroid.png')), (OBS_WIDTH, OBS_HEIGHT))

GAME_OVER = pygame.transform.scale(pygame.image.load(
    os.path.join('Assets', 'game-over.png')), (900,900))

# variables recieved from robot.py
asteroids = []

# event declaration
USER_HIT = pygame.USEREVENT + 1
ASTEROID_HIT = pygame.USEREVENT + 2

# font declaration
HEALTH_FONT = pygame.font.SysFont('comicsans', 40)



class Asteroid:
    def __init__(self, x, y, velocity, image):
        self.x = x
        self.y = y
        self.velocity = velocity
        self.image = image
        self.width = OBS_WIDTH
        self.height = OBS_HEIGHT


def detect_collision_on_asteroid():
    for bullet in bullets:
        for ast, obs in asteroids:
            if bullet.colliderect(obs):
                pygame.event.post(pygame.event.Event(ASTEROID_HIT))
                asteroids.remove((ast, obs))
                bullets.remove(bullet)


def detect_collision_on_player():
    for ast, obs in asteroids:
        if robot.colliderect(obs):
            pygame.event.post(pygame.event.Event(USER_HIT))
            asteroids.remove((ast,obs))


def end_game():
    global robot_health, robot, elapsed_time
    
    elapsed_time = 0
    asteroids.clear()
    # pygame.time.delay(5000)
    robot_health = 10
    robot.x = width//2-ROBOT.get_width()
    robot.y = height-100
    

def create_bullet():
    global bullets
    
    bullet = pygame.Rect(
        robot.x, robot.y + robot.height//2-2, 5, 10
    )
    bullets.append(bullet)


def move_bullets():
    global bullets

    for bullet in bullets:
        bullet.y -= 15
        if bullet.y < 0:
            bullets.remove(bullet)


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
    
    if keys_pressed[pygame.K_b]:
        create_bullet()


def setup_world():
    global asteroids, robot_health, end, game_over_timer, elapsed_time
    
    if end:
        if game_over_timer > 0:
            asteroids = []
            WIN.fill(BLACK)
            game_over_text = HEALTH_FONT.render(f"GAME OVER", 1, SILVER)
            WIN.blit(game_over_text, (350, 10))
            # WIN.blit(GAME_OVER, (0, 0))
            game_over_timer -= 1
        else:
            asteroids = []
            robot_health = 10
            end = False
            game_over_timer = 250
            elapsed_time = 0
    else:
        WIN.blit(VOID, (0, 0))
        time_text = HEALTH_FONT.render(f"{round(elapsed_time)}s", 1, 'white')
        WIN.blit(time_text, (10, 10))
        health_bar = HEALTH_FONT.render("HEALTH: "+str(robot_health), 1, SILVER)
        WIN.blit(health_bar, (350, 10))
        create_asteroid()

    
    WIN.blit(ROBOT, (robot.x, robot.y))

    for bullet in bullets:
        pygame.draw.rect(WIN, RED, bullet)

    for ast, obs in asteroids:
        WIN.blit(ast.image, (ast.x, ast.y))
    move_asteroids()
    

    pygame.display.update()

def main():
    global robot, robot_health, end, elapsed_time, game_over_timer, bullets

    robot = pygame.Rect(width//2-ROBOT.get_width(),
                        height-100, ROBO_WIDTH, ROBOT_HEIGHT)
    robot_health = 10

    run = True
    clock = pygame.time.Clock()
    start_time = time.time()
    elapsed_time = 0
    end = False
    game_over_timer = 250
    bullets = []

    while run:
        clock.tick(FPS)
        elapsed_time = time.time() - start_time
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == USER_HIT:
                robot_health -= 1
                if robot_health == 0:
                    end = True
                    end_game()
        
        move_bullets()
        detect_collision_on_asteroid()
        detect_collision_on_player()
        setup_world()
        listen()

    pygame.quit()


if __name__ == '__main__':
    main()
