class Solution(object):
    def removeStars(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        for letter in s:
            if letter == '*':
                if stack:
                    stack.pop()
            else:
                stack.append(letter)

        return ''.join(stack)




solution = Solution()
print(solution.removeStars("abc*de*f"))  # Output: "abdf"
