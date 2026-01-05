# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def maxDepth(root: [TreeNode]) -> int:
    """
    Given the root of a binary tree, return its maximum depth.

    A binary tree's maximum depth is the number of nodes along the longest
    path from the root node down to the farthest leaf node.

    >>> maxDepth(TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(4))))
    3

    """
    m = 0
    if root is None:
        return 0
    elif root.left is None and root.right is None:
        return 1

    if root.right is not None:
        count = 1
        count += maxDepth(root.right)
        m = max(m, count)

    if root.left is not None:
        count = 1
        count += maxDepth(root.left)
        m = max(m, count)

    return m







