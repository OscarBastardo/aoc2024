# https://adventofcode.com/2024/day/4

# Part 2

# 1. import input into a matrix
grid = []
with open("day4_input.txt") as f:
    grid = [[c for c in line.strip()] for line in f]

# # example data
# fmt: off
# grid = [
#     ["M","M","M","S","X","X","M","A","S","M"],
#     ["M","S","A","M","X","M","S","M","S","A"],
#     ["A","M","X","S","X","M","A","A","M","M"],
#     ["M","S","A","M","A","S","M","S","M","X"],
#     ["X","M","A","S","A","M","X","A","M","M"],
#     ["X","X","A","M","M","X","X","A","M","A"],
#     ["S","M","S","M","S","A","S","X","S","S"],
#     ["S","A","X","A","M","A","S","A","A","A"],
#     ["M","A","M","M","M","X","M","M","M","M"],
#     ["M","X","M","X","A","X","M","A","S","X"],
# ]
# fmt: on

# 2. define target X word
word = "MAS"


# 3. check neighbouring characters for a match
def check_x(i, j, grid=grid, word=word) -> int:
    # return 0 if not the middle word (e.g. "A" for "MAS")
    if grid[i][j] != word[1]:
        return 0

    # return 0 if diagonals are out of bounds
    if i + 1 >= len(grid) or i - 1 < 0 or j + 1 >= len(grid[0]) or j - 1 < 0:
        return 0

    count = 0

    # check diagonals
    if (  # top left to bottom right / bottom right to top left
        (grid[i - 1][j - 1] == word[0] and grid[i + 1][j + 1] == word[2])
        or (grid[i + 1][j + 1] == word[0] and grid[i - 1][j - 1] == word[2])
    ) and (  # bottom left to top right / top right to bottom left
        (grid[i + 1][j - 1] == word[0] and grid[i - 1][j + 1] == word[2])
        or (grid[i - 1][j + 1] == word[0] and grid[i + 1][j - 1] == word[2])
    ):
        count += 1

    return count


# 4. count the crosses across grid
def count_xs(grid=grid, word=word) -> int:
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            count += check_x(i, j)
    return count


print(count_xs(grid, word))
