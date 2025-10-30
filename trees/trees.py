from __future__ import annotations
from typing import Optional, Any


class Tree:
    """

    A recursive tree data structure. It just has a root and a list of subtrees
    (children)

    >>> t1 = Tree(1, [Tree(2, []), Tree(3, [])])
    >>> t1._root
    1

    """

    _root: Optional[Any]
    _subtrees: list[Tree]

    def __init__(self, root: Optional[Any], subtrees: list[Tree]) -> None:
        self._root = root
        self._subtrees = subtrees

    def is_empty(self) -> bool:
        return self._root is None

    def _str_indented(self, depth: int=0) -> str:
        """Return an indented string representation of this tree.

        The indentation level is specified by the <depth> parameter.
        """
        if self.is_empty():
            return ''
        else:
            s = '  ' * depth + str(self._root) + '\n'
            for subtree in self._subtrees:
                # Note that the 'depth' argument to the recursive call is
                # modified.
                s += subtree._str_indented(depth + 1)
            return s

    def __str__(self) -> str:
        """Return a string representation of this tree.
        """
        return self._str_indented(0)

    def size(self) -> int:
        """

        Return the size of the tree. This is the number of nodes in the tree including
        the root.

        >>> t2 = Tree(1, [Tree(2, [Tree(4, [])]), Tree(3, [Tree(5, [])])])
        >>> t2.size()
        5
        >>> t1 = Tree(1, [Tree(2, []), Tree(3, [])])
        >>> t1.size()
        3

        """

        size = 0
        if self._root is None:
            return 0
        elif self._subtrees == []:
            return 1
        else:
            size = 1
            for subtree in self._subtrees:
                size += subtree.size()
            return size










