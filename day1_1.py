# https://adventofcode.com/2024/day/1

# Part 1

# 1. import input into two lists
left, right = [], []
with open("day1_input.txt") as f:
    for line in f:
        lines = line.split()
        left.append(int(lines[0]))
        right.append(int(lines[1]))

# 2. sort the lists
left.sort()
right.sort()

# 3. find distance between pairs
dists = [abs(a - b) for a, b in zip(left, right)]

# 4. find the total distance
total_dist = sum(dists)
print(total_dist)
