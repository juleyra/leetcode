# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: None Do not return anything, modify head in-place instead.
        """
        # find the middle of the list
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        reversed = None
        current = slow
        while current:
            next = current.next
            current.next = reversed
            reversed = current
            current = next

        first, second = head, reversed
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2

        return head

    @staticmethod
    def printList(head):
        while head:
            print(head.val, end=" ")
            head = head.next
        print()




head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
sol = Solution()
sol.printList(sol.reorderList(head))


# [1,5,2,4,3]