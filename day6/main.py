import curses
import time
def read_from_file(path):
    with open(path, 'r') as f:
        return f.read()

def find_guard(maze):
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if maze[i][j] == '^':
                return i, j
    return 0, 0

def calc(i, guard_pos, radius, maze):
    return guard_pos - radius + i    

def draw_torch_aura(init_line, window, maze, x, y):
    radius = 9
    for i in range(init_line, radius*2+1+init_line):
        for j in range(init_line, radius*2+1+init_line):
            xx = calc(i, x, radius, maze)
            yy = calc(j, y, radius, maze)
            if xx <=0:
                char = '-'
            elif yy <=0:
                char = '|'
            elif xx >= len(maze)-1:
                char = '-'
            elif yy >= len(maze[0])-1:
                char = '|'
            else:
                char = maze[xx][yy]
            window.addstr(i, j, char)


def move_guard(maze, x, y):
    wall = '#'
    up = '^'
    down = 'v'
    left = '<'
    right = '>'
    p = '.'
    space = ' '

    guard = maze[x][y]
    maze_width = len(maze[0])
    maze_height = len(maze)

    if guard == up:
        if x > 0 and maze[x-1][y] == wall:
            maze[x][y] = right
            return x, y, False
        elif x > 0:
            distinct = maze[x-1][y] == "."
            maze[x][y] = space
            maze[x-1][y] = up
            return x-1, y, distinct
    elif  guard == right:
        if maze_width-1 > y and maze[x][y+1] == wall:
            maze[x][y] = down
            return x, y, False
        elif maze_width-1 > y:
            distinct = maze[x][y+1] == p
            maze[x][y] = space
            maze[x][y+1] = right
            return x, y+1, distinct
    elif guard == down:
        if maze_height-1 > x and maze[x+1][y] == wall:
            maze[x][y] = left
            return x, y, False
        elif maze_height-1 > x:
            distinct = maze[x+1][y] == p
            maze[x][y] = space
            maze[x+1][y] = down
            return x+1, y, distinct
    elif guard == left:
        if y > 0 and maze[x][y-1] == wall:
            maze[x][y] = up
            return x, y, False
        elif y > 0:
            distinct = maze[x][y-1] == p
            maze[x][y] = space
            maze[x][y-1] = left
            return x, y-1, distinct
    return x, y, False

def solve_maze(window):
    x = 0
    y = 0
    maze_init_x = 1
    maze_lines = read_from_file('input.txt').split('\n')
    maze = []
    for line in maze_lines:
        maze_line = []
        for char in line:
            maze_line.append(char)
        maze.append(maze_line)
    
    guard_x, guard_y = find_guard(maze)
    window = curses.initscr()
    window.clear()
    window.refresh()
    window.resize(len(maze[0]) + 1, len(maze) + 1)
    x += 1
    all_move = 1
    while guard_x != 0 or guard_y != 0:
        window.addstr(0, 0, 'Guard location: {},{}, Moves: {} |'.format(guard_x, guard_y, all_move))
        draw_torch_aura(maze_init_x, window, maze, guard_x, guard_y) 
        guard_x, guard_y, distinct = move_guard(maze, guard_x, guard_y)
        if distinct:
            all_move += 1

        previous_guard = (guard_x, guard_y)
        # time.sleep(0.1)
        window.refresh()
        x = maze_init_x
    window.refresh()

if __name__ == "__main__":
    curses.wrapper(solve_maze)