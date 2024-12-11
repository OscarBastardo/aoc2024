# https://adventofcode.com/2024/day/11

# Part 2
from functools import cache

# 1. import data
stones = []
with open("day11_input.txt") as f:
    stones = [int(n) for n in f.readline().strip().split(" ")]

## example data
# stones = [0, 1, 10, 99, 999]
# stones = [125, 17]

# 2. blink 25 times
BLINKS = 75


@cache
def count(stone, blink):
    if blink == BLINKS:
        return 1
    elif stone == 0:
        return count(1, blink + 1)
    elif len(str(stone)) % 2 == 0:
        return count(int(str(stone)[: len(str(stone)) // 2]), blink + 1) + count(
            int(str(stone)[len(str(stone)) // 2 :]), blink + 1
        )
    else:
        return count(stone * 2024, blink + 1)


def main():
    stones_count = sum([count(stone, 0) for stone in stones])
    print(stones_count)


main()
