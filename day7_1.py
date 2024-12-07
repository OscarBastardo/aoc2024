# https://adventofcode.com/2024/day/7

# Part 1
from itertools import product

## 1. import input from file
equations = []  # [(value, (number, number, ...)), (value, ...), ...]
with open("day7_input.txt") as f:
    for line in f:
        value = int(line.strip().split(": ")[0])
        numbers = list(int(n) for n in line.strip().split(": ")[1].split(" "))
        equations.append((value, numbers))

## example data
# equations = [
#     (190, [10, 19]),
#     (3267, [81, 40, 27]),
#     (83, [17, 5]),
#     (156, [15, 6]),
#     (7290, [6, 8, 6, 15]),
#     (161011, [16, 10, 13]),
#     (192, [17, 8, 14]),
#     (21037, [9, 7, 18, 13]),
#     (292, [11, 6, 16, 20]),
# ]

# 2. evaluate equations left to right and sum those whose value match the operations
value_sum = 0
for equation in equations:
    value, numbers = equation
    for ops in list(product(["+", "*"], repeat=len(numbers) - 1)):
        res = numbers[0]
        for i in range(len(ops)):
            if ops[i] == "+":
                res += numbers[i + 1]
            elif ops[i] == "*":
                res *= numbers[i + 1]
        if res == value:
            value_sum += value
            break
print(value_sum)
