import heapq


def d(src, adj):
    """

    Given a weighted undirected graph and a source. We need to find the shortest path
    distances from the src to all other vertices in the graph.

    >>> d(0, [[[1, 4], [2, 8]], [[0, 4], [4, 6], [2,3]], [[0, 8], [3, 2], [1,3]], [[2, 2], [4, 10]], [[1, 6], [3, 10]]])
    [0, 4, 7, 9, 10]


    Why wouldn't a classic BFS work for a weighted graph?

    BFS assumes that every edge has the same cost. Because of that, it explores
    nodes in order of the fewest number of edges from the source.

    However, in a weighted graph, taking fewer edges does not necessarily mean
    taking the minimum-cost path.

    For example, from 0 to 3: BFS would return 0-2-3 which has a cost of 10
    However, we know we can traverse 0-1-2-3 which would have a cost of 9

    """

    minheap = [(0, src)]
    dist = {src: 0}

    while minheap:
        w, node = heapq.heappop(minheap)

        if w > dist[node]:
            continue

        for nei in adj[node]:
            if nei[0] not in dist or dist[nei[0]] > nei[1] + w:
                heapq.heappush(minheap, (nei[1] + w, nei[0]))

                if nei[0] not in dist:
                    dist[nei[0]] = nei[1] + w
                else:
                    dist[nei[0]] = min(dist[nei[0]], nei[1] + w)

    return dist.values()













