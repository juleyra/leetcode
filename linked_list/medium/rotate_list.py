# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    # k = k % length  12%5 = 2

    def rotateRight(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        if not head or not head.next:
            return head

        length = 0
        current = head
        while current:
            length += 1
            current = current.next

        nodes_to_cut = k % length
        if not nodes_to_cut:
            return head

        current = head
        for i in range(length - nodes_to_cut - 1):
            current = current.next

        # 4->5
        new_head = current.next
        a = 5







head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
sol = Solution()
sol.rotateRight(head, 2)