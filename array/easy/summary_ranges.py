class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        if not len(nums):
            return nums
        res = [[nums[0]]]
        for i in range(1,len(nums)):
            if nums[i]-nums[i-1] == 1:
                res[-1].append(nums[i])
            else:
                res.append([nums[i]])
        for i in range(len(res)):
            res[i] = str(res[i][0]) if len(res[i]) == 1 else str(res[i][0]) + "->" + str(res[i][-1])
        return res




nums = [0, 1, 2, 4, 5, 7]
a = Solution().summaryRanges(nums)
print(a)
