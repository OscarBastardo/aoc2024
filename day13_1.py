# https://adventofcode.com/2024/day/13

# Part 1
import re
import numpy as np

# 1. import data
machines = []
with open("day13_input.txt") as f:
    # start on line 1 and read 3 lines at a time
    while True:
        # Read button A data
        button_a = f.readline().strip()
        x1, y1 = map(int, re.findall(r"\d+", button_a))
        # Read button B data
        button_b = f.readline().strip()
        x2, y2 = map(int, re.findall(r"\d+", button_b))
        # Read prize data
        prize = f.readline().strip()
        x3, y3 = map(int, re.findall(r"\d+", prize))
        # write to machines
        A = np.array([[x1, x2], [y1, y2]])
        b = np.array([x3, y3])
        machines.append((A, b))
        # Read empty line
        empty_line = f.readline()
        if not empty_line:
            break


# test data
machines = [
    (np.array([[94, 22], [34, 67]]), np.array([8400, 5400])),
    (np.array([[26, 67], [66, 21]]), np.array([12748, 12176])),
    (np.array([[17, 84], [86, 37]]), np.array([7870, 6450])),
    (np.array([[69, 27], [23, 71]]), np.array([18641, 10279])),
]


# for machine in machines:
#     print(machine)

# 2. solve system of equations
solutions = []
for machine in machines:
    A, b = machine
    solutions.append(np.linalg.solve(A, b))

# 3. compute number of tokens needed to solve all solvable machines
tokens = 0
for solution in solutions:
    a, b = solution
    if np.isclose(a, int(round(a))) and np.isclose(b, int(round(b))):
        tokens += 3 * int(round(a)) + 1 * int(round(b))
        print("Y", a, b, int(round(a)), int(round(b)))
    else:
        print("N", a, b, int(round(a)), int(round(b)))
print(tokens)
