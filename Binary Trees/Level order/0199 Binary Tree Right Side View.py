from typing import Any, Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def rightSideView(root: Optional[TreeNode]) -> list[int]:
    """
    Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.



    Example 1:

    Input: root = [1,2,3,null,5,null,4]

    Output: [1,3,4]

    Explanation:



    Example 2:

    Input: root = [1,2,3,4,null,null,null,5]

    Output: [1,3,4,5]

    Explanation:



    Example 3:

    Input: root = [1,null,3]

    Output: [1,3]

    Example 4:

    Input: root = []

    Output: []



    Constraints:

    The number of nodes in the tree is in the range [0, 100].
    -100 <= Node.val <= 100

    Time:

    - 0(n), n = number of nodes
    - append, popleft -> 0(1) time

    Space:

    - visited: max the height of the tree = 0(h). If tree balanced: log n height, if skewed, h = n
    - lst: max number leaves at the bottom level, 0(w), if balanced bt, then n/2 nodes
    - queue: max number leaves at the bottom level, 0(w)

    0(h) + 0(w) + 0(w)

    worst case: (skewed tree)

    - 0(h+w)
    ~ 0(n)


    """

    if root is None:
        return []

    q = deque([root])
    visited = []

    while q:
        level_size = len(q)
        lst = []

        for i in range(level_size):
            node = q.popleft()
            lst.append(node.val)

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

        visited.append(lst[-1])

    return visited
