from collections import deque
class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        q = deque()
        time, fresh = 0, 0

        i_n, j_n = len(grid), len(grid[0])
        directions = [[0 , 1], [1, 0], [-1, 0], [0, -1]]
        for i in range(i_n):
            for j in range(j_n):
                if grid[i][j] == 2:
                    q.append([i,j])
                if grid[i][j] == 1:
                    fresh +=1
        while q and fresh:
            for r in range(len(q)):
                rottenX, rottenY = q.pop()
                # print(rottenX, rottenY)
                for dx, dy in directions:
                    row, col = rottenX + dx, rottenY + dy
                    if row < 0 or col < 0 or row == i_n or col == j_n:
                        continue
                    if grid[row][col] == 1:
                        fresh -= 1
                        grid[row][col] = 2
                        q.append([row,col])

            time += 1

        return time if not fresh else -1




grid = [[2,1,1],[1,1,0],[0,1,1]]
grid = [[1],[2],[1],[2]]
a = Solution().orangesRotting(grid)



