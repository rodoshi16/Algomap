def adjacency_list(edges: list):
    """
    Return an adjacency list for the graph from its list of edges

    If the graph is bidirectional, traverse both ways
    For a one directional graph, only one line is needed

    """



    d = {}
    for u, v in edges:
        d.setdefault(u, []).append(v)
        d.setdefault(v, []).append(u)

    return d


def adjacency_matrix(edges: list):
    """
    Return an adjacency matrix from the list of a graphs edges

    >>> adjacency_matrix([[1, 4], [1, 2], [2, 3], [4, 3]])
    [[0, 1, 0, 1], [1, 0, 1, 0], [0, 1, 0, 1], [1, 0, 1, 0]]

    """
    n = len(edges)
    m = []
    for i in range(n):
        row = [0] * n
        m.append(row)

    for u, v in edges:
        m[u-1][v-1] = 1
        #only add this last line if its directional
        m[v-1][u-1] = 1

    return m
