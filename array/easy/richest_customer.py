class Solution:
    def maximumWealth(self, accounts) -> int:
        max = 0
        for col in accounts:
            wealth = sum(col)
            if wealth > max:
                max = wealth
        return max


accounts = [[1,2,3],[3,2,1]]
solution = Solution()
print(solution.maximumWealth(accounts))