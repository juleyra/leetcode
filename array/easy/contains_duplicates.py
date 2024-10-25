class Solution:
# O(n) complexity
    def containsDuplicate(self, nums):
      processed = set()
      for num in nums:
        if num in processed:
            return True
        processed.add(num)
      return False

# O(n) complexity
    def containsDuplicates2(self, nums):
        newSet = set(nums)
        if len(newSet) != len(nums):
            return True
        else:
            return False


result = Solution()
nums = [1, 4, 3]
print(result.containsDuplicate(nums))