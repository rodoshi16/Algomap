from typing import Optional


class ListNode:
        def __init__(self, val=0, next=None):
                self.val = val
                self.next = next


def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        You are given the heads of two sorted linked lists list1 and list2.

        Merge the two lists into one sorted list. The list should be made by
        splicing together the nodes of the first two lists.

        Return the head of the merged linked list.

        >>> n3 = ListNode(3)
        >>> n2 = ListNode(2, n3)
        >>> n1 = ListNode(1, n2)
        >>> n6 = ListNode(5)
        >>> n5 = ListNode(3, n6)
        >>> n4 = ListNode(1, n5)
        >>> mergeTwoLists(n1, n4)
        [1, 1, 2, 3, 3, 5]


        """

        l = []

        curr1 = list1
        curr2 = list2

        while curr1 and curr2 is not None:
                l.append(curr1.next.val)
                l.append(curr2.next.val)
                curr1 = curr1.next
                curr2 = curr2.next

        return l

