class Solution(object):
    def removeDuplicates(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return s
        stack = []
        for letter in s:
            if stack:
                # if letter.isupper() and stack[-1] == letter.lower() or letter.islower() and stack[-1] == letter.upper():
                if stack and stack[-1].swapcase() == letter:
                    stack.pop()
                else:
                    stack.append(letter)
            else:
                stack.append(letter)

        return ''.join(stack)


# s = "leEeetcode"
s = "abBAcC"
sol = Solution()
print(sol.removeDuplicates(s))