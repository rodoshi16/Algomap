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
        dummy = ListNode()
        tail = dummy

        while list1 and list2:
                if list1.val < list2.val:
                        tail.next = list1
                        list1 = list1.next
                else:
                        tail.next = list2
                        list2 = list2.next

                tail = tail.next

        if list1:
                tail.next = list1
        elif list2:
                tail.next = list2

        return dummy.next







