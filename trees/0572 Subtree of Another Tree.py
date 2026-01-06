class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def sub(root, subRoot):
    def sametree(p, q):
        if p is None and q is None:
            return True
        elif p is None or q is None:
            return False
        elif p.val != q.val:
            return False
        return sametree(p.left, q.left) and sametree(p.right, q.right)

    if root is None:
        return False

    return sametree(root, subRoot) or sametree(root.left, subRoot) or sametree(root.right, subRoot)




