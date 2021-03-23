maze = []  # matrix what about storing also the letters on this.
path = []  # fate
blacklist = []
turning_points = []
current_health = 10  # will decrease by one on every move
health_time = 10  # will reset health to this when reaching a health point.
import sys

def get_item(position):
    if len(maze) > position[0] >= 0:
        row = maze[position[0]]
        if len(row) > position[1] >= 0:
            return maze[position[0]][position[1]]


def is_any_match(it, obj):
    return len([x for x in it if x == obj]) > 0


class Tile:
    def __init__(self, pos):
        self.pos = pos

    def is_final(self):
        return is_any_match((get_item(self.left().pos), get_item(self.right().pos), get_item(self.up().pos), get_item(self.down().pos)), 'F')

    def left(self):
        return Tile((self.pos[0], self.pos[1] - 1))

    def right(self):
        return Tile((self.pos[0], self.pos[1] + 1))

    def up(self):
        return Tile((self.pos[0] - 1, self.pos[1]))

    def down(self):
        return Tile((self.pos[0] + 1, self.pos[1]))


def get_last_good_position():
    for point in reversed(turning_points):
        if point[1].count(True) > 1 and (point[0].pos, point[1].index(True)) not in blacklist:
            blacklist.append((point[0].pos, point[1].index(True)))
            global current_health
            current_health = point[2]  # restoring the health.
            return point[0]


def get_next_tile(tile):
    down, up, left, right = False, False, False, False
    if tile.is_final():
        return True

    if get_item(tile.pos) == 'H':  # we are on a health point, restore health.
        global current_health
        current_health = health_time

    if ('P', 'H').count(get_item(tile.down().pos)) > 0 and tile.down().pos not in path:  # todo shorten these significantly
        down = True

    if ('P', 'H').count(get_item(tile.up().pos)) > 0 and tile.up().pos not in path:
        up = True

    if ('P', 'H').count(get_item(tile.left().pos)) > 0 and tile.left().pos not in path:
        left = True

    if ('P', 'H').count(get_item(tile.right().pos)) > 0 and tile.right().pos not in path:
        right = True

    if (down, up, left, right).count(True) > 1:
        turning_points.append((tile, (down, up, left, right), current_health))  # we also need to restore the health.

    if down and (tile.pos, 0) not in blacklist:
        current_health -= 1
        if current_health < 0:
            return None
        return tile.down()
    if up and (tile.pos, 1) not in blacklist:
        current_health -= 1
        if current_health < 0:
            return None
        return tile.up()
    if left and (tile.pos, 2) not in blacklist:
        current_health -= 1
        if current_health < 0:
            return None
        return tile.left()
    if right and (tile.pos, 3) not in blacklist:
        current_health -= 1
        if current_health < 0:
            return None
        return tile.right()


def create_path(current_tile):
    path.append(current_tile.pos)
    next_tile = get_next_tile(current_tile)
    if next_tile is True:
        return  ##end
    if next_tile is not None:
        create_path(next_tile)
    else:  # revert and re-try
        del path[path.index(turning_points[-1][0].pos): path.index(current_tile.pos) + 1]
        create_path(get_last_good_position())


name_maze =  sys.argv[1]
name_maze_health = sys.argv[2]
health_time = int(sys.argv[3])
name_output = sys.argv[4]

file_maze = open(name_maze, "r", encoding="utf-8")
for line in file_maze:
    row = []
    for letter in line.strip("\n"):
        row.append(letter)
    maze.append(row)
file_maze.close()

current_health = 99999
pos_start = Tile(tuple(maze.index(it) for it in maze if 'S' in it) + tuple(it.index('S') for it in maze if 'S' in it))
pos_end = Tile(tuple(maze.index(it) for it in maze if 'F' in it) + tuple(it.index('F') for it in maze if 'F' in it))

sys.setrecursionlimit(15000)
create_path(pos_start)

file_output = open(name_output, "w", encoding="utf-8")  # todo sys.argv
file_output.write("Maze solution without health condition: \n")
for i in range(len(maze)):   #row
    for k in range(len(maze[i])):
        if (i, k) == pos_start.pos:
            file_output.write("S")
        elif (i, k) == pos_end.pos:
            file_output.write("F")
        elif (i, k) in path:
            file_output.write("1")
        else:
            file_output.write("0")

        if k == len(maze[i]) - 1:
            file_output.write("\n")
        else:
            file_output.write(", ")

maze = []
file_maze = open(name_maze_health, "r", encoding="utf-8")
for line in file_maze:
    row = []
    for letter in line.strip("\n"):
        row.append(letter)
    maze.append(row)
file_maze.close()
current_health = health_time

pos_start = Tile(tuple(maze.index(it) for it in maze if 'S' in it) + tuple(it.index('S') for it in maze if 'S' in it))
pos_end = Tile(tuple(maze.index(it) for it in maze if 'F' in it) + tuple(it.index('F') for it in maze if 'F' in it))
path = []
turning_points = []
blacklist = []
create_path(pos_start)

file_output.write("\nMaze solution with health condition: \n")
for i in range(len(maze)):
    for k in range(len(maze[i])):
        if (i, k) == pos_start.pos:
            file_output.write("S")
        elif (i, k) == pos_end.pos:
            file_output.write("F")
        elif (i, k) in path:
            file_output.write("1")
        else:
            file_output.write("0")

        if k == len(maze[i]) - 1:
            file_output.write("\n")
        else:
            file_output.write(", ")
