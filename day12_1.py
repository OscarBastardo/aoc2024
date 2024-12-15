# https://adventofcode.com/2024/day/12

# Part 1

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
    ["O", "O", "O", "O", "O"],
    ["O", "X", "O", "X", "O"],
    ["O", "O", "O", "O", "O"],
    ["O", "X", "O", "X", "O"],
    ["O", "O", "O", "O", "O"],
]

garden3 = [
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

# 2. locate garden groups


def propagate(i, j, garden, areas, visited, perimeters):
    if (i, j) in visited:
        return
    visited.add((i, j))
    areas[-1] += 1
    if i + 1 < len(garden) and garden[i][j] == garden[i + 1][j]:
        propagate(i + 1, j, garden, areas, visited, perimeters)
    else:
        perimeters[-1] += 1

    if j + 1 < len(garden[0]) and garden[i][j] == garden[i][j + 1]:
        propagate(i, j + 1, garden, areas, visited, perimeters)
    else:
        perimeters[-1] += 1

    if i - 1 >= 0 and garden[i][j] == garden[i - 1][j]:
        propagate(i - 1, j, garden, areas, visited, perimeters)
    else:
        perimeters[-1] += 1

    if j - 1 >= 0 and garden[i][j] == garden[i][j - 1]:
        propagate(i, j - 1, garden, areas, visited, perimeters)
    else:
        perimeters[-1] += 1


def main(garden, verbose=False):
    areas = []
    perimeters = []
    visited = set()
    for i in range(len(garden)):
        for j in range(len(garden)):
            if (i, j) not in visited:
                areas.append(0)
                perimeters.append(0)
                propagate(i, j, garden, areas, visited, perimeters)
    cost = sum([area * perimeter for area, perimeter in zip(areas, perimeters)])
    if verbose:
        print([area for area in areas])
        print([perimeter for perimeter in perimeters])
        print(cost)
    return cost


# test cases
assert main(garden1) == 140
assert main(garden2) == 772
assert main(garden3) == 1930

# result
print(main(garden))
