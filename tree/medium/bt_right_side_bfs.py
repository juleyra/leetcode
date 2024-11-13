import sys
from collections import deque


class TreeNode(object):
    fdnsjfnhsjkdhbnfsdjkhbfsdkjbfsdkjhbfsk
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
        k = 0
        while queue:
            level_size = len(queue)

            for i in range(level_size):
                node = queue.popright()
                if k == 1:
                    print(node.val)
                    sys.exit()
                if i == level_size - 1:
                    result.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            k+=1


        return result






# [1,2,3,null,5,6,null,4]
tree = TreeNode(1, TreeNode(2, None, TreeNode(5, TreeNode(4))), TreeNode(3, TreeNode(6)))

sol = Solution()
sol.rightSideView(tree)