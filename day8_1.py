# https://adventofcode.com/2024/day/8

# Part 1
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
## fmt: on

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
        anode_a = (ant_a[0] + ant_a[0] - ant_b[0], ant_a[1] + ant_a[1] - ant_b[1])
        anode_b = (ant_b[0] + ant_b[0] - ant_a[0], ant_b[1] + ant_b[1] - ant_a[1])
        if 0 <= anode_a[0] < len(grid) and 0 <= anode_a[1] < len(grid[0]):
            antinodes.add(anode_a)
        if 0 <= anode_b[0] < len(grid) and 0 <= anode_b[1] < len(grid[0]):
            antinodes.add(anode_b)
        
        
    
print(antinodes, len(antinodes))
