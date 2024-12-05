# https://adventofcode.com/2024/day/5

# Part 1

# 1. import data
ordering = []
updates = []

with open("day5_input.txt") as f:
    is_ordering = True
    for line in f:
        if line == "\n":
            is_ordering = False
            continue
        if is_ordering:
            a, b = [int(n) for n in line.strip().split("|")]
            ordering.append((a, b))
        else:
            update = [int(n) for n in line.strip().split(",")]
            updates.append(tuple(update))

# # example data
# ordering = [
#     (47, 53),
#     (97, 13),
#     (97, 61),
#     (97, 47),
#     (75, 29),
#     (61, 13),
#     (75, 53),
#     (29, 13),
#     (97, 29),
#     (53, 29),
#     (61, 53),
#     (97, 53),
#     (61, 29),
#     (47, 13),
#     (75, 47),
#     (97, 75),
#     (47, 61),
#     (75, 61),
#     (47, 29),
#     (75, 13),
#     (53, 13),
# ]

# updates = [
#     (75, 47, 61, 53, 29),
#     (97, 61, 53, 29, 13),
#     (75, 29, 13),
#     (75, 97, 47, 61, 53),
#     (61, 13, 29),
#     (97, 13, 75, 29, 47),
# ]

# 2. check ordering and add the middle number if update is correct
result = 0
for update in updates:
    correct = True
    for i in range(len(update)):
        after = update[i + 1 :]
        pairs = []
        for n in after:
            pairs.append((update[i], n))
        for pair in pairs:
            if pair not in ordering:
                correct = False
    if correct:
        result += update[len(update) // 2]
print(result)
