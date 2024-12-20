# https://adventofcode.com/2024/day/15

# Part 1
import time

# 1. import data
grid = []
moves = []
with open("day15_input.txt") as f:
    while True:
        line = f.readline().strip()
        if not line:
            break
        grid.append(list(line))

    while True:
        line = f.readline().strip()
        if not line:
            break
        moves += list(line)

# print(len(grid), len(grid[0]))
# print(len(moves))

# # example data
grid1 = [
    ["#", "#", "#", "#", "#", "#", "#", "#"],
    ["#", ".", ".", "O", ".", "O", ".", "#"],
    ["#", "#", "@", ".", "O", ".", ".", "#"],
    ["#", ".", ".", ".", "O", ".", ".", "#"],
    ["#", ".", "#", ".", "O", ".", ".", "#"],
    ["#", ".", ".", ".", "O", ".", ".", "#"],
    ["#", ".", ".", ".", ".", ".", ".", "#"],
    ["#", "#", "#", "#", "#", "#", "#", "#"],
]
moves1 = list("<^^>>>vv<v>>v<<")

grid2 = [
    ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
    ["#", ".", ".", "O", ".", ".", "O", ".", "O", "#"],
    ["#", ".", ".", ".", ".", ".", ".", "O", ".", "#"],
    ["#", ".", "O", "O", ".", ".", "O", ".", "O", "#"],
    ["#", ".", ".", "O", "@", ".", ".", "O", ".", "#"],
    ["#", "O", "#", ".", ".", "O", ".", ".", ".", "#"],
    ["#", "O", ".", ".", "O", ".", ".", "O", ".", "#"],
    ["#", ".", "O", "O", ".", "O", ".", "O", "O", "#"],
    ["#", ".", ".", ".", ".", "O", ".", ".", ".", "#"],
    ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
]
moves2 = list(
    "<vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^><<><>>v<vvv<>^v^>^<<<><<v<<<v^vv^v>^vvv<<^>^v^^><<>>><>^<<><^vv^^<>vvv<>><^^v>^>vv<>v<<<<v<^v>^<^^>>>^<v<v><>vv>v^v^<>><>>>><^^>vv>v<^^^>>v^v^<^^>v^^>v^<^v>v<>>v^v^<v>v^^<^^vv<<<v<^>>^^^^>>>v^<>vvv^><v<<<>^^^vv^<vvv>^>v<^^^^v<>^>vvvv><>>v^<<^^^^^^><^><>>><>^^<<^^v>>><^<v>^<vv>>v>>>^v><>^v><<<<v>>v<v<v>vvv>^<><<>^><^>><>^v<><^vvv<^^<><v<<<<<><^v<<<><<<^^<v<^^^><^>>^<v^><<<^>>^v<v^v<v^>^>>^v>vv>^<<^v<>><<><<v<<v><>v<^vv<<<>^^v^>^^>>><<^v>>v^v><^^>>^<>vv^<><^^>^^^<><vvvvv^v<v<<>^v<v>v<<^><<><<><<<^^<<<^<<>><<><^^^>^^<>^>v<>^^>vv<^v^v<vv>^<><v<^v>^^^>>>^^vvv^>vvv<>>>^<^>>>>>^<<^v>^vvv<>^<><<v>v^^>>><<^^<>>^v^<v^vv<>v^<<>^<^v^v><^<<<><<^<v><v<>vv>>v><v^<vv<>v^<<^"
)

# for row in grid1:
#     print(row)
# print()


