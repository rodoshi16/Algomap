from typing import Optional
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def inorderTraversal(root: Optional[TreeNode]) -> list[int]:
    """

    >>> n1 = TreeNode(6)
    >>> n2 = TreeNode(7)
    >>> n3 = TreeNode(9)
    >>> n8 = TreeNode(4)
    >>> n4 = TreeNode(8, n3)
    >>> n5 = TreeNode(5, n1, n2)
    >>> n6 = TreeNode(2, n8, n5)
    >>> n9 = TreeNode(3, n4)
    >>> n10 = TreeNode(1, n6, n9)
    >>> inorderTraversal(n10)
    [4, 2, 6, 5, 7, 1, 9, 8, 3]




    """
    if root is None:
        return []

    return inorderTraversal(root.left) + [root.val] + inorderTraversal(root.right)







