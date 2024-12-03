# https://adventofcode.com/2024/day/3

# Part 1

# 1. import input into a string
memory = ""
with open("day3_input.txt") as f:
    for line in f:
        memory += line.rstrip()

# 2. extract the mul(x,y) operations from the string
import re

muls = []
for mul in re.finditer(r"mul\((\d+),(\d+)\)", memory):
    muls.append((int(mul.group(1)), int(mul.group(2))))

# 3. multiply and sum
result = sum(x * y for (x, y) in muls)
print(result)
