# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def isPalindrome(self, head):
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        reversed_2_part = None
        while slow:
            next = slow.next
            slow.next = reversed_2_part
            reversed_2_part = slow
            slow = next

        left, right = head, reversed_2_part
        # while right and right.next:
        while right:
            if right.val != left.val:
                return False
            else:
                right = right.next
                left = left.next
        return True



head = ListNode(1, ListNode(2, ListNode(2, ListNode(1))))
# head = ListNode(1, ListNode(2))
solution = Solution()
print(solution.isPalindrome(head))