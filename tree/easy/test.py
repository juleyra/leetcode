# Definition for a binary tree node.
import sys
from collections import defaultdict


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def __init__(self):
        self.nodes = defaultdict(list)
    def ptraversal_(self, root, level):
        if not root:
            self.nodes[level].append(None)
            return
        self.nodes[level].append(root.val)
        self.ptraversal(root.left, level + 1)
        self.ptraversal(root.right, level + 1)

    def isSymmetric_(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        if not root:
            return False
        self.ptraversal(root, 0)
        # print(self.nodes)
        # sys.exit()
        for l in self.nodes.values():
            middle = len(l) // 2
            if middle > 0:
                if l[:middle] != l[:middle - 1:-1]:
                    return False
        return True

    def isSymmetric(self, root):
        def dfs(left, right):
            if not left and not right:
                return True
            if not left or not right:
                return False

            return (left.val == right.val and dfs(left.right, right.left) and dfs(left.left, right.right))

        return dfs(root.left, root.right)









root = [1,2,2,None,3,None,3]
root = TreeNode(1, TreeNode(2, None, TreeNode(3)), TreeNode(2, None, TreeNode(3)))
sol = Solution()
root = [1,2,2,3,4,4,3]
root = TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(2, TreeNode(4), TreeNode(3)))
print(sol.isSymmetric(root))