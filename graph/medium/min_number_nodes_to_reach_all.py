class Solution(object):
    def findSmallestSetOfVertices(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        hasIncomingEdge = [False] * n
        for s, e in edges:
            hasIncomingEdge[e] = True
        result = [i for i, x in enumerate(hasIncomingEdge) if not x]
        return result


edges = [[0,1],[0,2],[2,5],[3,4],[4,2]]
sol = Solution().findSmallestSetOfVertices(6, edges)
print(sol)