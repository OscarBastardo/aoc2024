# https://adventofcode.com/2024/day/15

# Part 2
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

grid3 = [
    ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
    ["#", "#", ".", ".", ".", ".", ".", ".", "#", "#", ".", ".", "#", "#"],
    ["#", "#", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "#", "#"],
    ["#", "#", ".", ".", ".", ".", "[", "]", "[", "]", "@", ".", "#", "#"],
    ["#", "#", ".", ".", ".", ".", "[", "]", ".", ".", ".", ".", "#", "#"],
    ["#", "#", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "#", "#"],
    ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
]
moves3 = list("<vv<<^^<<^^")

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


# 3. scale grid
def scale_grid(grid):
    grid_scaled = []
    for row in grid:
        row_scaled = []
        for item in row:
            if item == "#":
                row_scaled += ["#", "#"]
            elif item == ".":
                row_scaled += [".", "."]
            elif item == "O":
                row_scaled += ["[", "]"]
            elif item == "@":
                row_scaled += ["@", "."]
        grid_scaled.append(row_scaled)
    return grid_scaled


# 4. execute moves
def can_box_move(grid, move, l_x, l_y, r_x, r_y):
    if move == "^":
        if grid[l_x - 1][l_y] == "#" or grid[r_x - 1][r_y] == "#":
            return False
        if grid[l_x - 1][l_y - 1] == "[" and grid[r_x - 1][r_y - 1] == "]":
            if not can_box_move(grid, "^", l_x - 1, l_y - 1, r_x - 1, r_y - 1):
                return False
        if grid[l_x - 1][l_y] == "[" and grid[r_x - 1][r_y] == "]":
            if not can_box_move(grid, "^", l_x - 1, l_y, r_x - 1, r_y):
                return False
        if grid[l_x - 1][l_y + 1] == "[" and grid[r_x - 1][r_y + 1] == "]":
            if not can_box_move(grid, "^", l_x - 1, l_y + 1, r_x - 1, r_y + 1):
                return False
        return True
    elif move == ">":
        if r_y + 1 < len(grid[0]) and grid[r_x][r_y + 1] == "#":
            return False
        elif r_y + 1 < len(grid[0]) and grid[r_x][r_y + 1] == "[":
            if not can_box_move(grid, ">", r_x, r_y + 1, r_x, r_y + 2):
                return False
        return True
    elif move == "v":
        if grid[l_x + 1][l_y] == "#" or grid[r_x + 1][r_y] == "#":
            return False
        if grid[l_x + 1][l_y - 1] == "[" and grid[r_x + 1][r_y - 1] == "]":
            if not can_box_move(grid, "v", l_x + 1, l_y - 1, r_x + 1, r_y - 1):
                return False
        if grid[l_x + 1][l_y] == "[" and grid[r_x + 1][r_y] == "]":
            if not can_box_move(grid, "v", l_x + 1, l_y, r_x + 1, r_y):
                return False
        if grid[l_x + 1][l_y + 1] == "[" and grid[r_x + 1][r_y + 1] == "]":
            if not can_box_move(grid, "v", l_x + 1, l_y + 1, r_x + 1, r_y + 1):
                return False
        return True
    elif move == "<":
        if l_y - 1 >= 0 and grid[l_x][l_y - 1] == "#":
            return False
        elif l_y - 1 >= 0 and grid[l_x][l_y - 1] == "]":
            if not can_box_move(grid, "<", l_x, l_y - 2, l_x, l_y - 1):
                return False
        return True


