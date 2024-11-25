import heapq
from collections import Counter


class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """

        heap_freq = Counter(s)
        max_heap = [(-freq, char) for char, freq in heap_freq.items()]
        heapq.heapify(max_heap)
        res = []
        while max_heap:
            freq, char = heapq.heappop(max_heap)
            res.append(char*(-freq))
        return ''.join(res)


sol = Solution()
print(sol.frequencySort("trersesess"))