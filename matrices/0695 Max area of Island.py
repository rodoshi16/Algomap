def maxArea(grid):
    """


    You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

    The area of an island is the number of cells with a value 1 in the island.

    Return the maximum area of an island in grid. If there is no island, return 0.



    Example 1:


    Input: grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
    Output: 6
    Explanation: The answer is not 11, because the island must be connected 4-directionally.
    Example 2:

    Input: grid = [[0,0,0,0,0,0,0,0]]
    Output: 0

    Time: 0(n*m) + 0(n*m) ~ 0(n*m)

    Test cases:

    - [0,0,0][0,0,0]
    - [[1]]
    - [[1, 1, 0, 1]]
    - [[1,0][0,1]]
    - [1,1], [1,1]



    """
    #all edges are surrounded by water
    # area, max number of cells with value of 1
    # can't be diagonal

    # edge cases:
    # empty DNE
    # len(1):  [[1]]
    # either o or 1

    #iterate through and check for 1
    # dfs to find connected island
    # global variable to track max count

    row = len(grid)
    col = len(grid[0])
    visited = set()
    max_a = 0

    def dfs(i, j):
        l = 1
        visited.add((i, j))
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for d in directions:
            dr = i + d[0]
            dc = j + d[1]
            if 0<=dr <row and 0<= dc< col and grid[dr][dc] == 1 and (dr, dc) not in visited:
                l += dfs(dr, dc)
        return l

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1 and (i, j) not in visited:
                max_a = max(max_a, dfs(i, j))

    return max_a


