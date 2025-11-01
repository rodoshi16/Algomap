# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def invertTree(root: Optional[TreeNode]) -> Optional[TreeNode]:
    """

    Given the root of a binary tree, invert the tree, and return its root.
    Example 1:

    >>> a = TreeNode(1)
    >>> b = TreeNode(2)
    >>> c = TreeNode(3)
    >>> a.left, a.right = b, c
    >>> res = invertTree(a)
    >>> (res.val, res.left.val, res.right.val)
    (1, 3, 2)

    >>> a = TreeNode(1)
    >>> res = invertTree(a)
    >>> (res.val, res.left, res.right)
    (1, None, None)

    >>> res = invertTree(None)
    >>> res is None
    True

    >>> a = TreeNode(1)
    >>> a.left = TreeNode(2)
    >>> a.left.left = TreeNode(3)
    >>> res = invertTree(a)
    >>> (res.val, res.left, res.right.val)
    (1, None, 2)

    >>> res.right.right.val
    3


    """
    if root is None:
        return root

    root.left, root.right = root.right, root.left

    invertTree(root.left)
    invertTree(root.right)
    return root


