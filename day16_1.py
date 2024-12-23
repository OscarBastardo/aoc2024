# https://adventofcode.com/2024/day/16

# Part 1
import math
import sys
import heapq

sys.setrecursionlimit(10000)

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


## 3.a. solve maze recursively
def solve_maze_recursive(maze, x, y, steps, turns, facing, best_cost, visited) -> int:
    """
    Recursive algorithm to solve the maze

    Added optimisations by:
    - not visiting cells that have been visited before in the current path
    - not visiting cells that have a higher cost than the current best cost

    Good enough for (14, 14) maze, but not for (140, 140) maze
    """
    min_cost = best_cost
    visited.add((x, y))
    if maze[x][y] == "E":
        print(f"found exit with {steps} steps and {turns} turns")
        cost = steps + turns * 1000
        visited.remove((x, y))
        return cost
    if (x - 1, y) not in visited and maze[x - 1][y] != "#":
        turns_up = turns if facing == "up" else turns + 1
        if steps + turns_up * 1000 < best_cost:
            cost_up = solve_maze_recursive(
                maze, x - 1, y, steps + 1, turns_up, "up", min_cost, visited
            )
            min_cost = min(min_cost, cost_up)
    if (x, y + 1) not in visited and maze[x][y + 1] != "#":
        turns_right = turns if facing == "right" else turns + 1
        if steps + turns_right * 1000 < best_cost:
            cost_right = solve_maze_recursive(
                maze, x, y + 1, steps + 1, turns_right, "right", min_cost, visited
            )
            min_cost = min(min_cost, cost_right)
    if (x + 1, y) not in visited and maze[x + 1][y] != "#":
        turns_down = turns if facing == "down" else turns + 1
        if steps + turns_down * 1000 < best_cost:
            cost_down = solve_maze_recursive(
                maze, x + 1, y, steps + 1, turns_down, "down", min_cost, visited
            )
            min_cost = min(min_cost, cost_down)
    if (x, y - 1) not in visited and maze[x][y - 1] != "#":
        turns_left = turns if facing == "left" else turns + 1
        if steps + turns_left * 1000 < best_cost:
            cost_left = solve_maze_recursive(
                maze, x, y - 1, steps + 1, turns_left, "left", min_cost, visited
            )
            min_cost = min(min_cost, cost_left)
    visited.remove((x, y))
    return min_cost


## 3.b. solve maze using Dijkstra's algorithm
def solve_maze_dijkstra(maze, start_x, start_y) -> int:
    """
    Dijkstra's algorithm to solve the maze
    """

    dist = [
        [
            {direction: math.inf for direction in ["up", "down", "left", "right"]}
            for _ in range(len(maze[0]))
        ]
        for _ in range(len(maze))
    ]
    dist[start_x][start_y]["right"] = 0
    pq = [(0, start_x, start_y, "right")]

    while pq:
        d, x, y, _dir = heapq.heappop(pq)

        if d > dist[x][y][_dir]:
            continue

        if maze[x][y] == "E":
            return d

        for dir_x, dir_y, new_dir in [
            (-1, 0, "up"),
            (0, 1, "down"),
            (1, 0, "right"),
            (0, -1, "left"),
        ]:
            new_x, new_y = x + dir_x, y + dir_y
            if maze[new_x][new_y] != "#":
                weight = 1 if _dir == new_dir else 1001
                new_dist = d + weight
                if new_dist < dist[new_x][new_y][new_dir]:
                    dist[new_x][new_y][new_dir] = new_dist
                    heapq.heappush(pq, (new_dist, new_x, new_y, new_dir))

    return math.inf


## 4. all together
def main(maze):
    x, y = find_start(maze)
    # best_cost = solve_maze_recursive(maze, x, y, 0, 0, "right", math.inf, set())
    best_cost = solve_maze_dijkstra(maze, x, y)
    print(best_cost)


main(maze1)
main(maze2)
main(maze)
