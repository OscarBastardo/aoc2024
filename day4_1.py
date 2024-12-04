# https://adventofcode.com/2024/day/4

# Part 1

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

# 2. define target word
word = "XMAS"


# 3. check neighbouring characters for a match
def check_chars(i, j, grid=grid, word=word) -> int:
    if grid[i][j] != word[0]:
        return 0  # first character does not match

    count = 0

    dirs = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
    for dir_x, dir_y in dirs:  # check the 8 directions
        x, y = i + dir_x, j + dir_y

        for k in range(1, len(word)):  # check second to nth character
            # break if out of bounds
            if x >= len(grid) or x < 0 or y >= len(grid[0]) or y < 0:
                break

            # break if not char match
            if grid[x][y] != word[k]:
                break

            # continue in same direction
            x += dir_x
            y += dir_y
        else:
            if k == len(word) - 1:  # only true if for loop is complete without break
                count += 1
    return count


# 4. count the word across the grid
def count_words(grid=grid, word=word) -> int:
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            count += check_chars(i, j)
    return count


print(count_words(grid, word))
