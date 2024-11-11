class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def __init__(self):
        self.nodes = []

    def inorderTraversal(self, node):
        if not node:
            return
        self.inorderTraversal(node.left)
        self.nodes.append(node.val)
        self.inorderTraversal(node.right)
    def minDiffInBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.inorderTraversal(root)
        min = float("inf")
        if self.nodes:
            for i in range(1, len(self.nodes)):
                if self.nodes[i] - self.nodes[i - 1] < min:
                    min = self.nodes[i] - self.nodes[i - 1]
        return min



root = [4,2,6,1,3]
root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(6))
sol = Solution()
a = sol.minDiffInBST(root)
print(a)