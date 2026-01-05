class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def countNodes(root: [TreeNode]) -> int:
    """

    >>> countNodes(TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(4))))
    4

    Base cases:

    - empty tree (0 nodes)
    - leaf node

    """

    count = 1
    if root is None:
        return 0
    elif root.left is None and root.right is None:
        return 1

    else:
        count += countNodes(root.left)
        count += countNodes(root.right)
    return count



