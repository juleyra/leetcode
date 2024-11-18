import sys
from collections import deque


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def rightSideView(self, root):
        if root is None:
            return []
        result = []
        queue = deque([root])
        while queue:
            for _ in len(queue):
                node = queue.popleft()
                if node:
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
            result.append(node.val)

        return result






# [1,2,3,null,5,6,null,4]
tree = TreeNode(1, TreeNode(2, None, TreeNode(5, TreeNode(4))), TreeNode(3, TreeNode(6)))

sol = Solution()
a = sol.rightSideView(tree)
print(a)