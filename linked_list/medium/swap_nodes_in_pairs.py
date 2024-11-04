# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head or not head.next:
            return head

        dummy = ListNode(0)
        dummy.next = head
        current = dummy

        while current.next and current.next.next:
            first = current.next
            second = current.next.next

            first.next = second.next
            second.next = first
            current.next = second

            current = current.next.next

        return dummy.next

    @staticmethod
    def printList(head):
        while head:
            print(head.val, end=" ")
            head = head.next
        print()

head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
sol = Solution()
a = sol.printList(sol.swapPairs(head))