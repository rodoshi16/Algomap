class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def sameTree(p, q):
    """

    Given the roots of two binary trees p and q, write a function to check if
    they are the same or not.

    Two binary trees are considered the same if they are structurally identical,
    and the nodes have the same value.

    >>> t1 = TreeNode(1, TreeNode(2), TreeNode(3))
    >>> t2 = TreeNode(1, TreeNode(2), TreeNode(3))
    >>> sameTree(t1, t2)
    True


    """
    if p is None and q is None:
        return True
    elif p is None or q is None:
        return False
    elif p.val != q.val:
        return False
    else:
        f = None
        left = sameTree(p.left, q.left)
        right = sameTree(p.right, q.right)
        f = left and right

    return f








