# https://adventofcode.com/2024/day/8

# Part 2
from collections import defaultdict
from itertools import combinations

# 1. load import from file
grid = []
with open("day8_input.txt") as f:
    for line in f:
        grid.append(list(line.strip()))

## example data
# fmt: off
# grid = [
#     [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
#     [".", ".", ".", ".", ".", ".", ".", ".", "0", ".", ".", "."],
#     [".", ".", ".", ".", ".", "0", ".", ".", ".", ".", ".", "."],
#     [".", ".", ".", ".", ".", ".", ".", "0", ".", ".", ".", "."],
#     [".", ".", ".", ".", "0", ".", ".", ".", ".", ".", ".", "."],
#     [".", ".", ".", ".", ".", ".", "A", ".", ".", ".", ".", "."],
#     [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
#     [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
#     [".", ".", ".", ".", ".", ".", ".", ".", "A", ".", ".", "."],
#     [".", ".", ".", ".", ".", ".", ".", ".", ".", "A", ".", "."],
#     [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
#     [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
# ]
# fmt: on

# 2. locate antennas on the map
antennas = defaultdict(list)
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if not grid[i][j] == ".":
            antennas[grid[i][j]].append((i, j))

# 3. note antiondes on the map
antinodes = set()
for key in antennas:
    for ant_a, ant_b in combinations(antennas[key], 2):
        antinodes.add(ant_a)
        antinodes.add(ant_b)
        step = (ant_a[0] - ant_b[0], ant_a[1] - ant_b[1])
        antinode = ant_a
        while (0 <= antinode[0] + step[0] < len(grid)) and (
            0 <= antinode[1] + step[1] < len(grid[0])
        ):
            antinode = (antinode[0] + step[0], antinode[1] + step[1])
            antinodes.add(antinode)

        while (0 <= antinode[0] - step[0] < len(grid)) and (
            0 <= antinode[1] - step[1] < len(grid[0])
        ):
            antinode = (antinode[0] - step[0], antinode[1] - step[1])
            antinodes.add(antinode)


print(antinodes, len(antinodes))

for i, row in enumerate(grid):
    for j, cell in enumerate(row):
        if (i, j) in antinodes:
            print("#", end="")
        else:
            print(cell, end="")
    print()
