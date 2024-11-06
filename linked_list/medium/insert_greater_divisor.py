# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    @staticmethod
    def printList(head):
        while head:
            print(head.val, end=" ")
            head = head.next
        print()

    def insertGreatestCommonDivisors(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head or not head.next:
            return head

        def get_cd(a, b):
            while b:
                a, b = b, a % b
            return a

        current = head
        while current and current.next:
            next_chain = current.next
            current.next = ListNode(get_cd(current.val, current.next.val), next_chain)
            current = current.next.next
        return head



head = ListNode(18, ListNode(6, ListNode(10, ListNode(3))))
sol = Solution()
sol.printList(sol.insertGreatestCommonDivisors(head))