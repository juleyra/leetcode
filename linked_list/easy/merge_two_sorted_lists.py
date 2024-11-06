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

    def mergeTwoLists(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(-1)
        current = dummy

        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        current.next = list1 or list2

        return dummy.next


# [1,2,4]
# [1,3,4]
head1 = ListNode(1, ListNode(4, ListNode(6)))
head2 = ListNode(2, ListNode(3, ListNode(5)))

# [], [0]

solution = Solution()
solution.printList(solution.mergeTwoLists(head1, head2))
