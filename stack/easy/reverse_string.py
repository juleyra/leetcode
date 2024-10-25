class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        stack = list(s)
        for i in range(0, len(stack)):
            s[i] = stack.pop()



s = ["h","e","l","l","o"]
Solution().reverseString(s)
print(s)