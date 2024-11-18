class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def traversePreOrder(self):
        print(self.val)
        if self.left:
            self.left.traversePreOrder()
        if self.right:
            self.right.traversePreOrder()


    def traverseInOrder(self):
        if self.left:
            self.left.traverseInOrder()
        print(self.val)
        if self.right:
            self.right.traverseInOrder()

    def traversePostOrder(self):
        if self.right:
            self.right.traversePostOrder()
        if self.left:
            self.left.traversePostOrder()
        print(self.val)

    def bfs(self):
        # find another way with deque - ???
        if self is None:
            return
        queue = [self]

        while queue:
            cur_node = queue.pop(0)

            if cur_node.left is not None:
                queue.append(cur_node.left)

            if cur_node.right is not None:
                queue.append(cur_node.right)

            print(cur_node.val)

    def dfs(self):
        pass



root = TreeNode(1,
                TreeNode(2, TreeNode(4, TreeNode(8), TreeNode(9)), TreeNode(5, TreeNode(10), TreeNode(11))),
                TreeNode(3, TreeNode(6, TreeNode(12), TreeNode(13)), TreeNode(7, TreeNode(14), TreeNode(15))),
                )
# root.traversePreOrder()
# root.traverseInOrder()
# root.traversePostOrder()
root.bfs()