import turtle

# variables tracking position and direction
position_x = 0
position_y = 0
directions = ['forward', 'right', 'back', 'left']
current_direction_index = 0

# area limit vars
min_y, max_y = -200, 200
min_x, max_x = -100, 100

def is_position_allowed(new_x, new_y):
    """
    Checks if the new position will still fall within the max area limit
    :param new_x: the new/proposed x position
    :param new_y: the new/proposed y position
    :return: True if allowed, i.e. it falls in the allowed area, else False
    """
    return min_x <= new_x <= max_x and min_y <= new_y <= max_y

def update_position(robot_name, steps):
    """
    Update the current x and y positions given the current direction, and specific nr of steps
    :param steps:
    :return: True if the position was updated, else False
    """
    global position_x, position_y, robot
    new_x = position_x
    new_y = position_y

    if directions[current_direction_index] == 'forward':
        new_y = new_y + steps
    elif directions[current_direction_index] == 'right':
        new_x = new_x + steps
    elif directions[current_direction_index] == 'back':
        new_y = new_y - steps
    elif directions[current_direction_index] == 'left':
        new_x = new_x - steps

    if obstacles.is_position_blocked(new_x, new_y) or\
        obstacles.is_path_blocked(position_x, position_y, new_x, new_y):
        return None
    
    if is_position_allowed(new_x, new_y):
        position_x = new_x
        position_y = new_y
        robot.forward(steps)
        turtle.update()
        return True
    return False

def do_forward(robot_name, steps):
    """
    Moves the robot forward the number of steps
    :param robot_name:
    :param steps:
    :return: (True, forward output text)
    """
    go_on = update_position(robot_name, steps)

    if go_on == True:
        return True, ' > '+robot_name+' moved forward by '+str(steps)+' steps.'
    elif go_on == None:
        return True, f"{robot_name}: Sorry, there is an obstacle in the way."
    elif go_on == False:
        return True, ''+robot_name+': Sorry, I cannot go outside my safe zone.'

def do_back(robot_name, steps):
    """
    Moves the robot forward the number of steps
    :param robot_name:
    :param steps:
    :return: (True, forward output text)
    """
    go_on = update_position(robot_name, -steps)

    if go_on == True:
        return True, ' > '+robot_name+' moved back by '+str(steps)+' steps.'
    elif go_on == None:
        return True, f"{robot_name}: Sorry, there is an obstacle in the way."
    elif go_on == False:
        return True, ''+robot_name+': Sorry, I cannot go outside my safe zone.'
    
def do_left_turn(robot_name):
    """
    Do a 90 degree turn to the left
    :param robot_name:
    :return: (True, left turn output text)
    """
    global current_direction_index, robot
    
    current_direction_index -= 1
    if current_direction_index < 0:
        current_direction_index = 3
    
    robot.left(90)
    turtle.update()
    return True, ' > '+robot_name+' turned left.'

def do_right_turn(robot_name):
    """
    Do a 90 degree turn to the right
    :param robot_name:
    :return: (True, right turn output text)
    """
    global current_direction_index, robot
    
    current_direction_index += 1
    if current_direction_index > 3:
        current_direction_index = 0
        
    robot.right(90)
    turtle.update()
    return True, ' > '+robot_name+' turned right.'

def show_position(robot_name):
    print(' > '+robot_name+' now at position ('+str(position_x)+','+str(position_y)+').')

# The environment around the robot
env = turtle.getscreen()
env.setup(max_x*10, max_y*5)
env.bgcolor("#000221")
env.title("Toy Robot 4")

# The robot
robot = turtle.Turtle()
robot.pensize(5), robot.shape("classic")
robot.pencolor("navy blue"), robot.fillcolor("blue")
robot.speed(0)

# Seting the boundary
robot.penup(), robot.goto(min_x, max_y), robot.pendown()

for i in range(2):
    robot.forward(200)
    robot.right(90)
    robot.forward(400)
    robot.right(90)

robot.penup(), robot.home(), robot.left(90), robot.pendown(), robot.showturtle()
robot.pencolor("#000221")