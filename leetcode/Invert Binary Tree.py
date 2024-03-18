# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        if root:
            if root.left and root.right:
                root.left, root.right = root.right, root.left
                self.invertTree(root.right)
                self.invertTree(root.left)
            elif root.left is None and root.right:
                root.left, root.right = root.right, None
                self.invertTree(root.left)
            elif root.left and root.right is None:
                root.left, root.right = None, root.left
                self.invertTree(root.right)
        return root
