class Solution(object):
    def removeDuplicates(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        for letter in s:
            if stack and stack[-1] == letter:
                stack.pop()
            else:
                stack.append(letter)

        return ''.join(stack)




s = "abbaca"
# s = "azzaya"
sol = Solution()
print(sol.removeDuplicates(s))