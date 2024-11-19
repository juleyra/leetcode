class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        frequency = {}
        for char in s:
            frequency[char] = frequency.get(char, 0) + 1
        for i, char in enumerate(s):
            if frequency[char] == 1:
                return i
        return -1

s = "leetcode"
sol = Solution()
print(sol.firstUniqChar(s))