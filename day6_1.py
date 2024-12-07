# https://adventofcode.com/2024/day/6

# Part 1
import time


def print_grid(grid):
    out = ""
    for row in grid:
        out += "".join(row) + "\n"
    print(out, end="\n", flush=True)


# 1. import data
grid = []
with open("day6_input.txt") as f:
    for line in f:
        grid.append(list(line.strip()))


# # example data
# grid = [
#     [".", ".", ".", ".", "#", ".", ".", ".", ".", "."],
#     [".", ".", ".", ".", ".", ".", ".", ".", ".", "#"],
#     [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
#     [".", ".", "#", ".", ".", ".", ".", ".", ".", "."],
#     [".", ".", ".", ".", ".", ".", ".", "#", ".", "."],
#     [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
#     [".", "#", ".", ".", "^", ".", ".", ".", ".", "."],
#     [".", ".", ".", ".", ".", ".", ".", ".", "#", "."],
#     ["#", ".", ".", ".", ".", ".", ".", ".", ".", "."],
#     [".", ".", ".", ".", ".", ".", "#", ".", ".", "."],
# ]

# 2. locate guard
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] in ("^", ">", "v", "<"):
            guard_pos = (i, j)
# print(guard_pos)

# 2. move and track the visited positions
pos = set()
out = False
# print_grid(grid)
while True:
    pos.add(guard_pos)
    if grid[guard_pos[0]][guard_pos[1]] == "^":
        if guard_pos[0] - 1 < 0:
            break
        elif grid[guard_pos[0] - 1][guard_pos[1]] == "#":
            grid[guard_pos[0]][guard_pos[1]] = ">"
        else:
            grid[guard_pos[0]][guard_pos[1]] = "."
            guard_pos = (guard_pos[0] - 1, guard_pos[1])
            grid[guard_pos[0]][guard_pos[1]] = "^"
    elif grid[guard_pos[0]][guard_pos[1]] == ">":
        if guard_pos[1] + 1 >= len(grid[0]):
            break
        elif grid[guard_pos[0]][guard_pos[1] + 1] == "#":
            grid[guard_pos[0]][guard_pos[1]] = "v"
        else:
            grid[guard_pos[0]][guard_pos[1]] = "."
            guard_pos = (guard_pos[0], guard_pos[1] + 1)
            grid[guard_pos[0]][guard_pos[1]] = ">"
    elif grid[guard_pos[0]][guard_pos[1]] == "v":
        if guard_pos[0] + 1 >= len(grid):
            break
        elif grid[guard_pos[0] + 1][guard_pos[1]] == "#":
            grid[guard_pos[0]][guard_pos[1]] = "<"
        else:
            grid[guard_pos[0]][guard_pos[1]] = "."
            guard_pos = (guard_pos[0] + 1, guard_pos[1])
            grid[guard_pos[0]][guard_pos[1]] = "v"
    elif grid[guard_pos[0]][guard_pos[1]] == "<":
        if guard_pos[1] < 0:
            break
        elif grid[guard_pos[0]][guard_pos[1] - 1] == "#":
            grid[guard_pos[0]][guard_pos[1]] = "^"
        else:
            grid[guard_pos[0]][guard_pos[1]] = "."
            guard_pos = (guard_pos[0], guard_pos[1] - 1)
            grid[guard_pos[0]][guard_pos[1]] = "<"

    # time.sleep(0.05)
    # print_grid(grid)

# 3. return count of visited positions
print(len(pos))
