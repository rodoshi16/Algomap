from __future__ import annotations
from typing import Any


class _Vertex:
    """

    A vertex in a graph.

    Instance attributes:
     - item: The data stored in the vertex
     - neighbours: The vertices that are adjacent to this vertex

     Graphs allow circles

    >>> v1 = _Vertex('a', [])
    >>> v2 = _Vertex('b', [])
    >>> v3 = _Vertex('c', [])
    >>> v1.neighbours = {v2, v3}
    >>> v2.neighbours = {v1, v3}
    >>> v3.neighbours = {v1, v2}

    """

    item: Any
    neighbours: [_Vertex]

    def __init__(self, item: Any, neighbours: [_Vertex]):
        self.item = item
        self.neighbours = neighbours


class Graph:
    """

    A graph is a set of vertices and edges. Each pair in an edge is a set
    of two distinct vertices and the order does not matter.

    Adjacent: there is an edge between the two vertices
    Degree: number of neighbours or how many edges v is a part of
    Path: sequence of vertices
    Length: one less than no of vertices
    connected: there is a path between u and u'

    >>> g = Graph()
    >>> g.add_vertex('1')
    >>> g.add_vertex('2')
    >>> g.add_vertex('3')
    >>> g.add_edge('1', '2')
    >>> g.add_edge('1', '3')


    """

    def __init__(self) -> None:
        """
        Initialize an empty graph (no vertices or edges).
        """
        self._vertices = {}

    def add_vertex(self, item: Any) -> None:
        """

        Add a vertex with an item of Any in the graph


        """
        self._vertices[item] = _Vertex(item, [])

    def add_edge(self, item1: Any, item2: Any) -> None:
        """

        Add an edge between the vertices item2 and item1

        """

        #check if these vertices are in the graph -> otherwise its valid
        if item1 in self._vertices and item2 in self._vertices:
            v1 = self._vertices[item1]
            v2 = self._vertices[item2]

            v1.neighbours.append(v2)
            v2.neighbours.append(v1)

        else:
            raise ValueError

    def adjacency_matrix(self):
        """

        >>> g = Graph()
        >>> g.add_vertex('8')
        >>> g.add_vertex('9')
        >>> g.add_vertex('7')
        >>> g.add_edge('8', '9')
        >>> g.add_edge('8', '7')
        >>> g.adjacency_matrix()
        [[0, 1, 1], [1, 0, 0], [1, 0, 0]]


        """

        m = []
        for i in range(len(self._vertices)):
            m.append([0]*len(self._vertices))

        index = {}
        count = 0
        for key in self._vertices:
            index[key] = count
            count += 1

        for v in self._vertices:
            vertex = self._vertices[v]
            for n in vertex.neighbours:
                m[index[v]][index[n.item]] = 1
                m[index[n.item]][index[v]] = 1
        return m

    def bfs(self, start: Any) -> list[Any]:
        """
        Traverse the graph in breath first search and list out the
        items

        >>> g = Graph()
        >>> g.add_vertex('A')
        >>> g.add_vertex('B')
        >>> g.add_vertex('C')
        >>> g.add_vertex('D')
        >>> g.add_vertex('G')
        >>> g.add_edge('A', 'B')
        >>> g.add_edge('A', 'C')
        >>> g.add_edge('B', 'D')
        >>> g.add_edge('C', 'G')
        >>> g.bfs('A')
        ['A', 'B', 'C', 'D', 'G']



        """
        q = []
        visited = []

        q.append(start)
        visited.append(start)

        while q:
            curr = q.pop(0)
            for n in self._vertices[curr].neighbours:
                if n.item not in visited:
                    q.append(n.item)
                    visited.append(n.item)

        return visited

    def dfs(self, start: Any) -> list[Any]:
        """

        Traverse through the graph in depth first search.

        >>> g = Graph()
        >>> g.add_vertex('A')
        >>> g.add_vertex('B')
        >>> g.add_vertex('C')
        >>> g.add_vertex('D')
        >>> g.add_vertex('G')
        >>> g.add_edge('A', 'B')
        >>> g.add_edge('A', 'C')
        >>> g.add_edge('B', 'D')
        >>> g.add_edge('C', 'G')
        >>> g.dfs('A')
        ['A', 'B', 'D', 'C', 'G']


        """

        s = []
        visited = []

        s.append(start)
        visited.append(start)

        while s:
            curr = s.pop()

            if curr not in visited:
                visited.append(curr)

            for n in reversed(self._vertices[curr].neighbours):
                if n.item not in visited:
                    s.append(n.item)

        return visited

    def dfs_recursive(self, start: Any, visited=None):
        """
        Recursive approach to depth first search

        >>> g = Graph()
        >>> g.add_vertex('A')
        >>> g.add_vertex('B')
        >>> g.add_vertex('C')
        >>> g.add_vertex('D')
        >>> g.add_vertex('G')
        >>> g.add_edge('A', 'B')
        >>> g.add_edge('A', 'C')
        >>> g.add_edge('B', 'D')
        >>> g.add_edge('C', 'G')
        >>> g.dfs_recursive('A')
        ['A', 'B', 'D', 'C', 'G']



        """

        if visited is None:
            visited = []

        visited.append(start)

        for n in self._vertices[start].neighbours:
            if n.item not in visited:
                self.dfs_recursive(n.item, visited)

        return visited

















