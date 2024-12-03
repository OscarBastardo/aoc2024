# https://adventofcode.com/2024/day/3

# Part 2

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

# 3. extract the mul(x,y) operations between 'don't() and do()'
dont_muls = []
for dont_mul in re.finditer(r"(?<=don\'t\(\)).*?(?=do\(\))", memory):
    for mul in re.finditer(r"mul\((\d+),(\d+)\)", dont_mul.group()):
        dont_muls.append((int(mul.group(1)), int(mul.group(2))))

# 4. multiply and sum
dont_results = sum(x * y for (x, y) in dont_muls)

# 5. subtract
result -= dont_results
print(result)
