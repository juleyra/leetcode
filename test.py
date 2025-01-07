class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        deleted = False
        for i in range(len(s) // 2):
            cur = s[i]
            last = s[len(s) - i - 1]
            s[len(s) - i - 1]
            if cur != last:
                if deleted:
                    return False
                deleted = True
        return True


s = "abca"

a = Solution()
print(a.validPalindrome(s))