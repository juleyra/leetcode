class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        leftDepth = self.maxDepth(root.left)

        rightDepth = self.maxDepth(root.right)

        return max(leftDepth, rightDepth) + 1

solver = Solution()
tree = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
a = solver.maxDepth(tree)
print(a)