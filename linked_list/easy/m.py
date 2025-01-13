from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        current = dummy
        while list1 or list2:
            if list1.val < list2.val:
                current.next = list1
            else:
                current.next = list2
            current = current.next
        current.next = list1 or list2

        return dummy.next






list1 = ListNode(1, ListNode(2, ListNode(4)))
list2 = ListNode(1, ListNode(3, ListNode(4)))
a = Solution().mergeTwoLists(list1, list2)