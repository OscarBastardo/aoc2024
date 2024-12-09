# https://adventofcode.com/2024/day/9

# Part 1

# 1. import data
disk_map = []
with open("day9_input.txt") as f:
    disk_map = list([int(i) for i in f.readline().strip()])


## example data
# disk_map = [2, 3, 3, 3, 1, 3, 3, 1, 2, 1, 4, 1, 4, 1, 3, 1, 4, 0, 2]

## 2. convert disk map to file blocks
file_blocks = []
for i, j in enumerate(range(0, len(disk_map), 2)):
    if j == len(disk_map) - 1:
        file_blocks += [i] * disk_map[j]
    else:
        file_blocks += [i] * disk_map[j] + [None] * disk_map[j + 1]
# print(file_blocks)

## 3. move file blocks from the end to the empty blocks one by one
pointer = 0
back_pointer = len(file_blocks) - 1
while pointer < back_pointer:
    if file_blocks[pointer] == None:
        file_blocks[pointer] = file_blocks[back_pointer]
        file_blocks[back_pointer] = None
        while file_blocks[back_pointer] == None:
            back_pointer -= 1
    pointer += 1
    # print(file_blocks)


## 4. compute checksum
i = 0
checksum = 0
while file_blocks[i] != None:
    checksum += file_blocks[i] * i
    i += 1
print(checksum)
