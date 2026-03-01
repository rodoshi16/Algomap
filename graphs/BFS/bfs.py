from collections import defaultdict, deque


def bfs(root, edges: list):
    """

    Return items in a breadth first search traversal

    >>> bfs("a", [["a","b"], ["a","c"], ["b","d"], ["b","e"], ["c","f"], ["c","g"]])
    ['a', 'b', 'c', 'd', 'e', 'f', 'g']

    Time: 0(V+ E)

    - we go through every vertex
    - for every vertex, we loop through the neighbours
    - its not V*E because we skip if its already in visited

    Space: 0(V)

    - visited: V vertices
    - queue: at most V vertices



    """
    if root is None:
        return []

    d = defaultdict(list)

    for u, v in edges:
        d.setdefault(u, []).append(v)
        d.setdefault(v, []).append(u)

    q = deque([root])
    visited = []
    while q:
        temp = q.popleft()
        visited.append(temp)

        for n in d[temp]:
            if n not in visited:
                q.append(n)

    return visited


