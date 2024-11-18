from collections import defaultdict
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):

    def __init__(self):
        self.dict = defaultdict(list)

    def dfs(self, root, level):
        if not root:
            return

        self.dict[level].append(root.val)
        self.dfs(root.left, level + 1)
        self.dfs(root.right, level + 1)


    def averageOfLevels(self, root):
        self.dfs(root, 0)
        avg = []
        for level in self.dict.values():
            avg.append(float(sum(level)/len(level)))

        return avg


root = TreeNode(1,
                TreeNode(2, TreeNode(4, TreeNode(8), TreeNode(9)), TreeNode(5, TreeNode(10), TreeNode(11))),
                TreeNode(3, TreeNode(6, TreeNode(12), TreeNode(13)), TreeNode(7, TreeNode(14), TreeNode(15))),
                )
sol = Solution()
sol.averageOfLevels(root)