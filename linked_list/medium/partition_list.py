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

    def partition(self, head, x):
        """
        :type head: Optional[ListNode]
        :type x: int
        :rtype: Optional[ListNode]
        """

        LL = ListNode()
        RL = ListNode()
        curr, res, right_head = head, LL, RL
        while curr:
            if curr.val >= x:
                RL.next = ListNode(curr.val)
                RL = RL.next
                # is it poss to solve without ListNode() ????
            else:
                LL.next = ListNode(curr.val)
                LL = LL.next
            curr = curr.next
        LL.next = right_head.next

        return res.next

    def partition_3(self, head, x):
        smaller_part, bigger_part = ListNode(0), ListNode(0)
        sp, bp = smaller_part, bigger_part
        current = head
        while current:
            if current.val < x:
                sp.next = current
                sp = sp.next
            else:
                bp.next = current
                bp = bp.next
            current = current.next

        bp.next = None
        sp.next = bigger_part.next

        return smaller_part.next


head = ListNode(1, ListNode(4, ListNode(3, ListNode(2, ListNode(5, ListNode(2))))))
sol = Solution()
res = sol.printList(sol.partition_3(head, 3))
