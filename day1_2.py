# https://adventofcode.com/2024/day/1

# Part 2

# 1. import input into two lists
left, right = [], []
with open("day1_input.txt") as f:
    for line in f:
        lines = line.split()
        left.append(int(lines[0]))
        right.append(int(lines[1]))

# 2. calculate similarity
similarity = 0
for i in range(len(left)):
    count = 0
    for j in range(len(right)):
        if right[j] == left[i]:
            count += 1
    similarity += left[i] * count

print(similarity)
