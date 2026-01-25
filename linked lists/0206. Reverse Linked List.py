from typing import Optional

class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    """

    Given the head of a singly linked list, reverse the list, and return the reversed list.

    Example 1:


    Input: head = [1,2,3,4,5]
    Output: [5,4,3,2,1]
    Example 2:


    Input: head = [1,2]
    Output: [2,1]
    Example 3:

    Input: head = []
    Output: []


    Constraints:

    The number of nodes in the list is the range [0, 5000].
    -5000 <= Node.val <= 5000

    Time complexity: 0(n)
    Space complexity: 0(1)

    """
    prev = None
    curr = head
    while curr is not None:
        a = curr.next
        curr.next = prev
        prev = curr
        curr = a

    return prev


