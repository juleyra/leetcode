from collections import defaultdict
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        longestPal = 0
        centralElem = 0
        freq = defaultdict(int)
        for l in s:
            freq[l] += 1
        for l, amount in freq.items():
            if amount % 2 == 0:
                longestPal += amount
            else:
                centralElem = 1
                longestPal += amount-1

        return longestPal + centralElem


s = "abccccdd"
sol = Solution()
print(sol.longestPalindrome(s))