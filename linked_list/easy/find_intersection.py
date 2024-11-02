# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return None

        pointerA, pointerB = headA, headB

        while pointerA != pointerB:
            if pointerA:
                pointerA = pointerA.next
            else:
                pointerA = headB

            if pointerB:
                pointerB = pointerB.next
            else:
                pointerB = headA

        return pointerA

[4,1,8,4,5]
[5,6,1,8,4,5]

intersection = ListNode(8, ListNode(4, ListNode(5)))

# listA = ListNode(4, ListNode(1, intersection))  # List A: 4 -> 1 -> 8 -> 4 -> 5
listA = ListNode(4, ListNode(1))  # List A: 4 -> 1 -> 8 -> 4 -> 5
# listB = ListNode(5, ListNode(6, ListNode(1, intersection)))
listB = ListNode(5, ListNode(6, ListNode(1)))


sol = Solution()
a = sol.getIntersectionNode(listA, listB)