from collections import deque

# setup lists
walls = []
path = []
visited = set()
queue = deque()
solution = {}

def setup_maze(maze):
    """
    Set up the maze

    Args:
        Takes in 2d list that generates the maze
    """
    global start_x, start_y, bottom_x, bottom_y, top_x, top_y, left_x, left_y, right_x, right_y
    for y in range(len(maze)):
        for x in range(len(maze[y])):
            character = maze[y][x]
            screen_x = -100 + (x * 20)
            screen_y = 200 - (y * 20)

            if character == "#":
                walls.append((screen_x, screen_y))

            if character == "-" or character == "t" or character == "b" or character == "l" or character == "r":
                path.append((screen_x, screen_y))

            if character == "b":
                bottom_x, bottom_y = screen_x,screen_y

            if character == "t":
                top_x, top_y = screen_x,screen_y

            if character == "l":
                left_x, left_y = screen_x,screen_y

            if character == "r":
                right_x, right_y = screen_x,screen_y

            if character == "s":
                start_x, start_y = screen_x, screen_y


def search(x,y):
    """
    Breadth first search algo implementation

    Args:
        x : Coordinate of maze
        y : Coordinate of maze
    """    
    queue.append((x, y))
    solution[x,y] = x,y

    while len(queue) > 0:
        x, y = queue.popleft()

        # check the cell on the left
        if(x - 20, y) in path and (x - 20, y) not in visited:  
            cell = (x - 20, y)
            # backtracking, [cell] is the previous cell. x, y is the current cell
            solution[cell] = x, y
            queue.append(cell)
            visited.add((x-20, y))

        # check the cell down
        if (x, y - 20) in path and (x, y - 20) not in visited:  
            cell = (x, y - 20)
            solution[cell] = x, y
            queue.append(cell)
            visited.add((x, y - 20))

        # check the cell on the  right
        if(x + 20, y) in path and (x + 20, y) not in visited:
            cell = (x + 20, y)
            solution[cell] = x, y
            queue.append(cell)
            visited.add((x +20, y))

        # check the cell up
        if(x, y + 20) in path and (x, y + 20) not in visited:
            cell = (x, y + 20)
            solution[cell] = x, y
            queue.append(cell)
            visited.add((x, y + 20))
    
    solution_reversed = dict(reversed(list(solution.items())))

def mazerun():
    """
    Function to figure out what commands to use to get the robot to the top of the screen
    """
    print('starting maze run..')
    search(start_x, start_y)
    backroute(top_x, top_y)
    
    return True, 'I am at the top edge'


def mazerun_right():
    """
    Function to figure out what commands to use to get the robot to the top of the screen
    """
    print('starting maze run..')
    search(start_x,start_y)
    backroute(right_x, right_y)

    return True, 'I am at the right edge'


def mazerun_left():
    """
    Function to figure out what commands to use to get the robot to the top of the screen
    """
    print('starting maze run..')
    search(start_x,start_y)
    backroute(left_x, left_y)

    return True, 'I am at the left edge'


def mazerun_bottom():
    """
    Function to figure out what commands to use to get the robot to the top of the screen
    """
    print('starting maze run..')
    search(start_x,start_y)
    backroute(bottom_x, bottom_y)

    return True, 'I am at the bottom edge'


def backroute(x, y):
    robot.goto(solution[start_x, start_y])
    mylisyt = []
    while (x, y) != (start_x, start_y):
        mylisyt.append(solution[x, y])
        turtle.update()
        x, y = solution[x, y]    
    mylisyt.reverse()
    for i in mylisyt:
        robot.goto(i)
        turtle.update()

if __name__ != "__main__":
    setup_maze(maze.maze)
