import heapq


class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        max_stones = [-weight for weight in stones]
        heapq.heapify(max_stones)
        while len(max_stones) > 1:
            first_stone = heapq.heappop(max_stones)
            second_stone = heapq.heappop(max_stones)
            if -first_stone > -second_stone:
                second_stone = first_stone - second_stone
                heapq.heappush(max_stones, second_stone)
                heapq.heapify(max_stones)
        return 0 if not max_stones else -heapq.heappop(max_stones)



stones = [2,7,4,1,8,1]
sol = Solution()
sol.lastStoneWeight(stones)
