import turtle
import sys

turtle.tracer(2)

# variables tracking position and direction
position_x = 0
position_y = 0
min_y, max_y = -250, 250
min_x, max_x = -250, 250
directions = ['forward', 'right', 'back', 'left']
current_direction_index = 0
robot = turtle.Turtle()
screen = turtle.Screen()

def set_up_robot_environment():
    screen.bgcolor("#141D2A")
    screen.setup(width=720, height=1000)
    screen.title("Robot Environment")
    robot.pencolor("#4E9A06")
    robot.penup()
    robot.home()
    robot.setheading(90)
    robot.pensize(2)
    draw_obstacles()
    turtle.update()
    
def set_border():
    robot.speed(10)
    robot.setheading(90)
    robot.penup()
    robot.setx(-250)
    robot.sety(-250)
    robot.pendown()
    robot.pensize(5)
    for i in range(4):
        robot.forward(500)
        robot.right(90)
    robot.penup()
    robot.home()
    robot.setheading(90)
    turtle.update()


def draw_obstacles():
    slave = turtle.Turtle()
    for x, y in obs.obstacles_list:
        slave.penup(), slave.goto(x, y), slave.pendown()
        for i in range(4):
            slave.fd(4)
            slave.lt(90)
    slave.hideturtle()


def show_position(robot_name):
    print(' > '+robot_name+' now at position ('+str(position_x)+','+str(position_y)+').')


def is_position_allowed(new_x, new_y):
    """
    Checks if the new position will still fall within the max area limit
    :param new_x: the new/proposed x position
    :param new_y: the new/proposed y position
    :return: True if allowed, i.e. it falls in the allowed area, else False
    """

    return min_x <= new_x <= max_x and min_y <= new_y <= max_y


def update_position(steps, robot_name):
    """
    Update the current x and y positions given the current direction, and specific nr of steps
    :param steps:
    :return: True if the position was updated, else False
    """

    global position_x, position_y
    new_x = position_x
    new_y = position_y
 
    if directions[current_direction_index] == 'forward':
        new_y += steps
    elif directions[current_direction_index] == 'right':
        new_x += steps
    elif directions[current_direction_index] == 'back':
        new_y -= steps
    elif directions[current_direction_index] == 'left':
        new_x -= steps

    if obs.is_position_blocked(new_x, new_y) or (
        obs.is_path_blocked(new_x, new_y, position_x, position_y)):
            return None 

    if is_position_allowed(new_x, new_y):
        position_x = new_x
        position_y = new_y
        robot.forward(steps)
        turtle.update()
        return True
    else:
        return False


def do_forward(robot_name, steps):
    """
    Moves the robot forward the number of steps
    :param robot_name:
    :param steps:
    :return: (True, forward output text)
    """
    do_next = update_position(steps, robot_name)
    
    if do_next:
        return True, ' > '+robot_name+' moved forward by '+str(steps)+' steps.'
    elif do_next == None:
        return True, f"{robot_name} Sorry, there is an obstacle in the way."
    else:
        return True, ''+robot_name+': Sorry, I cannot go outside my safe zone.'


def do_back(robot_name, steps):
    """
    Moves the robot forward the number of steps
    :param robot_name:
    :param steps:
    :return: (True, forward output text)
    """
    do_next = update_position(-steps, robot_name)

    if do_next:
        return True, ' > '+robot_name+' moved back by '+str(steps)+' steps.'
    elif do_next == None:
        return True, f"{robot_name} Sorry, there is an obstacle in the way."
    else:
        return True, ''+robot_name+': Sorry, I cannot go outside my safe zone.'


def do_right_turn(robot_name):
    """
    Do a 90 degree turn to the right
    :param robot_name:
    :return: (True, right turn output text)
    """
    global current_direction_index

    current_direction_index += 1
    if current_direction_index > 3:
        current_direction_index = 0
    robot.right(90)
    turtle.update()
    
    return True, ' > '+robot_name+' turned right.'


def do_left_turn(robot_name):
    """
    Do a 90 degree turn to the left
    :param robot_name:
    :return: (True, left turn output text)
    """
    global current_direction_index

    current_direction_index -= 1
    if current_direction_index < 0:
        current_direction_index = 3
    robot.left(90)
    turtle.update()

    return True, ' > '+robot_name+' turned left.'
