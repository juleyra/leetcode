# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):

    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        prev = None
        current = head
        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next

        return prev

    @staticmethod
    def printList(head):
        while head:
            print(head.val, end=" ")
            head = head.next
        print()


NodeHead1 = ListNode(3, ListNode(4, ListNode(5)))
solution = Solution()
solution.printList(solution.reverseList(NodeHead1))

# print(NodeHead)
# input = [7]