# 2. locate robot
def get_robot_pos(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "@":
                return (i, j)


# print(robot_pos)


# 3. execute moves
def move_box(grid, item, move, x, y):
    if move == "^":
        if grid[x - 1][y] == "#":
            return
        elif grid[x - 1][y] == ".":
            grid[x - 1][y] = "O"
            grid[x][y] = "."
        elif grid[x - 1][y] == "O":
            move_box(grid, "O", "^", x - 1, y)
            if grid[x - 1][y] == "." and item == "O":
                grid[x - 1][y] = item
                grid[x][y] = "."
    elif move == ">":
        if grid[x][y + 1] == "#":
            return
        elif grid[x][y + 1] == ".":
            grid[x][y + 1] = "O"
            grid[x][y] = "."
        elif grid[x][y + 1] == "O":
            move_box(grid, "O", ">", x, y + 1)
            if grid[x][y + 1] == "." and item == "O":
                grid[x][y + 1] = item
                grid[x][y] = "."
    elif move == "v":
        if grid[x + 1][y] == "#":
            return
        elif grid[x + 1][y] == ".":
            grid[x + 1][y] = "O"
            grid[x][y] = "."
        elif grid[x + 1][y] == "O":
            move_box(grid, "O", "v", x + 1, y)
            if grid[x + 1][y] == "." and item == "O":
                grid[x + 1][y] = item
                grid[x][y] = "."
    elif move == "<":
        if grid[x][y - 1] == "#":
            return
        elif grid[x][y - 1] == ".":
            grid[x][y - 1] = "O"
            grid[x][y] = "."
        elif grid[x][y - 1] == "O":
            move_box(grid, "O", "<", x, y - 1)
            if grid[x][y - 1] == "." and item == "O":
                grid[x][y - 1] = item
                grid[x][y] = "."


def move_robot(grid, moves, robot_pos):
    x, y = robot_pos
    for move in moves:
        # print("move:", move)
        if move == "^":
            if grid[x - 1][y] == ".":
                grid[x - 1][y] = "@"
                grid[x][y] = "."
                x -= 1
            elif grid[x - 1][y] == "O":
                move_box(grid, "@", "^", x, y)
                if grid[x - 1][y] == ".":
                    grid[x - 1][y] = "@"
                    grid[x][y] = "."
                    x -= 1
        elif move == ">":
            if grid[x][y + 1] == ".":
                grid[x][y + 1] = "@"
                grid[x][y] = "."
                y += 1
            elif grid[x][y + 1] == "O":
                move_box(grid, "@", ">", x, y)
                if grid[x][y + 1] == ".":
                    grid[x][y + 1] = "@"
                    grid[x][y] = "."
                    y += 1
        elif move == "v":
            if grid[x + 1][y] == ".":
                grid[x + 1][y] = "@"
                grid[x][y] = "."
                x += 1
            elif grid[x + 1][y] == "O":
                move_box(grid, "@", "v", x, y)
                if grid[x + 1][y] == ".":
                    grid[x + 1][y] = "@"
                    grid[x][y] = "."
                    x += 1
        elif move == "<":
            if grid[x][y - 1] == ".":
                grid[x][y - 1] = "@"
                grid[x][y] = "."
                y -= 1
            elif grid[x][y - 1] == "O":
                move_box(grid, "@", "<", x, y)
                if grid[x][y - 1] == ".":
                    grid[x][y - 1] = "@"
                    grid[x][y] = "."
                    y -= 1
        # for row in grid:
        #     print(row)
        # print()
        # time.sleep(1)
    return grid


# 4. calculate the boxes GPS coordinates
def sum_gps(grid):
    gps = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "O":
                gps += 100 * i + j
    return gps


robot_pos1 = get_robot_pos(grid1)
move_robot(grid1, moves1, robot_pos1)
for row in grid1:
    print(row)
gps_sum1 = sum_gps(grid1)
print("GPS sum:", gps_sum1)

print()
robot_pos2 = get_robot_pos(grid2)
move_robot(grid2, moves2, robot_pos2)
for row in grid2:
    print(row)
gps_sum2 = sum_gps(grid2)
print("GPS sum:", gps_sum2)

robot_pos = get_robot_pos(grid)
move_robot(grid, moves, robot_pos)
gps_sum = sum_gps(grid)
print("GPS sum:", gps_sum)
