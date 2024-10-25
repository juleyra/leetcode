class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        mLen = len(matrix)
        for i in range(mLen):
            for j in range(i+1, mLen):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for i in matrix:
            i.reverse()
        return matrix



matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]]
sol = Solution()
sol.rotate(matrix)