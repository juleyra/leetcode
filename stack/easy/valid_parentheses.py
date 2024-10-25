class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        brackets = {
            '(' : ')',
            '{' : '}',
            '[' : ']'
        }
        for elem in s:
            if elem in brackets.keys():
                stack.append(elem)
            else:
                if not stack:
                    return False
                last = stack.pop()
                if elem != brackets[last]:
                    return False
        return not stack
    

s = "()[]{}"
print(Solution.isValid(s))