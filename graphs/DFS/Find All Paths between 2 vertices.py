from collections import defaultdict


def find_paths(n: int, edges: list[list[int]], source, destination) -> list[list]:
    """
    >>> find_paths(6, [["A","B"],["A","C"], ["A","D"], ["D","E"], ["C","E"], ["E","F"], ["B","F"]], "A", "B")
    [['A', 'B'], ['A', 'C', 'E', 'F', 'B'], ['A', 'D', 'E', 'F', 'B']]

    Time Complexity: 0(V-1!)



    """

    d = {}

    for u, v in edges:
        d.setdefault(u, []).append(v)
        d.setdefault(v, []).append(u)

    path = []
    paths = []

    def dfs(node):
        path.append(node)

        if node == destination:
            paths.append(path.copy())

        else:
            for neighbour in d[node]:
                if neighbour not in path:
                    dfs(neighbour)

        path.pop()

    dfs(source)
    return paths






