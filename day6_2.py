# https://adventofcode.com/2024/day/6

# Part 2
import time
import copy


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
            start_pos = (i, j)
            start_dir = grid[i][j]

# 2. move and track the visited positions


def traverse(grid, max_iters=10000):
    pos = set()
    guard_pos = start_pos
    iters = 0
    while True:
        if iters > max_iters:  # stuck in a loop
            return pos, True
        # time.sleep(0.01)
        # print_grid(grid)
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
        # if guard_pos == start_pos and grid[guard_pos[0]][guard_pos[1]] == start_dir:
        #     return pos, True
        iters += 1
    return pos, False


def stuck_in_loop(grid):
    _, stuck = traverse(grid)
    return stuck


grid_ = copy.deepcopy(grid)
pos, _ = traverse(grid_)
print(len(pos))

# 3. check blocks on the visited positions (minus starting one)
obs = set()
for p in pos - {start_pos}:
    grid_ = copy.deepcopy(grid)
    grid_[p[0]][p[1]] = "#"
    if stuck_in_loop(grid_):
        obs.add(p)


# 4. return count of possible obstacles
print(len(obs))
