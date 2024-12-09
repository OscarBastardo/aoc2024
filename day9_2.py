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
for pointer, j in enumerate(range(0, len(disk_map), 2)):
    if j == len(disk_map) - 1:
        file_blocks += [pointer] * disk_map[j]
    else:
        file_blocks += [pointer] * disk_map[j] + [None] * disk_map[j + 1]
# print(file_blocks)
# 00...111...2...333.44.5555.6666.777.888899

## 3. move file blocks from the end to the empty blocks in groups

# check free spaces
free_spaces = []
free_space_start = 0
free_space_end = 0
for pointer in range(1, len(file_blocks)):
    if file_blocks[pointer] == None and file_blocks[pointer - 1] != None:
        free_space_start = pointer
    elif file_blocks[pointer] != None and file_blocks[pointer - 1] == None:
        free_space_end = pointer
        free_spaces.append((free_space_start, free_space_end))
# print(file_blocks, free_spaces)

# fill out free spaces
back_pointer = len(file_blocks) - 1
file_end = back_pointer
file_start = back_pointer
file_id = file_blocks[-1]
while file_id > 0:
    while file_blocks[back_pointer] != file_id:
        back_pointer -= 1
    file_end = back_pointer + 1
    while file_blocks[back_pointer] == file_id:
        back_pointer -= 1
    file_start = back_pointer + 1
    # print(file_end, file_start)
    for i, (free_space_start, free_space_end) in enumerate(free_spaces):
        # print(free_space_start, free_space_end)
        if free_space_end > file_start:
            break
        if free_space_end - free_space_start >= file_end - file_start:
            for j in range(file_end - file_start):
                file_blocks[free_space_start + j] = file_id
                file_blocks[file_start + j] = None
            free_spaces[i] = (free_space_start + j + 1, free_space_end)
            break
    file_id -= 1

# print(file_blocks)


# pointer = 0
# free_space_start = pointer
# free_space_end = pointer
# back_pointer = len(file_blocks) - 1
# file_end = back_pointer
# file_start = back_pointer
# file_id = file_blocks[-1]
# while file_id > 0:
#     pointer = 0
#     while file_blocks[pointer] != None:
#         pointer += 1
#     free_space_start = pointer
#     while file_blocks[pointer] == None:
#         pointer += 1
#     free_space_end = pointer
#     while file_blocks[back_pointer] != file_id:
#         back_pointer -= 1
#     file_end = back_pointer + 1
#     while file_blocks[back_pointer] == file_id:
#         back_pointer -= 1
#     file_start = back_pointer + 1
#     if free_space_end - free_space_start >= file_end - file_start:
#         for i in range(file_end - file_start):
#             file_blocks[free_space_start + i] = file_id
#             file_blocks[file_start + i] = None
#     file_id -= 1
#     print(file_blocks)

## 4. compute checksum
checksum = 0
for i in range(len(file_blocks)):
    if file_blocks[i] != None:
        checksum += file_blocks[i] * i
print(checksum)
