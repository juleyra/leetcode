class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def depth(self, node):
        if not node:
            return 0

        leftDepth = self.depth(node.left)
        if leftDepth == -1:
            return -1
        rightDepth = self.depth(node.right)
        if rightDepth == -1:
            return -1

        if abs(leftDepth - rightDepth) > 1:
            return - 1

        return max(leftDepth, rightDepth) + 1

    def isBalanced(self, root):
        return self.depth(root) != -1



root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
sol = Solution()
a = sol.isBalanced(root)
print(a)