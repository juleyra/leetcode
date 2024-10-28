from collections import deque

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        d = deque(filter(str.isalnum, s))
        while len(d) > 1:
            if d.popleft() != d.pop():
                return False
        return True

sol = Solution()
a = sol.isPalindrome("A man, a plan, a canal: Panama")