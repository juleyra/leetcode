
class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        n = len(temperatures)
        result = [0] * n
        stack = []

        stack.append(0)
        for i in range(1, n):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                index = stack.pop()
                result[index] = i - index
            stack.append(i)

        return result


# temperatures = [73,74,75,71,69,72,76,73]
temperatures = [73,70,66,80]
# Output: [1,1,4,2,1,1,0,0]
sol = Solution()
a = sol.dailyTemperatures(temperatures)
print(a)