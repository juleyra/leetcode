class Solution():

    def nextGreater(self, nums):
        stack = []
        res = [-1] * len(nums)
        for i in range(len(nums) - 1, -1, -1):

            while stack and stack[-1] <= nums[i]:
                stack.pop()

            if stack:
                res[i] = stack[-1]

            stack.append(nums[i])

        return res

nums = [13, 7, 6, 12]
sol = Solution()
a = sol.nextGreater(nums)
print(a)