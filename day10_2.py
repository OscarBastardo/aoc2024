# https://adventofcode.com/2024/day/10

# Part 2

# 1. import data
grid = []
with open("day10_input.txt") as f:
    for line in f:
        grid.append([int(x) for x in line.strip()])

## example input
# grid = [
#     [8, 9, 0, 1, 0, 1, 2, 3],
#     [7, 8, 1, 2, 1, 8, 7, 4],
#     [8, 7, 4, 3, 0, 9, 6, 5],
#     [9, 6, 5, 4, 9, 8, 7, 4],
#     [4, 5, 6, 7, 8, 9, 0, 3],
#     [3, 2, 0, 1, 9, 0, 1, 2],
#     [0, 1, 3, 2, 9, 8, 0, 1],
#     [1, 0, 4, 5, 6, 7, 3, 2],
# ]

# for row in grid:
#     print(row)

# 2. recursively count number of trails from 0 to 9


def find_trails(grid, i, j, step, nines) -> int:
    if step == 9:  # found 9
        # print(i, j)
        nines.append((i, j))
    if i - 1 >= 0 and grid[i - 1][j] == step + 1:  # move up
        find_trails(grid, i - 1, j, step + 1, nines)
    if j + 1 < len(grid[0]) and grid[i][j + 1] == step + 1:  # move right
        find_trails(grid, i, j + 1, step + 1, nines)
    if i + 1 < len(grid) and grid[i + 1][j] == step + 1:  # move down
        find_trails(grid, i + 1, j, step + 1, nines)
    if j - 1 >= 0 and grid[i][j - 1] == step + 1:  # move left
        find_trails(grid, i, j - 1, step + 1, nines)


def main():
    scores_sum = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 0:
                # print("start: ", i, j)
                nines = []
                find_trails(grid, i, j, 0, nines)
                scores_sum += len(nines)
    print(scores_sum)


main()
