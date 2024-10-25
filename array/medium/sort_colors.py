class Solution(object):

    def sortColors_as_counting_algo(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        counts = [0, 0, 0]
        for color in nums:
            counts[color] += 1

        R, W, B = counts
        nums[:R] = [0] * R
        nums[R:R + W] = [1] * W
        nums[R + W:] = [2] * B

        return nums

    def sortColors_as_dutch_flag_algo(self, nums):
        low, mid = 0, 0
        high = len(nums) - 1

        while mid < high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid +=1
            if nums[mid] == 1:
                mid += 1
            if nums[mid] == 2:
                nums[mid], nums[high] = nums[high], nums[mid]
                high -=1

        return nums

nums = [0, 0, 2, 2, 1, 1, 0, 0, 2, 1, 1, 0, 2]
solution = Solution()
print(solution.sortColors_as_counting_algo(nums))
print(solution.sortColors_as_dutch_flag_algo(nums))