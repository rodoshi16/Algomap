from collections import defaultdict


def allPathsSourceTarget(graph: list[list[int]]) -> list[list[int]]:

    """

    Given a directed acyclic graph (DAG) of n nodes labeled from 0 to n - 1, find all possible paths from node 0 to node n - 1 and return them in any order.

    The graph is given as follows: graph[i] is a list of all nodes you can visit from node i (i.e., there is a directed edge from node i to node graph[i][j]).



    Example 1:


    Input: graph = [[1,2],[3],[3],[]]
    Output: [[0,1,3],[0,2,3]]
    Explanation: There are two paths: 0 -> 1 -> 3 and 0 -> 2 -> 3.
    Example 2:


    Input: graph = [[4,3,1],[3,2,4],[3],[4],[]]
    Output: [[0,4],[0,3,4],[0,1,3,4],[0,1,2,3,4],[0,1,4]]

    >>> allPathsSourceTarget([[4,3,1],[3,2,4],[],[4],[]])
    [[0,1,3],[0,2,3]]

    """
    d = defaultdict(list)
    for i in range(len(graph)):
        d[i].extend(graph[i])


    paths = []
    path = []

    def dfs(node):
        path.append(node)

        if not d[node]:
            paths.append(path.copy())

        for nei in d[node]:
            if nei not in path:
                dfs(nei)

        path.pop()

    dfs(0)
    return paths
