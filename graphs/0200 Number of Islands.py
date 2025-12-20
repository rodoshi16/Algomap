def number_of_islands(grid: list[list[str]]) -> int:
    """

    Given an m x n 2D binary grid which represents a map of '1's (land) and '0's (water), return the number of islands.

    An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.


    Example 1:

    >>> number_of_islands(grid = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]])
    1
    >>> number_of_islands(grid = [["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]])
    3

    """
    if not grid:
        return 0


    row = len(grid)
    col = len(grid[0])
    islands = 0
    visited = []

    def bfs(i, j):
        start = (i,j)
        q = []

        visited.append(start)
        q.append(start)

        while q:
            r, c = q.pop(0)
            directions = [[0,1],[0,-1],[1,0], [-1,0]]

            for d in directions:
                a = r + d[0]
                b = c + d[1]
                if ((a in range(row)) and (b in range(col)) and grid[a][b]
                        == '1' and ((a,b) not in visited)):
                    q.append((a,b))
                    visited.append((a, b))

    for i in range(row):
        for j in range(col):
            if grid[i][j] == "1" and (i,j) not in visited:
                bfs(i, j)
                islands += 1
    return islands





