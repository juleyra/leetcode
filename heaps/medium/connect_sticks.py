import heapq

class Solution:
    def connectSticks(self, sticks):
        heapq.heapify(sticks)
        cost = 0
        while len(sticks) > 1:
            price = heapq.heappop(sticks) + heapq.heappop(sticks)
            cost += price
            heapq.heappush(sticks, price)

        return cost





sol = Solution()
sticks = [5, 5, 5, 5]
min_price = sol.connectSticks(sticks)
print(min_price)
