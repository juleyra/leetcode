from collections import defaultdict

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def __init__(self):
        self.dict = defaultdict(list)

    def dfs(self, node, depth):
        if not node:
            return

        self.dict[depth].append(node.val)
        self.dfs(node.left, depth + 1)
        self.dfs(node.right, depth + 1)

    def rightSideView(self, root):
        self.dfs(root, 1)
        the_rightest = []
        for level in self.dict.values():
            the_rightest.append(level.pop())

        return the_rightest
    #
    # def rightSideView(self, root):
    #     """
    #     :type root: Optional[TreeNode]
    #     :rtype: List[int]
    #     """
    #     if not root:
    #         return []
    #     a = [root.val]
    #     q = deque([root])
    #     while q:
    #
    #         b = q.popleft()
    #
    #         a.append(b.val)
    #         if b.right:
    #             q = deque(b.right)
    #         else:
    #             q = deque(b.left)
    #
    #     return a



# [1,2,3,null,5,6,null,4]
tree = TreeNode(1, TreeNode(2, None, TreeNode(5, TreeNode(4))), TreeNode(3, TreeNode(6)))

sol = Solution()
sol.rightSideView(tree)