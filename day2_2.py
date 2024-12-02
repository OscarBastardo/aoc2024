# https://adventofcode.com/2024/day/2

# Part 1

# 1. import input into list of lists
reports = []
with open("day2_input.txt") as f:
    for line in f:
        report = [int(i) for i in line.split()]
        reports.append(report)

# # example data
# reports = [
#     [7, 6, 4, 2, 1],
#     [1, 2, 7, 8, 9],
#     [9, 7, 6, 2, 1],
#     [1, 3, 2, 4, 5],
#     [8, 6, 4, 4, 1],
#     [1, 3, 6, 7, 9],
# ]

# 2. count number of safe reports
safe_reports = 0
for report in reports:
    if not (report[1] == report[0] or abs(report[1] - report[0]) > 3):
        increasing = report[1] > report[0]
        for i in range(2, len(report)):
            if report[i] == report[i - 1] or abs(report[i] - report[i - 1]) > 3:
                break
            if increasing and report[i] < report[i - 1]:
                break
            if not increasing and report[i] > report[i - 1]:
                break
        else:
            safe_reports += 1
            continue
    # not safe, apply "Problem Dampener"
    for r in range(len(report)):
        report_pd = report[0:r] + report[r + 1 :]
        if report_pd[1] == report_pd[0] or abs(report_pd[1] - report_pd[0]) > 3:
            continue
        increasing_pd = report_pd[1] > report_pd[0]
        for i in range(2, len(report_pd)):
            if (
                report_pd[i] == report_pd[i - 1]
                or abs(report_pd[i] - report_pd[i - 1]) > 3
            ):
                break
            if increasing_pd and report_pd[i] < report_pd[i - 1]:
                break
            if not increasing_pd and report_pd[i] > report_pd[i - 1]:
                break
        else:
            safe_reports += 1
            break
print(safe_reports)