def move_box(grid, move, l_x, l_y, r_x, r_y):
    if not can_box_move(grid, move, l_x, l_y, r_x, r_y):
        return
    if move == "^":
        if grid[l_x - 1][l_y] == "#" or grid[r_x - 1][r_y] == "#":
            return
        if grid[l_x - 1][l_y - 1] == "[" and grid[r_x - 1][r_y - 1] == "]":
            move_box(grid, "^", l_x - 1, l_y - 1, r_x - 1, r_y - 1)
        if grid[l_x - 1][l_y] == "[" and grid[r_x - 1][r_y] == "]":
            move_box(grid, "^", l_x - 1, l_y, r_x - 1, r_y)
        if grid[l_x - 1][l_y + 1] == "[" and grid[r_x - 1][r_y + 1] == "]":
            move_box(grid, "^", l_x - 1, l_y + 1, r_x - 1, r_y + 1)
        if grid[l_x - 1][l_y] == "." and grid[r_x - 1][r_y] == ".":
            grid[l_x - 1][l_y] = "["
            grid[r_x - 1][r_y] = "]"
            grid[l_x][l_y] = "."
            grid[r_x][r_y] = "."
    elif move == ">":
        if r_y + 1 < len(grid[0]) and grid[r_x][r_y + 1] == "#":
            return
        elif r_y + 1 < len(grid[0]) and grid[r_x][r_y + 1] == "[":
            move_box(grid, ">", r_x, r_y + 1, r_x, r_y + 2)
        if grid[r_x][r_y + 1] == ".":
            grid[l_x][l_y + 1] = "["
            grid[r_x][r_y + 1] = "]"
            grid[l_x][l_y] = "."
    elif move == "v":
        if grid[l_x + 1][l_y] == "#" or grid[r_x + 1][r_y] == "#":
            return
        if grid[l_x + 1][l_y - 1] == "[" and grid[r_x + 1][r_y - 1] == "]":
            move_box(grid, "v", l_x + 1, l_y - 1, r_x + 1, r_y - 1)
        if grid[l_x + 1][l_y] == "[" and grid[r_x + 1][r_y] == "]":
            move_box(grid, "v", l_x + 1, l_y, r_x + 1, r_y)
        if grid[l_x + 1][l_y + 1] == "[" and grid[r_x + 1][r_y + 1] == "]":
            move_box(grid, "v", l_x + 1, l_y + 1, r_x + 1, r_y + 1)
        if grid[l_x + 1][l_y] == "." and grid[r_x + 1][r_y] == ".":
            grid[l_x + 1][l_y] = "["
            grid[r_x + 1][r_y] = "]"
            grid[l_x][l_y] = "."
            grid[r_x][r_y] = "."
    elif move == "<":
        if l_y - 1 >= 0 and grid[l_x][l_y - 1] == "#":
            return
        elif l_y - 1 >= 0 and grid[l_x][l_y - 1] == "]":
            move_box(grid, "<", l_x, l_y - 2, l_x, l_y - 1)
        if grid[l_x][l_y - 1] == ".":
            grid[l_x][l_y - 1] = "["
            grid[r_x][r_y - 1] = "]"
            grid[r_x][r_y] = "."


def move_robot(grid, moves, robot_pos):
    x, y = robot_pos
    for i, move in enumerate(moves):
        # print("move:", move)
        if move == "^":
            if grid[x - 1][y] == ".":
                grid[x - 1][y] = "@"
                grid[x][y] = "."
                x -= 1
            elif grid[x - 1][y] in ("[", "]"):
                if grid[x - 1][y] == "[":
                    move_box(grid, "^", x - 1, y, x - 1, y + 1)
                elif grid[x - 1][y] == "]":
                    move_box(grid, "^", x - 1, y - 1, x - 1, y)
                if grid[x - 1][y] == ".":
                    grid[x - 1][y] = "@"
                    grid[x][y] = "."
                    x -= 1
        elif move == ">":
            if grid[x][y + 1] == ".":
                grid[x][y + 1] = "@"
                grid[x][y] = "."
                y += 1
            elif grid[x][y + 1] == "[":
                move_box(grid, ">", x, y + 1, x, y + 2)
                if grid[x][y + 1] == ".":
                    grid[x][y + 1] = "@"
                    grid[x][y] = "."
                    y += 1
        elif move == "v":
            if grid[x + 1][y] == ".":
                grid[x + 1][y] = "@"
                grid[x][y] = "."
                x += 1
            elif grid[x + 1][y] in ("[", "]"):
                if grid[x + 1][y] == "[":
                    move_box(grid, "v", x + 1, y, x + 1, y + 1)
                elif grid[x + 1][y] == "]":
                    move_box(grid, "v", x + 1, y - 1, x + 1, y)
                if grid[x + 1][y] == ".":
                    grid[x + 1][y] = "@"
                    grid[x][y] = "."
                    x += 1
        elif move == "<":
            if grid[x][y - 1] == ".":
                grid[x][y - 1] = "@"
                grid[x][y] = "."
                y -= 1
            elif grid[x][y - 1] == "]":
                move_box(grid, "<", x, y - 2, x, y - 1)
                if grid[x][y - 1] == ".":
                    grid[x][y - 1] = "@"
                    grid[x][y] = "."
                    y -= 1
        # print(f"move {i}: {move}")
        # for row in grid:
        #     print("".join(row))
        # print()
        # input()
    return grid


# 5. calculate the boxes GPS coordinates
def sum_gps(grid):
    gps = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "[":
                gps += 100 * i + j
    return gps


# robot_pos1 = get_robot_pos(grid1)
# move_robot(grid1, moves1, robot_pos1)
# for row in grid1:
#     print(row)
# gps_sum1 = sum_gps(grid1)
# print("GPS sum:", gps_sum1)

# grid2 = scale_grid(grid2)
# robot_pos2 = get_robot_pos(grid2)
# move_robot(grid2, moves2, robot_pos2)
# for row in grid2:
#     print("".join(row))
# gps_sum2 = sum_gps(grid2)
# print("GPS sum:", gps_sum2)


grid = scale_grid(grid)
robot_pos = get_robot_pos(grid)
move_robot(grid, moves, robot_pos)
for row in grid:
    print("".join(row))
gps_sum = sum_gps(grid)
print("GPS sum:", gps_sum)

# robot_pos3 = get_robot_pos(grid3)
# for row in grid3:
#     print("".join(row))
# move_robot(grid3, moves3, robot_pos3)
# for row in grid3:
#     print("".join(row))
