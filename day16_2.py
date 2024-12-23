# https://adventofcode.com/2024/day/16

# Part 1
import math
import heapq
from collections import defaultdict


# 1. import data
maze = []
with open("day16_input.txt") as f:
    for line in f:
        maze.append(line.strip())

# print(len(maze), len(maze[0]))

## example data
maze1 = [
    "###############",
    "#.......#....E#",
    "#.#.###.#.###.#",
    "#.....#.#...#.#",
    "#.###.#####.#.#",
    "#.#.#.......#.#",
    "#.#.#####.###.#",
    "#...........#.#",
    "###.#.#####.#.#",
    "#...#.....#.#.#",
    "#.#.#.###.#.#.#",
    "#.....#...#.#.#",
    "#.###.#.#.#.#.#",
    "#S..#.....#...#",
    "###############",
]

maze2 = [
    "#################",
    "#...#...#...#..E#",
    "#.#.#.#.#.#.#.#.#",
    "#.#.#.#...#...#.#",
    "#.#.#.#.###.#.#.#",
    "#...#.#.#.....#.#",
    "#.#.#.#.#.#####.#",
    "#.#...#.#.#.....#",
    "#.#.#####.#.###.#",
    "#.#.#.......#...#",
    "#.#.###.#####.###",
    "#.#.#...#.....#.#",
    "#.#.#.#####.###.#",
    "#.#.#.........#.#",
    "#.#.#.#########.#",
    "#S#.............#",
    "#################",
]


## 2.a. find start position
def find_start(maze):
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == "S":
                return i, j


## 2.b. find end position
def find_end(maze):
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == "E":
                return i, j


def solve_maze_dijkstra(maze, start_x, start_y):
    """
    Modified Dijkstra's algorithm to find best paths and count unique paths in them
    Returns: (best_cost, set of coordinates that belong to optimal paths)
    """
    # Distance to reach each cell coming from each direction
    dist = [
        [
            {direction: math.inf for direction in ["up", "down", "left", "right"]}
            for _ in range(len(maze[0]))
        ]
        for _ in range(len(maze))
    ]

    # For each cell and direction, store the previous tiles in best paths
    prev = defaultdict(set)  # (x, y, direction) -> set of (prev_x, prev_y, prev_dir)

    dist[start_x][start_y]["right"] = 0
    pq = [(0, start_x, start_y, "right")]

    end_x, end_y = None, None  # Will store coordinates of 'E'
    best_cost = math.inf

    while pq:
        d, x, y, _dir = heapq.heappop(pq)

        if d > dist[x][y][_dir]:
            continue

        if maze[x][y] == "E":
            end_x, end_y = x, y
            best_cost = min(best_cost, d)
            continue

        for dir_x, dir_y, new_dir in [
            (-1, 0, "up"),
            (0, 1, "right"),
            (1, 0, "down"),
            (0, -1, "left"),
        ]:
            new_x, new_y = x + dir_x, y + dir_y
            if maze[new_x][new_y] != "#":
                weight = 1 if _dir == new_dir else 1001
                new_dist = d + weight

                # If we found an equal-cost path
                if new_dist == dist[new_x][new_y][new_dir]:
                    prev[(new_x, new_y, new_dir)].add((x, y, _dir))

                # If we found a better path
                elif new_dist < dist[new_x][new_y][new_dir]:
                    dist[new_x][new_y][new_dir] = new_dist
                    prev[(new_x, new_y, new_dir)] = {(x, y, _dir)}
                    heapq.heappush(pq, (new_dist, new_x, new_y, new_dir))

    # If we didn't find the end, return infinity and empty set
    if end_x is None:
        return math.inf, set()

    # Backtrack from end to start to find all cells in best paths
    best_path_tiles = set()

    def backtrack(x, y, direction, visited):
        if (x, y) == (start_x, start_y):
            return

        current_key = (x, y, direction)
        if current_key not in prev:
            return

        for prev_x, prev_y, prev_dir in prev[current_key]:
            best_path_tiles.add((prev_x, prev_y))
            if (prev_x, prev_y, prev_dir) not in visited:
                visited.add((prev_x, prev_y, prev_dir))
                backtrack(prev_x, prev_y, prev_dir, visited)

    # Start backtracking from each direction that reaches the end with optimal cost
    for direction in ["up", "down", "left", "right"]:
        if dist[end_x][end_y][direction] == best_cost:
            best_path_tiles.add((end_x, end_y))  # Add end cell
            backtrack(end_x, end_y, direction, set())

    best_path_tiles.add((start_x, start_y))  # Add start cell

    return best_cost, len(best_path_tiles)


## 4. all together
def main(maze):
    x, y = find_start(maze)
    best_cost, tiles_count = solve_maze_dijkstra(maze, x, y)
    print(f"Best cost: {best_cost}")
    print(f"Number of cells in optimal path(s): {tiles_count}")


main(maze1)
main(maze2)
main(maze)
