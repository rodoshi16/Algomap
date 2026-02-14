from __future__ import annotations
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def zigzagLevelOrder(root: Optional[TreeNode]) -> list[list[int]]:
        """

        Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).



        Example 1:


        Input: root = [3,9,20,null,null,15,7]
        Output: [[3],[20,9],[15,7]]
        Example 2:

        Input: root = [1]
        Output: [[1]]
        Example 3:

        Input: root = []
        Output: []


        Constraints:

        The number of nodes in the tree is in the range [0, 2000].
        -100 <= Node.val <= 100

        >>> n1 = TreeNode(5)
        >>> n2 = TreeNode(4)
        >>> n3 = TreeNode(3)
        >>> n4 = TreeNode(2, n2, n1)
        >>> n1 = TreeNode(1, n4, n3)
        >>> n1.zigzagLevelOrder()
        [[1], [3, 2], [4, 5]]


        """
        if root is None:
            return []

        q = deque([root])
        lst = []
        flag = True

        while q:
            level_size = len(q)
            visited = []

            for i in range(level_size):
                node = q.popleft()
                visited.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            if not flag:
                visited.reverse()
                flag = True
            else:
                flag = False

            lst.append(visited)

        return lst
