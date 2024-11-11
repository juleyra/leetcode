class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):

    def __init__(self, root=None, low = 0, high = 0):
        self.root = root
        self.low = low
        self.high = high
        self.sum = 0

    def traverseRootInOrder(self, node):
        if not node:
            return
        self.traverseRootInOrder(node.left)
        if self.low <= node.val <= self.high:
            self.sum += node.val
        self.traverseRootInOrder(node.right)

    def rangeSumBST(self):
        self.traverseRootInOrder(self.root)
        return self.sum


root = TreeNode(10, TreeNode(5, TreeNode(3), TreeNode(7)), TreeNode(15, None, TreeNode(18)))
low = 7
high = 15

sol = Solution(root, low, high)
print(sol.rangeSumBST())