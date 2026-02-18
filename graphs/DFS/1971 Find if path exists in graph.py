from collections import defaultdict


def validPath(n: int, edges: list[list[int]], source: int, destination: int) -> bool:
    """

    >>> validPath(7, [["A", "B"], ["A", "D"], ["A", "E"], ["B", "F"], ["D", "L"], ["E", "Q"]], "A", "Q")
    True
    >>> validPath(6, [[0,1],[1,2],[2,0]], 0, 2)
    True

    """

    d = {}
    for u,v in edges:
        d.setdefault(u, []).append(v)
        d.setdefault(v, []).append(u)

    visited = set()

    def dfs(node):
        visited.add(node)

        if node == destination:
            return True

        for neighbour in d[node]:
            if neighbour not in visited:
                if dfs(neighbour):
                    return True
        return False

    return dfs(source)
