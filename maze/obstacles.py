#IMPORTS
import turtle
import random

#GLOBALS
obs = []
width, length = 4, 4

def set_obstacles(obx, oby):
    """Draws the obstacles using Turtle if world.turtle.world is loaded

    Args:
        obx (int): the obstacles x pos
        oby (int): the obstacles y pos
    """
    o = turtle.Turtle()
    o.speed(0)
    o.penup(), o.goto(obx, oby), o.pendown()
    o.pencolor("teal")
    o.begin_fill()
    o.fillcolor("teal")
    o.fd(width), o.lt(90), o.fd(length)
    o.lt(90), o.fd(width), o.lt(90)
    o.fd(length), o.lt(90)
    o.end_fill(), o.hideturtle()
    del o


def is_position_blocked(new_x, new_y):
    """Checks if the position the robot is trying to go to is an obstacles pos or not

    Args:
        new_x (int): the x pos the robot is trying to go to
        new_y (int): the y pos the robot is trying to go to

    Returns:
        bool: True or False depending on the obstacles pos in the world
    """
    for obx, oby in obs:
        if new_x in range(obx, obx+5) and new_y in range(oby, oby+5):
            return True
    return False


def is_path_blocked(x1, y1, x2, y2):
    """Checks if there is an obstacle between x1,y1 and x2,y2

    Args:
        x1 (int): initial x value of robot
        y1 (int): initial y value of robot
        x2 (int): destination x value robot is going to
        y2 (int): destination y value robot is going to

    Returns:
        bool: True or False depending on whether there is obstacle in path or not
    """
    if x1 == x2:
        if y1 > y2:
            for i in range(y2, y1):
                if is_position_blocked(x1, i):
                    return True
        elif y2 > y1:
            for i in range(y1, y2):
                if is_position_blocked(x1, i):
                    return True
    if y1 == y2:
        if x1 > x2:
            for i in range(x2, x1):
                if is_position_blocked(i, y1):
                    return True
        elif x2 > x1:
            for i in range(x1, x2):
                if is_position_blocked(i, y1):
                    return True
    return False

def get_obstacles(obstacles):
    """Recevies randomly generated obstacle list from main file

    Args:
        obstacles (list): random obstacle list
    """
    global obs

    obs = obstacles

def call_set_obstacles():
    """Will run set obstacles in a for loop

    Args:
        obs (list): carries a list with random obstacles
    """
    for obx, oby in obs:
        set_obstacles(obx, oby)