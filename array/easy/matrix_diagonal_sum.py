class Solution:
    def diagonalSum(self, mat):
        total = 0
        dimention = len(mat)

        for i in range(0, dimention):
            total += mat[i][i]
            total += mat[i][dimention - 1 - i]

        if dimention % 2 != 0:
            medium = dimention // 2
            total -= mat[medium][medium]

        return total

mat = [[1,1,1,1], [1,1,1,1], [1,1,1,1],[1,1,1,1]]
solution = Solution()
print(solution.diagonalSum(mat))