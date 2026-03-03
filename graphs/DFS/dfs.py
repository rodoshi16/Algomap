from typing import Any
from collections import deque


def dfs(n: int, edges: list[list[Any]]):
    """

    Given  an undirected graph, visit the vertices in DFS.

    >>> dfs(6, [["A","B"],["A","C"], ["A","D"], ["D","E"], ["C","E"], ["E","F"], ["B","F"]])
    {"A", "B", "C", "D", "E", "F"}

    """

    #NOTE: for a direction graph you just wouldn't traverse backwards in edge list
    # just the first line of setdefault would be okay

    d = {}

    for u, v in edges:
        d.setdefault(u, []).append(v)
        d.setdefault(v, []).append(u)

    visited = []

    def dfs(start):
        s = [start]

        while s:
            temp = s.pop()
            visited.append(temp)

            for n in d[temp]:
                if n not in visited:
                    s.append(n)

    for node in d:
        if node not in visited:
            dfs(node)

    return visited

    # d = {}
    # for u, v in edges:
    #     d.setdefault(u, []).append(v)
    #     d.setdefault(v, []).append(u)
    #
    # visited = set()
    #
    # def dfs_visit(k: Any):
    #     visited.add(k)
    #     for neighbour in d[k]:
    #         if neighbour not in visited:
    #             dfs_visit(neighbour)
    #
    # for key in d:
    #     if key not in visited:
    #         dfs_visit(key)
    #
    # return visited










