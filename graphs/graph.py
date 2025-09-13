from __future__ import annotations
from typing import Any 

class _Vertex:
    """
        Instance attributes:

        -item: the data stored in the vertex
        -neighbours: the set of vertices adjacent to this vertex
    
        Representation invariants:

        - self cannot be in self.neighbours
        -all(self in u.neighbours for u in self.neighbours)
    
    """

    # can be int, string, any type
    item: Any 
    neighbours: set[_Vertex]


    def __init__(self, item: Any, neighbours: set[_Vertex]) -> None:
        self.item = item
        self.neighbours = neighbours 
    

class Graph:

    def __init__(self) -> None:
        #dict
        self._vertices = {}

    def add_vertex(self, item: Any) -> None:

        #add key value pair where item is the key and the value is the vertex
        self._vertices[item] = _Vertex(item, set())

    def add_edge(self, item1: Any, item2: Any) -> None:

        # 1. Must check if the vertices actually exist, do a key lookup
        # 2. Define the vertices
        # 3. Add the opposite vertices as neighbours to each vertex 


        if item1 in self._vertices and item2 in self._vertices:
            v1 = self._vertices[item1]
            v2 = self._vertices[item2]
        
            v1.neighbours.add(v2)
            v2.neighbours.add(v1)
        
        else:
            raise ValueError 
    
    def adjacent(self, item1: Any, item2: Any) -> bool:

        #check if v2 is a neighbour of v1 and vise versa 

        if item1 in self._vertices and item2 in self._vertices:
            v1 = self._vertices[item1]
            v2 = self._vertices[item2]

            return v2 in v1.neighbours and v1 in v2.neighbours
        else:
            return False 

    def get_neighbours(self, item: Any) -> set:

        # 1. check if the vertex exists in the set of vertices 
        # 2. Find the neighbours 

        s = set()
        if item in self._vertices:
            v1 = self._vertices[item]

            for n in v1.neighbours:
                s.add(n.item)
        else:
            raise ValueError 
        
        return s 

    

    

