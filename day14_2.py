# https://adventofcode.com/2024/day/14

# Part 2
import re
import time

# 1. import data

robots = []
MAX_Y, MAX_X = 101, 103
with open("day14_input.txt") as f:
    while True:
        line = f.readline().strip()
        if not line:
            break
        y, x, vy, vx = map(int, re.findall(r"-?\d+", line))
        robots.append([y, x, vy, vx])

# for robot in robots:
#     print(robot)

# example data
# MAX_Y, MAX_X = 11, 7
# robots = [
#     [0, 4, 3, -3],
#     [6, 3, -1, -3],
#     [10, 3, -1, 2],
#     [2, 0, 2, -1],
#     [0, 0, 1, 3],
#     [3, 0, -2, -2],
#     [7, 6, -1, -3],
#     [3, 0, -1, -2],
#     [9, 3, 2, 3],
#     [7, 3, -1, 2],
#     [2, 4, 2, -3],
#     [9, 5, -3, -3],
# ]


# 2. simulate 100 seconds
def simulate(robots, seconds=1):
    for k in range(len(robots)):
        y, x, vy, vx = robots[k]
        robots[k][0] = (y + vy * seconds) % MAX_Y
        robots[k][1] = (x + vx * seconds) % MAX_X
    return robots


# robots = simulate(robots)


# 3. create grid
def create_grid(robots):
    grid = [[0 for _ in range(MAX_Y)] for _ in range(MAX_X)]
    for robot in robots:
        y, x, _, _ = robot
        grid[x][y] += 1

    # for row in grid:
    #     print(row)
    return grid


# grid = create_grid(robots)


# # 4. count robots in quadrants and compute safety factor
# def safety_factor(grid):
#     quad_1 = quad_2 = quad_3 = quad_4 = 0
#     for i in range(len(grid)):
#         for j in range(len(grid[0])):
#             if i < len(grid) // 2 and j < len(grid[0]) // 2:
#                 quad_1 += grid[i][j]
#             elif i < len(grid) // 2 and j > len(grid[0]) // 2:
#                 quad_2 += grid[i][j]
#             elif i > len(grid) // 2 and j < len(grid[0]) // 2:
#                 quad_3 += grid[i][j]
#             elif i > len(grid) // 2 and j > len(grid[0]) // 2:
#                 quad_4 += grid[i][j]
#     # print(quad_1, quad_2, quad_3, quad_4)
#     safety_factor = quad_1 * quad_2 * quad_3 * quad_4
#     return safety_factor

# print(safety_factor(grid))


# 4. print grid to display christmas tree
def print_grid(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            char = " " if grid[i][j] == 0 else "█"
            if j == len(grid[0]) - 1:
                print(char)
            else:
                print(char, end="", flush=True)


seconds = 0
grid = create_grid(robots)
# print(f"seconds: {seconds}")
# print_grid(grid)
while seconds < 10000:
    seconds += 1
    robots = simulate(robots)
    grid = create_grid(robots)
    if seconds == 7344:
        print(f"seconds: {seconds}")
        print_grid(grid)
    # time.sleep(0.1)
