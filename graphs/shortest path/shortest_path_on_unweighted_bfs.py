from typing import List
import math


def shortestCellPath(grid: List[List[int]], sr: int, sc: int, tr: int, tc: int) -> int:
    """
    In a given grid of 0s and 1s, we have some starting row and column sr, sc and a target row and column tr, tc. Return the length of the shortest path from sr, sc to tr, tc that walks along 1 values only.

    Each location in the path, including the start and the end, must be a 1. Each subsequent location in the path must be 4-directionally adjacent to the previous location.

    It is guaranteed that grid[sr][sc] = grid[tr][tc] = 1, and the starting and target positions are different.

    If the task is impossible, return -1.

    Examples:

    input:
    grid = [[1, 1, 1, 1], [0, 0, 0, 1], [1, 1, 1, 1]]
    sr = 0, sc = 0, tr = 2, tc = 0
    output: 8
    (The lines below represent this grid:)
    1111
    0001
    1111

    grid = [[1, 1, 1, 1], [0, 0, 0, 1], [1, 0, 1, 1]]
    sr = 0, sc = 0, tr = 2, tc = 0
    output: -1
    (The lines below represent this grid:)
    1111
    0001
    1011
    Constraints:

    [time limit] 5000ms
    [input] array.array.integer grid
    1 ≤ arr.length = arr[i].length ≤ 10
    [input] integer sr
    [input] integer sc
    [input] integer tr
    [input] integer tc
    All sr, sc, tr, tc are valid locations in the grid, grid[sr][sc] = grid[tr][tc] = 1, and (sr, sc) != (tr, tc).
    [output] integer
    """

    n = len(grid)
    m = len(grid[0])
    visited = set((sr, sc))

    q = [(sr, sc)]
    c = 0

    while q:
        l = len(q)

        for _ in range(l):
            t = q.pop(0)

            dir = [[1, 0], [0, 1], [0, -1], [-1, 0]]
            for d in dir:
                a = t[0] + d[0]
                b = t[1] + d[1]

                if 0 <= a < n and 0 <= b < m and (a, b) not in visited and grid[a][b] == 1:
                    q.append((a, b))
                    visited.add((a, b))
                    if a == tr and b == tc:
                        return c + 1

        c += 1

    return -1




grid = [[1, 1, 1, 1], [0, 0, 0, 1], [1, 1, 1, 1]]
sr, sc, tr, tc = 0, 0, 2, 0
print(shortestCellPath(grid, sr, sc, tr, tc))

