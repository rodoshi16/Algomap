from __future__ import annotations
from typing import Any


class _Vertex:
    """

    A vertex in a graph.

    Instance attributes:
     - item: The data stored in the vertex
     - neighbours: The vertices that are adjacent to this vertex

    >>> v1 = _Vertex('a', set())
    >>> v2 = _Vertex('b', set())
    >>> v3 = _Vertex('c', set())
    >>> v1.neighbours = {v2, v3}
    >>> v2.neighbours = {v1, v3}
    >>> v3.neighbours = {v1, v2}

    """
    item: Any
    neighbours: set[_Vertex]


class graph:
    """

    A graph is a set of vertices and edges. Each pair in an edge is a set
    of two distinct vertices and the order does not matter.

    Adjacent: there is an edge between the two vertices
    Degree: number of neighbours or how many edges v is a part of
    Path: sequence of vertices
    Length: one less than no of vertices
    connected: there is a path between u and u'








    """



