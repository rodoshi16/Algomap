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

    #initialize
    curr, prev = head, None

    while curr is not None:
        #store the next value
        temp = curr.next
        #draw the backwards connection
        curr.next = prev
        #move the prev pointer to curr
        prev = curr
        #curr will move to temp (which is technically next in the list)
        curr = temp

    return prev



