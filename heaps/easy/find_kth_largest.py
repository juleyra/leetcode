import heapq
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        max_heap = [-el for el in nums]
        heapq.heapify(max_heap)
        needed = None
        for _ in range(k):
            needed = -heapq.heappop(max_heap)
        return needed

sol = Solution()
print(sol.findKthLargest([3,2,1,5,6,4], 3))