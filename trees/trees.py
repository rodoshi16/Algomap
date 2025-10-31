from __future__ import annotations
from typing import Callable, Optional, Any


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

    def __repr__(self) -> str:
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

    def height(self) -> int:
        """

        Find the height of the tree. Height is the length of the longest subtree.

        >>> t3 = Tree(1, [Tree(2, [Tree(4, [Tree(6, [])])]), Tree(3, [Tree(5, [Tree(7, [])])])])
        >>> t3.height()
        4
        >>> t2 = Tree(1, [Tree(2, [Tree(4, [])]), Tree(3, [Tree(5, [])])])
        >>> t2.height()
        3
        >>> t4 = Tree(1, [Tree(2, []), Tree(3, [Tree(5, [])])])
        >>> t4.height()
        3
        >>> t5 = Tree(1, [Tree(2, []), Tree(3, [Tree(5, [Tree(9, [Tree(10, [])])])])])
        >>> t5.height()
        5
        """
        height = 0
        if self._root is None:
            return 0
        elif self._subtrees == []:
            return 1
        else:

           height = 1
           for subtree in self._subtrees:
               if subtree.height() > height:
                   height = subtree.size()
           return height + 1

    def leaves(self) -> list:
        """

        Return the leaves of a tree.

        >>> t = Tree(1, [Tree(2, []), Tree(3, [Tree(5, [Tree(9, [Tree(10, [])])])])])
        >>> t1 = Tree(2, [Tree(5, []), Tree(6, []), Tree(7, [])])
        >>> t2 = Tree(3, [Tree(8, []), Tree(9, []), Tree(10, [])])
        >>> t3 = Tree(4, [Tree(11, []), Tree(12, []), Tree(13, [])])
        >>> t4 = Tree(1, [t1, t2, t3])
        >>> t4.leaves()
        [5, 6, 7, 8, 9, 10, 11, 12, 13]
        >>> t5 = Tree(None, [])
        >>> t5.leaves()
        []
        >>> t6 = Tree(1, [])
        >>> t6.leaves()
        [1]
        >>> Tree(0, [Tree(1, []), Tree(2, []), Tree(3, [])]).leaves()
        [1, 2, 3]
        >>> Tree(0, [Tree(1, [Tree(2, [Tree(3, [])])])]).leaves()
        [3]
        >>> Tree(0, [Tree(1, [Tree(4, [])]), Tree(2, []), Tree(3, [Tree(5, []), Tree(6, [])])]).leaves()
        [4, 2, 5, 6]
        >>> Tree(0, [Tree(1, [Tree(2, [])])]).leaves()
        [2]
        >>> t = Tree(1, [Tree(2, []), Tree(3, [Tree(5, [])])])
        >>> t.leaves()
        [2, 5]


        """

        if self._root is None:
            return []
        elif self._subtrees == []:
            return [self._root]
        else:
            lst = []
            for subtree in self._subtrees:
                lst.extend(subtree.leaves())
            return lst

    def average(self) -> float:
        """Return the average of all values in this tree.
        Return 0.0 if this tree is empty.
        Precondition: this tree is a tree of numbers

        >>> t6 = Tree(2, [Tree(5, []), Tree(6, [])])
        >>> t7 = Tree(3, [Tree(7, [])])
        >>> t8 = Tree(4, [Tree(8, [])])
        >>> t9 = Tree(1, [t6, t7, t8])
        >>> t9.average()
        4.5
        >>> t1 = Tree(2, [Tree(5, []), Tree(6, []), Tree(7, [])])
        >>> t2 = Tree(3, [Tree(8, []), Tree(9, []), Tree(10, [])])
        >>> t3 = Tree(4, [Tree(11, []), Tree(12, []), Tree(13, [])])
        >>> t4 = Tree(1, [t1, t2, t3])
        >>> t4.average()
        7.0

        """
        #track the number of nodes in the tree
        # count the value of the nodes

        if self.is_empty():
            return 0.0
        elif not self._subtrees:
            return float(self._root)
        else:
            total = self._root
            count = 1
            for subtree in self._subtrees:
                n = subtree.recursive_helper()
                total += n[0]
                count += n[1]
            return total/count

    def recursive_helper(self) -> tuple:
        """
        Return a tuple of the value of the node and the count.
        """
        if self._root is None:
            return 0, 0
        elif self._subtrees == []:
            return self._root, 1
        else:
            count = 1
            val = self._root
            for subtree in self._subtrees:
                n = subtree.recursive_helper()
                val += n[0]
                count += n[1]
            return val, count

    def delete_item(self, n: int) -> bool:
        """
        Delete the item n from the tree and return True.
        Return false if not possible


        >>> t = Tree(1, [Tree(2, []), Tree(3, [])])
        >>> t.delete_item(1)
        True

        """

        if self._root is None:
            return False
        elif self._root == n:
            self.delete_root()
            return True
        else:
            for subtree in self._subtrees:
                deleted = subtree.delete_item(n)
                if deleted == True:
                    return True
            return False

    def delete_root(self) -> None:
        """

        Return the root of the tree. If the root has children,
        it will prioritize the right subtree to the new root.

        >>> t = Tree(1, [Tree(2, []), Tree(3, [])])
        >>> t.delete_item(1)
        >>> t
        3
         2


        """
        if self._subtrees == []:
            self._root = None
        else:
            right_subtree = self._subtrees[-1]
            self._root = right_subtree._root
            if right_subtree._subtrees != []:
                self._subtrees.remove(right_subtree)
                self._subtrees.extend(right_subtree._subtrees)

    def preorder(self, act: Callable[[Any], None]) -> None:
        """
        Perform a preorder traversal of the tree and apply 'act' to each node's root.

        >>> lt = Tree(2, [Tree(4, []), Tree(5, [])])
        >>> rt = Tree(13, [Tree(16, []), Tree(17, [])])
        >>> t = Tree(10, [lt, rt])
        >>> t.preorder(print)
        10
        2
        4
        5
        13
        16
        17
        """
        act(self._root)
        for subtree in self._subtrees:
            subtree.preorder(act)














