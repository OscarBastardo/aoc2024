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
        x3 += 10000000000000
        y3 += 10000000000000
        # write to machines
        A = np.array([[x1, x2], [y1, y2]])
        b = np.array([x3, y3])
        machines.append((A, b))
        # Read empty line
        empty_line = f.readline()
        if not empty_line:
            break

# test data
# machines = [
#     (
#         np.array([[94, 22], [34, 67]]),
#         np.array([8400 + 10000000000000, 5400 + 10000000000000]),
#     ),
#     (
#         np.array([[26, 67], [66, 21]]),
#         np.array([12748 + 10000000000000, 12176 + 10000000000000]),
#     ),
#     (
#         np.array([[17, 84], [86, 37]]),
#         np.array([7870 + 10000000000000, 6450 + 10000000000000]),
#     ),
#     (
#         np.array([[69, 27], [23, 71]]),
#         np.array([18641 + 10000000000000, 10279 + 10000000000000]),
#     ),
# ]


# for machine in machines:
#     print(machine)

# 2. solve system of equations and add solutions if values are integers
solutions = []
for machine in machines:
    tol = 1e-2
    A, b = machine
    solution = np.linalg.solve(A, b)
    if np.all(np.abs(solution - np.round(solution)) < tol):
        solutions.append(np.round(solution).astype(int))
    #     print(
    #         "Y", solution[0], solution[1], np.round(solution[0]), np.round(solution[1])
    #     )
    # else:
    #     print(
    #         "N", solution[0], solution[1], np.round(solution[0]), np.round(solution[1])
    #     )

# 3. compute number of tokens needed to solve all solvable machines
tokens = 0
for solution in solutions:
    tokens += 3 * solution[0] + 1 * solution[1]
print(tokens)
