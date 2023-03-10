import turtle
turtle.tracer(3)

maze = [
    ['#','#','#','#','#','t','#','#','#','#'],
    ['#','-','-','-','-','-','-','-','-','#'],
    ['#','-','#','#','#','#','-','#','-','#'],
    ['#','-','#','-','-','-','-','#','-','#'],
    ['#','-','#','#','#','#','-','#','-','#'],
    ['#','-','#','-','-','-','-','#','#','#'],
    ['#','-','-','-','-','-','-','-','-','#'],
    ['#','#','#','#','#','-','#','#','-','#'],
    ['#','-','-','-','-','-','-','#','-','#'],
    ['l','-','#','#','#','#','-','#','-','#'],
    ['#','-','#','-','-','-','-','#','-','r'],
    ['#','-','-','-','-','s','-','-','-','#'],
    ['#','#','#','#','#','-','#','#','#','#'],
    ['#','-','-','-','-','-','-','-','-','#'],
    ['#','-','#','-','#','#','#','#','-','#'],
    ['#','-','#','-','#','-','-','-','-','#'],
    ['#','-','#','-','#','#','#','#','-','#'],
    ['#','-','#','-','#','-','-','-','-','#'],
    ['#','-','#','#','#','#','#','#','-','#'],
    ['#','-','-','-','-','-','-','-','-','#'],
    ['#','#','#','#','b','#','#','#','#','#']
]

walls = []
path = []

def setup_maze(maze):
    """
    Set up the maze

    Args:
        Takes in 2d list that generates the maze
    """
    screen = turtle.Screen()
    screen.bgcolor("#141D2A")
    screen.setup(width=720, height=720)
    screen.title("Maze Environment")
    wall = turtle.Turtle()
    wall.hideturtle()
    wall.speed(0)
    
    for y in range(len(maze)):
        for x in range(len(maze[y])):
            screen_x, screen_y = -100 + (x*20), 200 - (y*20)
            character = maze[y][x]
            wall.penup()
            wall.goto(screen_x, screen_y)
            wall.pendown() 
            if character == "#":
                walls.append((screen_x, screen_y))
                draw_square("#A1ED2F", wall)
                turtle.update()

            if character == "-":
                path.append((screen_x, screen_y))
                wall.penup()
                wall.fd(20)


def draw_square(color, pen):
    pen.fillcolor(color)
    pen.pencolor(color)
    pen.begin_fill()
    for i in range(4):
        pen.fd(20)
        pen.lt(90)
    pen.end_fill()
    

def is_position_blocked(new_x, new_y):
    """
    A function that returns True if the position
    x, y falls inside an obstacle

    Args:
        x (int): Coordinates of the x position
        y (int): Coordinates of the y position
    """
    for index, tuple in enumerate(walls):
        if new_x in range(tuple[0], tuple[0]+20) and new_y in range(tuple[1], tuple[1]+20):
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


def print_obstacles():
    """
    A function to print all the available obstacles.
    """
    if obstacles_list:
        print("There are some obstacles:")
        for index, tuple in enumerate(obstacles_list):
            x = tuple[0]
            y = tuple[1]
            print(f"- At position {x},{y} (to {x+20},{y+20})")


def get_obstacles(obstacles):
    global obstacles_list

    obstacles_list = walls