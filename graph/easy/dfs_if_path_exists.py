from collections import defaultdict
class Solution(object):
    def validPath(self, n, edges, source, destination):
        """
        :type n: int
        :type edges: List[List[int]]
        :type source: int
        :type destination: int
        :rtype: bool
        """

        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        visited = set()

        def dfs(node):
            if node == destination:
                return True
            visited.add(node)

            for neighbor in graph[node]:
                if neighbor not in visited:
                    if dfs(neighbor):
                        return True
            return False

        return dfs(source)

n = 3
edges = [[0,1],[1,2],[2,0]]
source = 0
destination = 2
a = Solution().validPath(n, edges, source, destination)
print(a)

n = 6
edges =  [[0,1],[0,2],[3,5],[5,4],[4,3]]
source = 0
destination = 5
b = Solution().validPath(n, edges, source, destination)
print(b)