# https://adventofcode.com/2024/day/11

# Part 1

# 1. import data
stones = []
with open("day11_input.txt") as f:
    stones = [int(n) for n in f.readline().strip().split(" ")]

## example data
# stones = [0, 1, 10, 99, 999]
# stones = [125, 17]

# 2. blink 25 times
blinks = 25
print(stones)
for blink in range(blinks):
    print(f"Blink {blink}")
    i = 0
    new_stones = []
    while i < len(stones):
        if stones[i] == 0:
            stones[i] = 1
        elif len(str(stones[i])) % 2 == 0:
            # new_stones = [
            #     int(str(stones[i])[: len(str(stones[i])) // 2]),
            #     int(str(stones[i])[len(str(stones[i])) // 2 :]),
            # ]
            # stones = stones[:i] + new_stones + stones[i + 1 :]
            # i += 1
            stone = stones[i]
            stones[i] = int(str(stone)[: len(str(stone)) // 2])
            new_stones.append(int(str(stone)[len(str(stone)) // 2 :]))
        else:
            stones[i] = stones[i] * 2024
        i += 1
    stones += new_stones
print(len(stones))
