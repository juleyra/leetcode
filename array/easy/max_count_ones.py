class Solution(object):
    def rowAndMaximumOnes(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
        maxCountIndex, maxCount = 0, 0
        for i in range(0, len(mat)):
            count = 0
            for j in range(0, len(mat[i])):
                if mat[i][j] == 1:
                    count += 1
            if count > maxCount:
                maxCount = count
                maxCountIndex = i
        return [maxCountIndex, maxCount]

mat = [[0,0,0],[0,1,1]]
print(Solution().rowAndMaximumOnes(mat))