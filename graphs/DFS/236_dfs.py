from __future__ import annotations
from typing import Any, Optional
import math

class Vertex:
    color: str
    d: int
    p: Vertex
    f: int

    def __init__(self, color: str, d: int, f: int, p: Optional[Vertex]):
        self.color = color
        self.d = d
        self.f = f
        self.p = None


def dfs(V: Vertex, e: dict):
    for v in V:
        v.color = "white"
        v.d = math.inf
        v.f = math.inf
        v.p = None
    time = 0

    def visit(V, e, u):
        u.color = "grey"
        u.d = time
        for (u,v) in e:
            if v.color == "white":
                v.p = u
                visit(V,e)
            u.color = "black"
            u.f = time

    for v in V:
        if v.color == "white":
            visit(V, e, v)






