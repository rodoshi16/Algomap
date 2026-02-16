def number_of_islands(grid: list[list[str]]) -> int:
    """

    Given an m x n 2D binary grid which represents a map of '1's (land) and '0's (water), return the number of islands.

    An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.


    Example 1:

    >>> number_of_islands(grid = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]])
    1
    >>> number_of_islands(grid = [["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]])
    3

    Time complexity: 0(m*n), m = len(row), n = len(col)

    This is because the nested for loop runs row*col which is 0(m*n)
    Checking if grid[i][j] == 1 and look up in set visited is constant

    For bfs:
    adding to set -> 0(1)
    appending to list -> 0(1)
    That's why use set and queue instead of list

    checking directions 0(4mn) ~ 0(mn)
    Total : 0(mn) + 0(mn) ~ 0(mn)

    We run BFS NOT for every single cell we visit but rather the ones that are 1
    and have not been visited before. Therefore each 1 in the grid is visited only once.

    Space complexity: 0(m*n)
     We're storing numbers for the most part. In worst case, all the elements in the grid would be 1
     and we would need to store all cells.

     Number of cells = m * n
     Visited would have the worst space complexity of 0(m*n)

     FOR DFS:

     - nested loop: 0(n*m), n = len(row), m = len(col)
     - dfs: worst case all 1s in the arr, first iteration visits all cells, number of cells: n*m
     BUT never visited again so

     0(n*m) + 0(n*m) = 0(n*m)



    """

    row = len(grid)
    col = len(grid[0])
    island = 0
    visited = set()

    def dfs(i, j):
        visited.add((i, j))
        directions = [(1,0), (-1, 0), (0, 1), (0, -1)]
        for d in directions:
            dr = i + d[0]
            dc = j + d[1]
            if 0 <= dr < row and 0 <= dc < col and grid[dr][dc] == "1" and (dr,dc) not in visited:
                dfs(dr, dc)
        return

    for i in range(row):
        for j in range(col):
            if grid[i][j] == "1" and (i,j) not in visited:
                island += 1
                dfs(i, j)
    return island

#BFS SOLUTION
    if not grid:
        return 0


    row = len(grid)
    col = len(grid[0])
    islands = 0
    visited = set()

    def bfs(i, j):
        start = (i,j)
        q = []

        visited.add(start)
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
                    visited.add((a, b))

    for i in range(row):
        for j in range(col):
            if grid[i][j] == "1" and (i,j) not in visited:
                bfs(i, j)
                islands += 1
    return islands





