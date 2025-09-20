from __future__ import annotations
from typing import Optional 


class _Node:
    item: Any
    #by default it doesnt link to any other node
    next: Optional[_Node]


class LinkedList:
    _first: Optional[_Node]

    def __init__(self) -> None:
        self._first = None 
    
    def print_items(self):
        """

        >>> n1 = _Node(1)
        >>> n2 = _Node(2)
        >>> n3 = _Node(3)
        >>> n1.next = n2
        >>> n2.next = n3
        >>> l1 = LinkedList(n1)
        >>> l1.print()
        1
        2
        3
        
        """
        if self._first is not None:
            node = self._first 

            while node is not None:
                print(node.item)
                node = node.next
        



if __name__ == '__main__':
    import doctest
    doctest.testmod()



                






