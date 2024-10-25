class Solution:
    def leftRightDifference(self, nums):
        leftSum = 0
        rightSum = 0
        diffArray = []
        for num in nums:
            rightSum += num
        for num in nums:
            rightSum -= num
            diffArray.append(abs(rightSum - leftSum))
            leftSum += num

        return diffArray


nums = [10,4,8,3]
solution = Solution()
print(solution.leftRightDifference(nums))