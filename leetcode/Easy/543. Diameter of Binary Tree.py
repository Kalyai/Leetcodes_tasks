# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        def path(node, res):
            if node is None:
                return 0

            left = path(node.left, res)
            right = path(node.right, res)

            res[0] = max(res[0], left + right)
            return 1 + max(left, right)

        if root is None:
            return 0
        res = [0]
        path(root, res)
        return res[0]

