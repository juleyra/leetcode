import heapq
import math


class Solution:
    def remainingGifts(self, gifts, k):
        max_heap = [-gift for gift in gifts]
        heapq.heapify(max_heap)
        for _ in range(k):
            max = -heapq.heappop(max_heap)
            heapq.heappush(max_heap, -int(max**0.5))
        return -sum(max_heap)



gifts = [4, 9, 16]
sol = Solution()
sol.remainingGifts(gifts, 2)