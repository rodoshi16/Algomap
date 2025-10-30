from __future__ import annotations

from typing import Any, Optional


class _Node:
    item: Any
    #by default it doesnt link to any other node
    next: Optional[_Node]
    def __init__(self, item: Any):
        self.item = item
        self.next = None


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
        >>> l1 = LinkedList()
        >>> l1._first = n1
        >>> l1.print_items()
        1
        2
        3

        """
        if self._first is not None:
            node = self._first

            while node is not None:
                print(node.item)
                node = node.next

    def toList(self) -> list:
        """
        Take a linked list and turn that into a list.

        """

        if self._first is not None:
            curr = self._first

        items = []

        while curr is not None:
            items.append(curr.item)
            curr = curr.next

        return items
    def __getitem__(self, i: int):
        """
        Return the item of the linkedist at index i.


        """

        if self._first is not None:
            node = self._first

        index = 0
        while node is not None:
            if index == i:
                return node.item

            else:
                curr = curr.next
                index += 1

        #end of list and no item no has been returned, we have reached the end of the linked list and that i > indices available
        raise IndexError

    #Another way of doing the same method but in a different traversal logic

    def __getitem__(self, i: int):

        node = self._first
        index = 0

        #demorgan's law, node is not None and index != i
        while not (node is None or index == i):
            node = node.next
            index += 1

        #end of the while loop, either node is none or index == i
        if node is none:
            return IndexError
        else:
            return node.item


    def append(self, item: Any):
        new_node = _Node(item)
        if self._first is None:
            self._first = new_node
        else:
            curr = self._first
            while curr.next is not None:
                curr = curr.next

            curr.next = new_node


    def insert(self, i: int, item: Any):
        """

        insert a node with item at index i.

        >>> n1 = _Node(1)
        >>> n2 = _Node(2)
        >>> n3 = _Node(3)
        >>> n1.next = n2
        >>> n2.next = n3
        >>> l1 = LinkedList()
        >>> l1._first = n1
        >>> l1.insert(2, 7)
        1
        2
        3
        7

        """
        new_node = _Node(item)

        curr = self._first
        index = 0

        while curr is not None:
            if index == i:
                val = curr.next
                curr.next = new_node
                new_node.next = val

            else:
                curr = curr.next
                index += 1

        raise IndexError


    def delete_node(self, item: Any) -> None:
        """

        >>> n1 = _Node(1)
        >>> n2 = _Node(2)
        >>> n3 = _Node(3)
        >>> n1.next = n2
        >>> n2.next = n3
        >>> l1 = LinkedList()
        >>> l1._first = n1
        >>> l1.delete_node(3)
        >>> l1.print_items()
        1
        2




        """
        if self._first is None:
            return

        if self._first.item == item:
            self._first = self._first.next
            return

        curr = self._first
        while curr.next is not None:
            if curr.next.item == item:
                curr.next = curr.next.next
                return
            curr = curr.next



if __name__ == '__main__':
    import doctest
    doctest.testmod()










