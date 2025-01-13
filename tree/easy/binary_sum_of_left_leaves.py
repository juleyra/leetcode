# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        def isLeaf(root):
            return root and not root.left and not root.right

        sum = 0
        if root.left and isLeaf(root.left):
            sum += root.left.val

        return sum + self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)



root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
sol = Solution().sumOfLeftLeaves(root)
print(sol)