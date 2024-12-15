# https://adventofcode.com/2024/day/12

# Part 1
from math import floor

# 1. import data
garden = []
with open("day12_input.txt") as f:
    for line in f:
        garden.append(list(line.strip()))

## sample data
garden1 = [
    ["A", "A", "A", "A"],
    ["B", "B", "C", "D"],
    ["B", "B", "C", "C"],
    ["E", "E", "E", "C"],
]

garden2 = [
    ["E", "E", "E", "E", "E"],
    ["E", "X", "X", "X", "X"],
    ["E", "E", "E", "E", "E"],
    ["E", "X", "X", "X", "X"],
    ["E", "E", "E", "E", "E"],
]

garden3 = [
    ["A", "A", "A", "A", "A", "A"],
    ["A", "A", "A", "B", "B", "A"],
    ["A", "A", "A", "B", "B", "A"],
    ["A", "B", "B", "A", "A", "A"],
    ["A", "B", "B", "A", "A", "A"],
    ["A", "A", "A", "A", "A", "A"],
]

garden4 = [
    ["R", "R", "R", "R", "I", "I", "C", "C", "F", "F"],
    ["R", "R", "R", "R", "I", "I", "C", "C", "C", "F"],
    ["V", "V", "R", "R", "R", "C", "C", "F", "F", "F"],
    ["V", "V", "R", "C", "C", "C", "J", "F", "F", "F"],
    ["V", "V", "V", "V", "C", "J", "J", "C", "F", "E"],
    ["V", "V", "I", "V", "C", "C", "J", "J", "E", "E"],
    ["V", "V", "I", "I", "I", "C", "J", "J", "E", "E"],
    ["M", "I", "I", "I", "I", "I", "J", "J", "E", "E"],
    ["M", "I", "I", "I", "S", "I", "J", "E", "E", "E"],
    ["M", "M", "M", "I", "S", "S", "J", "E", "E", "E"],
]


def expand(garden):
    garden_expanded = []
    for i in range(len(garden) * 2):
        k = floor(i / 2)
        garden_expanded.append([])
        for j in range(len(garden) * 2):
            l = floor(j / 2)
            garden_expanded[i].append(garden[k][l])
    return garden_expanded


# fmt: off
def is_corner(garden, i, j):
    is_top_left_out = (
        (i - 1 < 0 or garden[i][j] != garden[i - 1][j])
        and (j - 1 < 0 or garden[i][j] != garden[i][j - 1])
    )
    is_top_right_out = (
        (i - 1 < 0 or garden[i][j] != garden[i - 1][j])
        and (j + 1 >= len(garden[0]) or garden[i][j] != garden[i][j + 1])
    )
    is_bottom_left_out = (
        (i + 1 >= len(garden) or garden[i][j] != garden[i + 1][j])
        and (j - 1 < 0 or garden[i][j] != garden[i][j - 1])
    )
    is_bottom_right_out = (
        (i + 1 >= len(garden) or garden[i][j] != garden[i + 1][j])
        and (j + 1 >= len(garden[0]) or garden[i][j] != garden[i][j + 1])
    )
    is_top_left_in = (
        (i - 1 >= 0 and garden[i][j] == garden[i - 1][j])
        and (j - 1 >= 0 and garden[i][j] == garden[i][j - 1])
        and (garden[i][j] != garden[i - 1][j - 1])
    )
    is_top_right_in = (
        (i - 1 >= 0 and garden[i][j] == garden[i - 1][j])
        and (j + 1 < len(garden[0]) and garden[i][j] == garden[i][j + 1])
        and (garden[i][j] != garden[i - 1][j + 1])
    )
    is_bottom_left_in = (
        (i + 1 < len(garden) and garden[i][j] == garden[i + 1][j])
        and (j - 1 >= 0 and garden[i][j] == garden[i][j - 1])
        and (garden[i][j] != garden[i + 1][j - 1])
    )
    is_bottom_right_in = (
        (i + 1 < len(garden) and garden[i][j] == garden[i + 1][j])
        and (j + 1 < len(garden[0]) and garden[i][j] == garden[i][j + 1])
        and (garden[i][j] != garden[i + 1][j + 1])
    )
    return (
        is_top_left_out
        or is_top_right_out
        or is_bottom_left_out
        or is_bottom_right_out
        or is_top_left_in
        or is_top_right_in
        or is_bottom_left_in
        or is_bottom_right_in
    )
# fmt: on


def propagate(garden, i, j, visited, areas, sides):
    if (i, j) not in visited:
        areas[-1] += 0.25
    visited.add((i, j))
    if is_corner(garden, i, j):
        sides[-1] += 1
    if i + 1 < len(garden) and garden[i][j] == garden[i + 1][j]:
        if (i + 1, j) not in visited:
            propagate(garden, i + 1, j, visited, areas, sides)

    if j + 1 < len(garden[0]) and garden[i][j] == garden[i][j + 1]:
        if (i, j + 1) not in visited:
            propagate(garden, i, j + 1, visited, areas, sides)

    if i - 1 >= 0 and garden[i][j] == garden[i - 1][j]:
        if (i - 1, j) not in visited:
            propagate(garden, i - 1, j, visited, areas, sides)

    if j - 1 >= 0 and garden[i][j] == garden[i][j - 1]:
        if (i, j - 1) not in visited:
            propagate(garden, i, j - 1, visited, areas, sides)


def main(garden):
    garden = expand(garden)
    visited = set()
    areas = []
    sides = []
    for i in range(len(garden)):
        for j in range(len(garden)):
            if (i, j) not in visited:
                areas.append(0)
                sides.append(0)
                propagate(garden, i, j, visited, areas, sides)
    print([area for area in areas])
    print([side for side in sides])

    cost = sum([int(area * side) for area, side in zip(areas, sides)])
    return cost


# test cases
assert main([["C", "D", "D"], ["C", "C", "D"], ["E", "C", "D"]]) == 60
assert main(garden1) == 80
assert main(garden2) == 236
assert main(garden3) == 368
assert main(garden4) == 1206

# result
print(main(garden))
