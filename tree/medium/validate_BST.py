# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if not root:
                return True
            if not root.left and not root.right:
                return True
            if root.left.val >= root.val >= root.right.val:
                return False
            else:
                return (dfs(root.left) and dfs(root.right))

        return dfs(root)

root = TreeNode(3, TreeNode(9), TreeNode(2))
a = Solution().isValidBST(root)
print(a)