class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        chars = set()
        maxLen, start, end = 0, 0, 0
        while end < len(s):
            if s[end] not in chars:
                chars.add(s[end])
                maxLen = max(maxLen, end-start+1)
                end +=1
            else:
                chars.remove(s[start])
                start+=1

        return maxLen


s = "abcabcbb"
sol = Solution()
sol.lengthOfLongestSubstring(s)


