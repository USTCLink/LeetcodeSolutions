class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.res = 0
        def depth(node):
            if not node:
                return 0
            leftDepth = depth(node.left)
            rightDepth = depth(node.right)
            self.res = max(self.res, leftDepth + rightDepth)
            return max(leftDepth, rightDepth) + 1
        depth(root)
        return self.res
        