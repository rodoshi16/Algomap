# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def levelorder(root):
    """
    Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).



    Example 1:


    Input: root = [3,9,20,null,null,15,7]
    Output: [[3],[9,20],[15,7]]
    Example 2:

    Input: root = [1]
    Output: [[1]]
    Example 3:

    Input: root = []
    Output: []


    Constraints:

    The number of nodes in the tree is in the range [0, 2000].
    -1000 <= Node.val <= 1000

    """
    if root is None:
        return []

    q = [root]
    lst = []

    #

    while q:
        level_size = len(q)
        visited = []

        for i in range(level_size):
            node = q.pop(0)
            visited.append(node.val)

            if node.left:
                q.append(node.left.val)
            if node.right:
                q.append(node.right.val)

        lst.append(visited)

    return lst




