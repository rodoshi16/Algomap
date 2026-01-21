from typing import Any


class Node:

    def __init__(self, val: Any):
        self.val = val
        self.left = None
        self.right = None


class BinaryTree:

    def __init__(self, root: Node):
        self.root = root

    def insert(self, n: Any):
        """

        Binary tree must have at most 2 children, no rules about the values.
        For insert, just insert at the very first leaf.

        >>> root = Node(1)
        >>> root.left = Node(2)
        >>> root.right = Node(3)
        >>> b = BinaryTree(root)
        >>> b.insert(8)


        """

        if self.root is None:
            self.root = Node(n)
            return True
        elif self.root.left is None:
            self.root.left = Node(n)
            return True
        elif self.root.right is None:
            self.root.right = Node(n)
            return True

        if BinaryTree(self.root.left).insert(n):
            return True
        return BinaryTree(self.root.right).insert(n)
