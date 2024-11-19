from collections import defaultdict
class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        freq = defaultdict(int)
        for el in arr:
            freq[el] += 1

        return len(set(freq.values())) == len(freq)


# arr = [1,2,2,1,1,3]
arr = [1,2]
sol = Solution()
print(sol.uniqueOccurrences(arr))