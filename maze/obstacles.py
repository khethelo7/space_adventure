# -------------------------------------------------------------------------------------------------
#
# TODO: Please replace this placeholder code with your solution for Toy Robot 4, and work from there.
#
# -------------------------------------------------------------------------------------------------

import turtle
import random

colors = ["light green", "gray", "maroon", "yellow", "orange", "coral", "gold", "white"]
obstacles_list = []

def is_position_blocked(new_x, new_y):
    """
    A function that returns True if the position
    x, y falls inside an obstacle

    Args:
        x (int): Coordinates of the x position
        y (int): Coordinates of the y position
    """
    for index, tuple in enumerate(obstacles_list):
        if new_x in range(tuple[0], tuple[0]+5) and new_y in range(tuple[1], tuple[1]+5):
            return True
        
    return False


def is_path_blocked(x1, y1, x2, y2):
    """
    A function that returns True if there is an
    obstacle in the line between the coordinates (x1, y1) and (x2, y2)

    Args:
        x1 (int): Coordinates of the first point
        y1 (int): Coordinates of the first point
        x2 (int): Coordinates of the second point
        y2 (int): Coordinates of the second point
    """
    if x1 == x2:
        if y1 > y2:
            for i in range(y2, y1):
                if is_position_blocked(x1, i):
                    return True

        if  y1 < y2:
            for i in range(y1, y2):
                if is_position_blocked(x1, i):
                    return True
        
        return False


    if y1 == y2:
        if x1 > x2:
            for i in range(x2, x1):
                if is_position_blocked(i, y1):
                    return True

        if x1 < x2:
            for i in range(x1, x2):
                if is_position_blocked(i, y1):
                    return True
        
        return False


def create_turtle(x_pos, y_pos):
    """
    A function that creates a turtle

    Args:
        x_pos (int): x position of the turtle
        y_pos (int): y position of the turtle

    Returns:
        asteroid (turtle object)
    """
    asteroid = turtle.Turtle()
    asteroid.speed(0)
    asteroid.fillcolor(random.choice(colors))
    asteroid.penup()
    asteroid.goto(x_pos, y_pos)
    asteroid.pendown()
    asteroid.begin_fill()
    for i in range(4):
        asteroid.forward(5)
        asteroid.right(90)

    asteroid.end_fill()
    asteroid.hideturtle()
    turtle.update()


def print_obstacles(robot_name):
    """
    A function to print all the available obstacles
    """
    if obstacles_list:
        print(f"{robot_name}: Loaded obstacles.")
        print("There are some obstacles:")
        for index, tuple in enumerate(obstacles_list):
            x = tuple[0]
            y = tuple[1]
            print(f"- At position {x},{y} (to {x+4},{y+4})")


def get_obstacles(obstacles):
    global obstacles_list

    obstacles_list = obstacles


def pass_x_y(obstacles_list):
    for tuple in obstacles_list:
        create_turtle(tuple[0], tuple[1])