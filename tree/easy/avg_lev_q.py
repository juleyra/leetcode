from collections import defaultdict
from collections import deque

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):

    def __init__(self):
        self.dict = defaultdict(list)

    def averageOfLevels(self, root):
        if self is None:
            return

        queue = deque([root])
        averages = []

        while queue:
            level_sum = 0
            level_count = len(queue)

            for h in range(level_count):
                node = queue.popleft()
                level_sum += node.val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            averages.append(level_sum / level_count)





root = TreeNode(1,
                TreeNode(2, TreeNode(4, TreeNode(8), TreeNode(9)), TreeNode(5, TreeNode(10), TreeNode(11))),
                TreeNode(3, TreeNode(6, TreeNode(12), TreeNode(13)), TreeNode(7, TreeNode(14), TreeNode(15))),
                )
sol = Solution()
sol.averageOfLevels(root)
