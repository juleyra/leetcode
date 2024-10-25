class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        stack = []
        path = path.split('/')
        for elem in path:
            if elem == '..':
                if len(stack) > 0:
                    stack.pop()
            elif elem and elem != '.':
                stack.append(elem)

        return '/' + '/'.join(stack)

input = "/../"
# input = "/a//b////c/d//././/.."

solution = Solution()
print(solution.simplifyPath(input))