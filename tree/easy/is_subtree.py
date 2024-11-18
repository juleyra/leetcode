# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def isSubtree(self, root, subRoot):
        """
        :type root: Optional[TreeNode]
        :type subRoot: Optional[TreeNode]
        :rtype: bool
        """
        if not subRoot: return True
        if not root: return False
        if self.sameTree(root, subRoot):
            return True
        return (self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot))

    def sameTree(self, l, r):
        if not l and not r:
            return True

        if l and r and l.val == r.val:
            return (self.sameTree(l.left, r.left) and self.sameTree(l.right, r.right))

        return False




root = TreeNode(3, TreeNode(4, TreeNode(1), TreeNode(2)), TreeNode(5))
subRoot = TreeNode(4, TreeNode(1), TreeNode(2))
sol = Solution()
sol.isSubtree(root, subRoot)
